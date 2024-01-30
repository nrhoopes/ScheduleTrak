import asyncio
import logging
import pickle
import os
from datetime import datetime
from typing import List, Tuple, Any
from time import sleep

from asyncua import Server, ua
from asyncua.common.methods import uamethod

class SchedulerOPCpyServer:
    def __init__(self, uri, objects) -> None:
        self.uri = uri
        self.objects = objects
        self.allObjects = {}
        self.launchServer()

    async def main(self):
        _logger = logging.getLogger(__name__)
        # Setup Server
        self.server = Server()
        await self.server.init()
        self.server.set_endpoint('opc.tcp://localhost:4840/server/')

        # Setup namespace
        self.idx = await self.server.register_namespace(self.uri)

        for obj in self.objects:
            await self.newObj(obj[0], obj[1])

        _logger.info("Starting Server")
        newValue = await self.getValueFromVariable("NEWmyObjectNEW", "AnotherTag")
        print("Server Setup Complete")
        async with self.server:
            while True:
                await asyncio.sleep(1)
                newValue = newValue + 1
                await self.updateObj("NEWmyObjectNEW", "AnotherTag", newValue)
                _logger.info("A second has passed! It is now " + datetime.now().strftime("%H:%M:%S"))

    def launchServer(self):
        # logging.basicConfig(level=logging.DEBUG)
        print("Launching Server...")
        asyncio.run(self.main(), debug=False)

    async def newObj(self, 
               objName: str,
               variables: List[Tuple[str, Any]] = []):
        varsToAdd = {}
        obj = await self.server.nodes.objects.add_object(self.idx, objName)
        for var in variables:
            newVar = await obj.add_variable(self.idx, var[0], var[1])
            await newVar.set_writable()
            varsToAdd[var[0]] = newVar
        self.allObjects[objName] = varsToAdd
        print(self.allObjects)

    async def updateObj(self,
                        objName: str,
                        variableName: str,
                        newValue: Any):
        variables = self.allObjects[objName]
        for i in variables:
            if i == variableName:
                await variables[i].write_value(newValue)
                return True
        return False
    
    async def getValueFromVariable(self,
                             objName: str,
                             variableName: str):
        obj = self.allObjects[objName]
        return await obj[variableName].get_value()


# sleep(5)

pathToPickle = os.getenv("APPDATA") + "\\ScheduleTrak"
os.makedirs(pathToPickle, exist_ok=True)
pathToPickle += "\\schedules.pickle"

colorKey = []
schedules = []

with open(pathToPickle, 'rb') as f:
    colorKey = pickle.load(f)
    schedules = pickle.load(f)

colorKeyForOPCUA = ["colorKey", []]
names = ["names", []]
jobs = ["jobs", []]
locations = ["locations", []]

for i in colorKey:
    colorKeyForOPCUA[1].append((colorKey[i], i))

for num, i in enumerate(schedules):
    if num == 0:
        continue
    person = 'Person' + str(num)
    names[1].append((person, str(i[0])))
    jobs[1].append((person, str(i[1])))
    locations[1].append((person, str(i[2])))


number = 125
number2 = 42
string = "123 Test String 123"

serv = SchedulerOPCpyServer("https://dentechindustrial.com/ScheduleTrak", [["NEWmyObjectNEW", [("NEWmyVarNEW", number), ("AnotherTag", number2), ("PerhapsAString", string)]],
                                                                          colorKeyForOPCUA, jobs, locations, names])





