from discord import client
from .JBModule import JBModule

async def parrotTriggerCheck(message):
    if message.content.lower().startswith("parrotme"):
        return True
    return False

async def parrotMessage(message):
    channel = client.get_channel(730422286922022926)
    await channel.send(message.content[8:])

def buildModule(_client):
    global client
    client = _client
    return JBModule(parrotTriggerCheck, parrotMessage)