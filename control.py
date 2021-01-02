import aiohttp
import pysmartthings
import asyncio

token = ''
device_name = ''
async def control():
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
    asyncio.run(control())