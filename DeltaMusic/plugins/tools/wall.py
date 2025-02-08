import random

import requests
from DeltaMusic import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@app.on_message(filters.command(["wall", "wallpaper"]))
async def wall(_, message: Message):
    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        text = None
    if not text:
        return await message.reply_text(
            "⚠️ Harap berikan kata kunci untuk pencarian.")
    m = await message.reply_text("🔍")
    try:
        url = requests.get(f"https://api.safone.dev/wall?query={text}").json()[
            "results"
        ]
        ran = random.randint(0, 7)
        await message.reply_photo(
            photo=url[ran]["imageUrl"],
            caption=f"**Diminta oleh :** {message.from_user.mention}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("🌐 Link", url=url[ran]["imageUrl"])],
                ]
            ),
        )
        await m.delete()
    except Exception as e:
        await m.edit_text(
            f"⚠️ Tidak ada wallpaper yang ditemukan untuk : `{text}`",
        )


__MODULE__ = "🖼️ Wallpaper"
__HELP__ = """
📌 Perintah:

• /wall - Unduh dan kirim wallpaper.

Informasi:

- Bot ini menyediakan perintah untuk mengunduh dan mengirim wallpaper.
- Gunakan perintah /wall dengan kata kunci untuk mencari dan mengirim wallpaper di chat.

Catatan:

- Perintah ini dapat digunakan untuk mengunduh dan mengirim wallpaper.
"""