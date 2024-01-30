from src.model.formatExcelFile import ExcelReader
from src.controller.runtimeController import schedulerRuntimeController
from sys import exit
from time import sleep
import os

pathToDB = os.getenv("APPDATA") + "\\ScheduleTrak"
os.makedirs(pathToDB, exist_ok=True)
pathToPickle = pathToDB + "\\schedules.pickle"
pathToDB += "\\scheduleTrakDB.db"

user = os.getenv("py_outlook_user")
pas = os.getenv("py_outlook_pass")
send = os.getenv("py_outlook_sender")

if user is None or pas is None or send is None:
    print("Please setup environment variables prior to launching the runtime.  See README.md for more information, or launch the included 'setEmailSender.bat' tool to help you.")
    sleep(10)
    exit()

reader = ExcelReader()

controller = schedulerRuntimeController(reader, "", pathToDB, pathToPickle)

controller.startRuntime()