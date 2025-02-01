from pyrogram import filters
from pyrogram.types import Message

from DeltaMusic import app
from DeltaMusic.misc import SUDOERS
from DeltaMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>Contoh :</b>\n\n/autoend [enable | disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto end stream diaktifkan.\n\nAsisten akan otomatis meninggalkan video chat setelah beberapa menit ketika tidak ada yang mendengarkan."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Auto end stream dinonaktifkan.")
    else:
        await message.reply_text(usage)
