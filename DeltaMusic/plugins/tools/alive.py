import asyncio

from DeltaMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://envs.sh/yJN.mp4",
        caption=f"❤️ Hai {message.from_user.mention}\n\n🔮 Saya adalah {MUSIC_BOT_NAME}\n\n✨ Saya adalah bot pemutar musik yang cepat dan kuat dengan beberapa fitur keren.\n\n💫 Jika Anda memiliki pertanyaan, bergabunglah dengan grup dukungan kami 🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="☆ Kotak Biasa 💗", url=f"https://t.me/KotakBiasa"
            ),
            InlineKeyboardButton(
                text="☆ Dukungan 💗", url=f"https://t.me/DeltaStreamChat"
            ),
        ],
                [
            InlineKeyboardButton(
                text="☆ Channel 💗", url=f"https://t.me/KotakBiasaCH"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "✯ Tutup ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
