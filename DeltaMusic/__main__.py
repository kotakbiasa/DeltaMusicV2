import asyncio
import aiorun
import importlib
import sys
import uvloop
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DeltaMusic import LOGGER, app, userbot
from DeltaMusic.core.call import Hotty
from DeltaMusic.misc import sudo
from DeltaMusic.plugins import ALL_MODULES
from DeltaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    """Fungsi utama untuk menginisialisasi bot."""
    if not any([config.STRING1, config.STRING2, config.STRING3, config.STRING4, config.STRING5]):
        LOGGER(__name__).error("Variabel klien asisten tidak ditentukan, keluar...")
        sys.exit()

    try:
        users = await get_gbanned()
        BANNED_USERS.update(users)

        users = await get_banned_users()
        BANNED_USERS.update(users)
    except Exception as e:
        LOGGER(__name__).error(f"Error saat mengambil daftar banned users: {e}")

    await app.start()

    for module in ALL_MODULES:
        importlib.import_module(f"DeltaMusic.plugins.{all_modules}")

    LOGGER("DeltaMusic.plugins").info("Berhasil mengimpor semua modul.")

    await userbot.start()
    await Hotty.start()

    try:
        await Hotty.stream_call("https://envs.sh/yJN.mp4")
    except NoActiveGroupCall:
        LOGGER("DeltaMusic").error(
            "Silakan nyalakan videochat dari grup log/saluran Anda.\n\nMenghentikan Bot..."
        )
        sys.exit()
    except Exception as e:
        LOGGER("DeltaMusic").error(f"Error saat memulai stream: {e}")

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

def handler(loop, context):
    exception = context.get("exception")
    if exception:
        print(f"Stopping loop due to error: {exception}")
    loop.stop()

if __name__ == "__main__":
    aiorun.logger.disabled = True
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.set_exception_handler(handler)

    try:
        aiorun.run(init())
    except Exception as e:
        LOGGER("DeltaMusic").error(f"Bot berhenti karena error: {e}")
