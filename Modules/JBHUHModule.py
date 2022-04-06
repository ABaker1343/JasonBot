from .JBModule import JBModule

prevMessages = []
prevAuthors = []

async def JBHUHTriggerCheck(message):
    if message.content.startswith("!HUH?"):
        return True

    if message.content.startswith("parrotme"):
        return False

    if len(prevMessages) > 10:
        prevMessages.pop()
        prevAuthors.pop()
    prevMessages.insert(0, message.content)
    prevAuthors.insert(0, message.author)
    return False

async def bringBackMessage(message):
    reply = ""
    splits = message.content.split(" ")
    if len(splits) > 1:
        try:
            if int(splits[1]) < len(prevMessages) and int(splits[1]) > -1:
                reply += prevAuthors[int(splits[1])].mention + " said: " + prevMessages[int(splits[1])]
        except:
            pass
    else:
        reply += prevAuthors[0].mention + " said: " + prevMessages[0]
    await message.channel.send(reply)

def buildModule():
    return JBModule(JBHUHTriggerCheck, bringBackMessage)