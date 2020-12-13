"""Sample code to get the device status from V-ZUG Device."""
import asyncio

from vzug.vzug import VZUG

IP_ADDRESS = "YOUR_IP"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

async def main():
    """Sample code to work with a V-ZUG Device."""
    async with VZUG(IP_ADDRESS, USERNAME, PASSWORD) as vzug:
        # Collect the data of the current state
        await vzug.get_device_status()
        await vzug.get_program_status()
        print("Device details:", vzug.device_status)
        print("Program details:", vzug.program_status)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())