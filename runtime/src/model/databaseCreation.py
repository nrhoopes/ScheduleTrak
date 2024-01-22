import sqlite3
from sqlite3 import Error

class dataBase:
    def __init__(self, 
                 dbConnPath: str):
        self.dbFile = dbConnPath
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.dbFile)
            print("SQLITE VERSION: " + sqlite3.version)
        except Error as e:
            print(e)
            quit()
        finally:
            if(self.conn):
                self.conn.execute(''' CREATE TABLE IF NOT EXISTS schedule (
                             person TEXT PRIMARY KEY NOT NULL,
                             job TEXT,
                             location TEXT
                );
                ''')

                self.conn.execute(''' CREATE TABLE IF NOT EXISTS paths (
                             name TEXT PRIMARY KEY NOT NULL,
                             path TEXT NOT NULL
                );
                ''')

                self.conn.execute(''' CREATE TABLE IF NOT EXISTS emailList (
                             emailAddr TEXT PRIMARY KEY NOT NULL,
                             emailPings INTEGER
                );
                ''')

                self.conn.execute(''' CREATE TABLE IF NOT EXISTS timeForUpdate (
                             time TEXT PRIMARY KEY NOT NULL
                );
                ''')

                self.conn.execute(''' CREATE TABLE IF NOT EXISTS messages (
                                  date TEXT PRIMARY KEY NOT NULL,
                                  message TEXT NOT NULL
                ); 
                ''')

                self.conn.execute(''' INSERT OR IGNORE INTO paths (name, path) VALUES (?, ?); ''', ('Excel sheet', 'schedule.xlsx'))
                self.conn.commit()

    def getConn(self):
        return self.conn

    def insertEmail(self, 
                    emailAddr: str, 
                    emailPing: bool):
        status = self.conn.execute(''' INSERT INTO emailList (emailAddr, emailPings) VALUES (?, ?)''', (emailAddr, emailPing))
        if status:
            self.conn.commit()
            return status
        else:
            print("email insertion failed")
            return status
        
    def insertPath(self, 
                   pathName: str,
                   path: str):
        status = self.conn.execute(''' INSERT INTO paths (name, path) VALUE (?, ?)''', (pathName, path))
        if status:
            self.conn.commit()
            return status
        else:
            print("path insertion failed")
            return status
        
    def insertSchdule(self, 
                      person: str, 
                      job: str, 
                      location: str):
        status = self.conn.execute(''' INSERT INTO schedule (person, job, location) VALUES (?, ?, ?)''', (person, job, location))
        if status:
            self.conn.commit()
            return status
        else:
            print("schedule insertion failed")
            return status
        
    def insertTime(self,
                   time: str):
        self.conn.execute(''' DELETE FROM timeForUpdate;''')
        status = self.conn.execute(''' INSERT INTO timeForUpdate (time) values (?); ''', (time, ))
        if status:
            self.conn.commit()
            return status
        else:
            print("time insertion failed")
            return status
        
    def getSchedules(self):
        return list(self.conn.execute(''' SELECT * FROM schedule; '''))
    
    def getActiveEmailList(self):
        activeEmails = list(self.conn.execute(''' SELECT * FROM emailList WHERE emailPings = 1;'''))
        emailList = []
        for email in activeEmails:
            emailList.append(email[0])
        return emailList
    
    def getFullEmailList(self):
        return list(self.conn.execute(''' SELECT * FROM emailList; '''))
    
    def getPaths(self):
        return list(self.conn.execute(''' SELECT * FROM paths; '''))
    
    def getTime(self):
        time = "12:34"
        try:
            time = list(self.conn.execute(''' SELECT * FROM timeForUpdate; '''))[0][0]
            return time
        except IndexError:
            return time
        
    def getMessages(self, date: str):
        msgs = list(self.conn.execute(''' SELECT * FROM messages WHERE date = ?; ''', (date,)))
        if msgs == []:
            return ''
        else:
            return msgs[0][1]
    
    def updateEmail(self, email: str, ping: bool):
        try:
            status = self.conn.execute(''' UPDATE emailList SET emailPings = ? WHERE emailAddr = ?''', (ping, email))
            return status
        except Error as e:
            print(e)
    
    def clearSchedule(self):
        return list(self.conn.execute(''' DELETE FROM schedule; '''))
