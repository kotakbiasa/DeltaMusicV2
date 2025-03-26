import asyncio 
import aiorun
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
import uvloop  # Add this import

import config 
from aiorun import run
from DeltaMusic import LOGGER, app, userbot
from DeltaMusic.core.call import Hotty
from DeltaMusic.misc import sudo
from DeltaMusic.plugins import ALL_MODULES
from DeltaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# Initialize SUDOERS as an empty set or load it from a configuration
SUDOERS = set()

async def sudo():
    global SUDOERS
    SUDOERS = {int(user) for user in SUDOERS if isinstance(user, (int, str))}

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Variabel klien asisten tidak ditentukan, keluar...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DeltaMusic.plugins" + all_module)
    LOGGER("DeltaMusic.plugins").info("Berhasil Mengimpor Modul...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://envs.sh/yJN.mp4")
    except NoActiveGroupCall:
        LOGGER("DeltaMusic").error(
            "Silakan nyalakan videochat dari grup log\saluran Anda.\n\nMenghentikan Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("DeltaMusic").info(
        "Bergabunglah dengan @DeltaStreamChat untuk dukungan dan @KotakBiasaCH untuk pembaruan terbaru!"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("DeltaMusic").info("Menghentikan Delta Music Bot...")

uvloop.install()

async def job():
    raise Exception("ouch")


async def other_job():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("other_job was cancelled!")


if __name__ == "__main__": 
    aiorun.logger.disabled = True  
    aiorun.run(init)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(job())
    loop.create_task(other_job())

    def handler(loop, context):
        # https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler
        print(f'Stopping loop due to error: {context["exception"]} ')
        loop.stop()

    loop.set_exception_handler(handler=handler)

    run(loop=loop)