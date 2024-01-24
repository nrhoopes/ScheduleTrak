from src.model.formatExcelFile import ExcelReader
from src.controller.runtimeController import schedulerRuntimeController
import os

pathToDB = os.path.dirname(os.path.dirname(__file__)) + "\\scheduleTrakDB.db"
print(pathToDB)

reader = ExcelReader()

controller = schedulerRuntimeController(reader, "", pathToDB)

controller.startRuntime()