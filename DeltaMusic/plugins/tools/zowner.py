import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from DeltaMusic import app
from DeltaMusic.mongo.afkdb import LOGGERS as OWNERS
from DeltaMusic.utils.database import add_served_chat, get_assistant


@app.on_message(filters.command("repo"))
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1aac9a42f6f35138da34b.jpg",
        caption=f"""🍁Klik tombol di bawah ini untuk mendapatkan repo!🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sumber", url=f"https://github.com/kotakbiasa/DeltaStream"
                    )
                ]
            ]
        ),
    )


@app.on_message(filters.command("clone"))
async def clones(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1aac9a42f6f35138da34b.jpg",
        caption=f"""**Anda bukan pengguna Sudo, jadi Anda tidak diizinkan untuk mengkloning saya.**\n**Klik tombol di bawah ini dan host secara manual atau hubungi pemilik atau pengguna Sudo untuk mengkloning.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sumber", url=f"https://github.com/kotakbiasa/DeltaStream"
                    )
                ]
            ]
        ),
    )


# --------------------------------------------------------------------------------- #


@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #


import asyncio


@app.on_message(filters.command("gadd") & filters.user(int(OWNERS)))
async def add_allbot(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**⚠️ Format perintah tidak valid. Silakan gunakan seperti ini » `/gadd @DeltaStreamBot`**"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **Menambahkan bot yang diberikan ke semua obrolan!**")
        await userbot.send_message(bot_username, f"/start")
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001754457302:
                continue
            try:

                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🔂 Menambahkan {bot_username}**\n\n**➥ Berhasil ditambahkan di {done} obrolan ✅**\n**➥ Gagal di {failed} obrolan ❌**\n\n**➲ Ditambahkan oleh»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🔂 Menambahkan {bot_username}**\n\n**➥ Berhasil ditambahkan di {done} obrolan ✅**\n**➥ Gagal di {failed} obrolan ❌**\n\n**➲ Ditambahkan oleh»** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits

        await lol.edit(
            f"**➻ Bot {bot_username} berhasil ditambahkan 🎉**\n\n**➥ Berhasil ditambahkan di {done} obrolan ✅**\n**➥ Gagal di {failed} obrolan ❌**\n\n**➲ Ditambahkan oleh»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")


__MODULE__ = "Sumber"
__HELP__ = """
## Modul Sumber Repo

Modul ini menyediakan perintah utilitas bagi pengguna untuk berinteraksi dengan bot.

### Perintah:
- `/repo`: Dapatkan tautan ke repositori kode sumber bot.
"""
