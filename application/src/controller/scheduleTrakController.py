import os

from src.model.databaseConnection import dataBase

class scheduleTrakController:
    def __init__(self, gui) -> None:
        self.GUI = gui
        pathToDB = os.getenv("APPDATA") + "\\ScheduleTrak"
        os.makedirs(pathToDB, exist_ok=True)
        pathToDB += "\\scheduleTrakDB.db"
        self.database = dataBase(pathToDB)

    def insertNewEmail(self, 
                       email: str):
        return self.database.insertEmail(email)
    
    def insertNewMessage(self,
                         date: str,
                         message: str):
        return self.database.insertNewMessage(date, message)

    def getEmails(self):
        return self.database.getFullEmailList()
    
    def getTime(self):
        return self.database.getTime()
    
    def getPath(self):
        return self.database.getPaths()[0][1]
    
    def updateEmail(self, email: str, ping: int):
        return self.database.updateEmail(email, ping)
    
    def updateTime(self, time: str):
        return self.database.insertTime(time)
    
    def updatePath(self, path:str):
        return self.database.updatePath(path)
    