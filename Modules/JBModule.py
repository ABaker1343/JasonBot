class JBModule:
    def __init__(self, triggerCheckFunc, executionFunc):
        self.triggerCheckFunc = triggerCheckFunc
        self.executionFunc = executionFunc

    async def checkTrigger(self, message):
        result = await self.triggerCheckFunc(message)
        if type(result) is bool:
            return result
        return False

    async def execute(self, message):
        await self.executionFunc(message)