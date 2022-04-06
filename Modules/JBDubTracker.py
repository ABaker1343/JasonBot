from discord import Client
import json
from .JBModule import JBModule

async def showDubsTriggerCheck(message):
    if message.content.lower() == "jb.showdubs":
        return True
    return False

async def JBShowDubs(message):
    returnString = ""

    with open("dubs.json") as file:
        dubData = file.read()

    dubDict = json.loads(dubData)
    for i in range(len(dubDict)):
        #u = await self.fetch_user(dubDict[i]["id"])
        #name = u.name
        u = await client.fetch_user(dubDict[i]["id"])
        returnString += u.name + " Ws: " + str(dubDict[i]["Ws"]) + ", Ls: " + str(dubDict[i]["Ls"]) + "\n"
        
    await message.channel.send(returnString)

def buildModule(_client):
    global client
    client = _client
    return JBModule(showDubsTriggerCheck, JBShowDubs)

client = None