import time
import pickle
from datetime import datetime, date
from src.model.emailer import Emailer
from src.model.databaseCreation import dataBase

class schedulerRuntimeController:
    def __init__(self, 
                 reader, 
                 timeToSendUpdate: str = '', 
                 pathToDB: str = 'scheduleTrakDB.db',
                 pathToPickle: str = 'schedules.pickle') -> None:
        self.reader = reader
        self.pathToPickle = pathToPickle
        self.database = dataBase(pathToDB)
        self.customTime = timeToSendUpdate

        self.findPath()

        self.__today = []
        self.findTime()
        
        self.findEmails()

        # SETTING THIS BIT TO TRUE WILL IMMEDIATELY SEND AN EMAIL ON STARTUP
        self.DEBUGsend = True


    def startRuntime(self):
        while True:
            self.findTime()
            self.findPath()
            self.findEmails()
            currentTime = datetime.now().strftime("%H:%M")

            dayOfWeek = date.today().weekday()

            if (currentTime == self.__time and dayOfWeek < 5) or self.DEBUGsend:
                self.Email = Emailer()
                today = self.getToday() # Today must be acquired before the key
                try:
                    self.readerKey = self.reader.getKey()
                except Exception as e:
                    print("An error has occurred with reading the file given.  Are you sure it is formatted correctly?: " + e)
                    return None
                self.todaysMessage = self.database.getMessages(date.today().strftime("%Y-%m-%d")) # Expect String
                self.__pickleTodaysData(self.pathToPickle)
                self.Email.sendDailyUpdate(self.__emailList, today, self.reader.getKey(), self.todaysMessage)
                self.Email.logout()
                del self.Email
                self.DEBUGsend = False
            print('Sleeping... @ ' + currentTime)
            time.sleep(60) 

    def findTime(self):
        if self.customTime != '':
            self.__time = self.customTime # HH:MM format
        else:
            self.__time = self.database.getTime() # HH:MM format

        return self.__time
    
    def findEmails(self):
        self.__emailList = self.database.getActiveEmailList()
    
    def findPath(self):
        try:
            self.reader.setFilepath(self.database.getPaths()[0][1])
        except IndexError as e:
            print(e)

    def getToday(self):
        try:
            self.__today = self.reader.getTodaysSchedule()
        except Exception as e:
            print("An error has occurred with reading the file given.  Are you sure it was formatted correctly?: " + e)
            return None

        self.database.clearSchedule()
        for rowNum, i in enumerate(self.__today):
            if rowNum == 0:
                continue
            else:
                self.database.insertSchdule(i[0], i[1], i[2])
        return self.__today
    
    def __pickleTodaysData(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.readerKey, f, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.__today, f, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.todaysMessage, f, pickle.HIGHEST_PROTOCOL)