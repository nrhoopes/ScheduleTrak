from datetime import datetime, date
from src.model.emailer import Emailer
from src.model.databaseCreation import dataBase
import time

class schedulerRuntimeController:
    def __init__(self, 
                 reader, 
                 timeToSendUpdate: str = '', 
                 pathToDB: str = 'runtimeDB.db') -> None:
        self.reader = reader
        self.database = dataBase(pathToDB)
        self.customTime = timeToSendUpdate

        self.findPath()

        self.__today = []
        self.findTime()
        
        self.findEmails()

        self.DEBUGsend = False


    def startRuntime(self):
        while True:
            self.findTime()
            self.findPath()
            self.findEmails()
            currentTime = datetime.now().strftime("%H:%M")
            if currentTime == self.__time or self.DEBUGsend:
                self.Email = Emailer()
                today = self.getToday() # Today must be acquired before the key
                self.Email.sendDailyUpdate(self.__emailList, today, self.reader.getKey(), self.database.getMessages(date.today().strftime("%Y-%m-%d")))
                self.Email.logout()
                del self.Email
                self.DEBUGsend = False
            print('Sleeping... ')
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
        self.__today = self.reader.getTodaysSchedule()
        self.database.clearSchedule()
        for rowNum, i in enumerate(self.__today):
            if rowNum == 0:
                continue
            else:
                self.database.insertSchdule(i[0], i[1], i[2])
        return self.__today