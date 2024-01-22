from src.view.scheduleTrakViewDriver import scheduleTrakViewDriver
from src.controller.scheduleTrakController import scheduleTrakController

gui = scheduleTrakViewDriver()

controller = scheduleTrakController(gui)

gui.assignController(controller)

gui.launch()