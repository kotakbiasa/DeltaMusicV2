import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from DeltaMusic import LOGGER, app, userbot
from DeltaMusic.core.call import Hotty
from DeltaMusic.plugins import ALL_MODULES
from DeltaMusic.utils.database import get_banned_users, get_gbanned


async def load_banned_users():
    """Memuat daftar pengguna yang diblokir dengan delay untuk menghindari flood wait."""
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
            await asyncio.sleep(0.5)  # Mencegah flood wait

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
            await asyncio.sleep(0.5)

    except Exception as e:
        LOGGER("YukkiMusic").error(f"Error saat memuat banned users: {e}")


async def import_modules():
    """Mengimpor semua modul secara paralel di latar belakang."""
    tasks = [asyncio.to_thread(importlib.import_module, f"DeltaMusic.plugins{mod}") for mod in ALL_MODULES]
    await asyncio.gather(*tasks)
    LOGGER("YukkiMusic.plugins").info("Successfully Imported Modules")


async def start_bot():
    """Memulai semua klien bot dan asisten secara bertahap untuk mencegah flood wait."""
    await app.start()
    await asyncio.sleep(2)  # Beri jeda sebelum userbot.start()
    await userbot.start()
    await asyncio.sleep(2)  # Beri jeda sebelum Hotty.start()
    await Hotty.start()

    # Menjalankan operasi di latar belakang
    asyncio.create_task(load_banned_users())
    asyncio.create_task(import_modules())

    LOGGER("YukkiMusic").info("All Clients Started Successfully")


async def start_stream():
    """Menunda pemanggilan stream call untuk mencegah request berlebihan saat startup."""
    await asyncio.sleep(5)  # Tunggu sebelum memulai stream call
    try:
        await Hotty.stream_call("http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4")
    except NoActiveGroupCall:
        LOGGER("YukkiMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except Exception as e:
        LOGGER("YukkiMusic").error(f"Error saat memulai stream: {e}")

    await Hotty.decorators()


async def init():
    """Fungsi utama untuk inisialisasi bot."""
    if not any([config.STRING1, config.STRING2, config.STRING3, config.STRING4, config.STRING5]):
        LOGGER("YukkiMusic").error("No Assistant Clients Vars Defined!.. Exiting Process.")
        return

    if not all([config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET]):
        LOGGER("YukkiMusic").warning("No Spotify Vars defined. Your bot won't be able to play spotify queries.")

    await start_bot()
    asyncio.create_task(start_stream())  # Menjalankan stream call di latar belakang

    LOGGER("YukkiMusic").info("Yukki Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    try:
        asyncio.run(init())
    except KeyboardInterrupt:
        LOGGER("YukkiMusic").info("Stopping Yukki Music Bot! GoodBye")
