from src.view.scheduleTrakViewDriver import scheduleTrakViewDriver
from src.controller.scheduleTrakController import scheduleTrakController
from os import path as osPATH

pathToSrc = osPATH.dirname(__file__)

gui = scheduleTrakViewDriver(pathToSrc)

controller = scheduleTrakController(gui)

gui.assignController(controller)

gui.launch()