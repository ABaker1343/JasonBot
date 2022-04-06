from .JBModule import JBModule

async def JBDubConverterTriggerCheck(message):
    if " " not in message.content and len(message.content) > 4 and message.content.isalpha() and not message.content.startswith("dub"):
        return True
    return False

async def JBConvertToDub(message):
    dubWord = ""
    dubString = "dub"
    for i in range(len(message.content)):
        if i > 2:
            if message.content[i] == message.content[i-1]:
                continue
            dubWord += message.content[i]
        else:
            dubWord += dubString[i]
    await message.channel.send(dubWord)

def buildModule():
    return JBModule(JBDubConverterTriggerCheck, JBConvertToDub)