import discord
import random
import json
import re
import numpy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from Modules import *

class myClient (discord.Client):

    #list of JBModules
    JBModuleList = []

    async def on_ready(self):
        print("logged in")

    async def on_message(self, message):
        if message.author == self.user:
            return
        for module in self.JBModuleList:
            result = await module.checkTrigger(message)
            if result:
                await module.execute(message)

# get the client token using the config.json file
jsonData = json.load(open("config.json"))
clientToken = jsonData["token"]


client = myClient()
client.JBModuleList.append(JBDubConverter.buildModule())
client.JBModuleList.append(JBDubTracker.buildModule(client))
client.JBModuleList.append(JBHUHModule.buildModule())
client.JBModuleList.append(JBNonTriggerCommands.buildModule())
client.JBModuleList.append(JBQuestionModule.buildModule())
client.JBModuleList.append(JBParrotModule.buildModule(client))
client.run(clientToken)
