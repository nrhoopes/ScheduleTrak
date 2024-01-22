from src.model.formatExcelFile import ExcelReader
from src.controller.runtimeController import schedulerRuntimeController

reader = ExcelReader()

controller = schedulerRuntimeController(reader, "", "runtimeDB.db")

controller.startRuntime()