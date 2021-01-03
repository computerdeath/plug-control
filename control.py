import aiohttp
import pysmartthings
import asyncio
import os 

device_name = ''
path = os.path.dirname(__file__)

def getToken():
    token_file = os.path.join(path,'token.key')
    token_file = open(token_file,'r')
    token = token_file.read().strip()
    token_file.close()
    return token

async def control(token):
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session,token)
        devices = await api.devices()
        for device in devices:
            if device.label == device_name:
                await device.status.refresh()
                state = device.status.values['switch']
                if state == 'on':
                    await device.command("main","switch","off")
                if state == 'off':
                    await device.command("main","switch","on")
if __name__ == "__main__":
    token = getToken()
    asyncio.run(control(token))
