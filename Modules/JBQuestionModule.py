import numpy
import json
import re
from .JBModule import JBModule

def LoadQuestionResponses():
    with open("QuestionResponses.json") as file:
        responseString = file.read()
    response_json = json.loads(responseString)
    dubResponses = response_json[0]
    questionResponses = response_json[1]

    return dubResponses, questionResponses


async def JBQuestionTriggerCheck(message):
    if re.search("^is .* a dub\?$",message.content.lower()):
        dubQuestion = True
        return True
    if re.search("^(is|are|does|do|should|will) .*\?$", message.content.lower()):
        dubQuestion = False
        return True
    return False

async def RespondToQuestion(message):
    if dubQuestion:
        rand = numpy.random.randint(len(dubResponses))
        await message.channel.send(dubResponses[rand])
    else:
        rand = numpy.random.randint(len(questionResponses))
        await message.channel.send(questionResponses[rand])

def buildModule():
    return JBModule(JBQuestionTriggerCheck, RespondToQuestion)
    
dubQuestion = False
dubResponses, questionResponses = LoadQuestionResponses()
print(questionResponses)