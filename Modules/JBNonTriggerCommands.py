import numpy
import json
from .JBModule import JBModule

async def noTriggerCheck(message):
    return True

async def incrementDubs(dub, uid):
    dubData = ""
    with open("dubs.json") as file:
        dubData = file.read()
    dubDict = json.loads(dubData)
        
    if dub:
        for i in range(len(dubDict)):
            if dubDict[i]["id"] == uid:
                    dubDict[i]["Ws"] += 1
    else:
        for i in range(len(dubDict)):
            if dubDict[i]["id"] == uid:
                dubDict[i]["Ls"] += 1
        
    with open("dubs.json", "w") as file:
        json_string = json.dumps(dubDict)
        file.write(json_string)


async def checkForDubs(message):
    rand = numpy.random.randint(100)
    if rand == 0:
        await message.channel.send("W")
        await incrementDubs(True, message.author.id)
    if rand == 1:
        await message.channel.send("L")
        await incrementDubs(False, message.author.id)

def buildModule():
    return JBModule(noTriggerCheck, checkForDubs)