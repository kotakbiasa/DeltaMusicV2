import re

import requests
from DeltaMusic import app
from config import LOG_GROUP_ID
from pyrogram import filters
from pyrogram.types import Message


@app.on_message(filters.command(["ig", "instagram", "reel"]))
async def download_instagram_video(_, message: Message):
    if len(message.command) < 2:
        await message.reply_text(
            "Harap berikan URL reel Instagram setelah perintah 📲"
        )
        return
    url = message.text.split()[1]
    if not re.match(
            re.compile(r"^(https?://)?(www\.)?(instagram\.com|instagr\.am)/.*$"), url
    ):
        return await message.reply_text(
            "URL yang diberikan tidak valid untuk Instagram 😅"
        )
    a = await message.reply_text("Memproses...⏳")
    api_url = f"https://insta-dl.hazex.workers.dev/?url={url}"

    response = requests.get(api_url)
    try:
        result = response.json()
        data = result["result"]
    except Exception as e:
        f = f"𝗘𝗿𝗿𝗼: \n{e} ❌"
        try:
            await a.edit(f)
        except Exception:
            await message.reply_text(f)
            return await app.send_message(LOG_GROUP_ID, f)
        return await app.send_message(LOG_GROUP_ID, f)
    if not result["error"]:
        video_url = data["url"]
        duration = data["duration"]
        quality = data["quality"]
        type = data["extension"]
        size = data["formattedSize"]
        caption = f"**Durasi:** {duration} 🕒\n**Kualitas:** {quality} 📹\n**Tipe:** {type} 🎥\n**Ukuran:** {size} 💾"
        await a.delete()
        await message.reply_video(video_url, caption=caption)
    else:
        try:
            return await a.edit("Gagal mengunduh reel ❗")
        except Exception:
            return await message.reply_text("Gagal mengunduh reel ❗")


__MODULE__ = "📲Reel"
__HELP__ = """
Pengunduh Reels Instagram:

• /ig [URL]: Unduh reels Instagram. Berikan URL reel setelah perintah
• /instagram [URL]: Unduh reels Instagram. Berikan URL reel setelah perintah
• /reel [URL]: Unduh reels Instagram. Berikan URL reel setelah perintah
"""