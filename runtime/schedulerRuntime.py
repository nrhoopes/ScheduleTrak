from src.model.formatExcelFile import ExcelReader
from src.controller.runtimeController import schedulerRuntimeController
import os

pathToDB = os.getenv("APPDATA") + "\\ScheduleTrak"
os.makedirs(pathToDB, exist_ok=True)
pathToDB += "\\scheduleTrakDB.db"

reader = ExcelReader()

controller = schedulerRuntimeController(reader, "", pathToDB)

controller.startRuntime()