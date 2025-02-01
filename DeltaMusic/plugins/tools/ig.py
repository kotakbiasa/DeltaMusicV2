import requests
from pyrogram import filters

from DeltaMusic import app

@app.on_message(filters.command(["ig", "instagram", "reel"]))
async def download_instagram_video(client, message):
    if len(message.command) < 2:
        await message.reply_text(
            "Silakan berikan URL reel Instagram setelah perintah"
        )
        return
    a = await message.reply_text("Memproses...")
    url = message.text.split()[1]
    api_url = (
        f"https://nodejs-1xn1lcfy3-jobians.vercel.app/v2/downloader/instagram?url={url}"
    )

    response = requests.get(api_url)
    data = response.json()

    if data["status"]:
        video_url = data["data"][0]["url"]
        await a.delete()
        await client.send_video(message.chat.id, video_url)
    else:
        await a.edit("Gagal mengunduh reel")

__MODULE__ = "Instagram"
__HELP__ = """/reel [URL reel Instagram] - Untuk mengunduh reel dengan bot
/ig [URL reel Instagram] - Untuk mengunduh reel dengan bot
/instagram [URL reel Instagram] - Untuk mengunduh reel dengan bot
