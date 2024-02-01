import sqlite3
from sqlite3 import Error
from sys import exit

# Tools only needed by the GUI for talking to the database

class dataBase:
    def __init__(self,
                 dbConnPath: str) -> None:
        self.dbFile = dbConnPath
        self.conn = None
        print(self.dbFile)
        try:
            self.conn = sqlite3.connect(self.dbFile)
            print("SQLITE VERSION: " + sqlite3.version + " CONNECTED SUCCESSFULLY")
        except Error as e:
            print(e)
            # exit()
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
                    emailPing: bool = 1):
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
        status = self.conn.execute(''' INSERT INTO paths (name, path) VALUES (?, ?)''', (pathName, path))
        if status:
            self.conn.commit()
            return status
        else:
            print("path insertion failed")
            return status
        
    def insertTime(self,
                   time: str):
        self.conn.execute(''' DELETE FROM timeForUpdate;''')
        status = self.conn.execute(''' INSERT INTO timeForUpdate (time) VALUES (?); ''', (time, ))
        if status:
            self.conn.commit()
            return status
        else:
            print("time insertion failed")
            return status
        
    def insertNewMessage(self, date: str, message: str):
        messageExists = list(self.conn.execute(''' SELECT * FROM messages WHERE date = ?; ''', (date,)))
        if messageExists == []: # Date doesn't already exist
            self.conn.execute(''' INSERT INTO messages (date, message) VALUES (?, ?); ''', (date, message))
            self.conn.commit()
            return
        else: # Date already contains a message
            newMessage = messageExists[0][1] + '\n' + message
            self.conn.execute(''' UPDATE messages SET message = ? WHERE date = ?; ''', (newMessage, date))
            self.conn.commit()
            return

        # Test output to see messages when they are put into the DB.  Make sure to remove return statement above
        # messageExists = list(self.conn.execute(''' SELECT * FROM messages WHERE date = ?; ''', (date,)))
        # print(messageExists)


    
    def getFullEmailList(self):
        return list(self.conn.execute(''' SELECT * FROM emailList; '''))
    
    def updateEmail(self, email: str, ping: int):
        try:
            status = self.conn.execute(''' UPDATE emailList SET emailPings = ? WHERE emailAddr = ?; ''', (ping, email))
            self.conn.commit()
            return status
        except Error as e:
            print(e)

    def updatePath(self, path:str):
        try:
            status = self.conn.execute(''' UPDATE paths SET path = ? WHERE name = ?; ''', (path, 'Excel sheet'))
            self.conn.commit()
            return status
        except Error as e:
            print(e)
    
    def getPaths(self):
        paths = list(self.conn.execute(''' SELECT * FROM paths; '''))
        if paths == []:
            return [['Excel Sheet', 'schedule.xlsx']]
        else:
            return paths
    
    def getTime(self):
        time = "12:34"
        try:
            time = list(self.conn.execute(''' SELECT * FROM timeForUpdate; '''))[0][0]
            return time
        except IndexError:
            return time

