import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from config import LOGGER_ID as LOG_GROUP_ID
from DeltaMusic import app
from DeltaMusic.core.userbot import Userbot
from DeltaMusic.utils.database import delete_served_chat
from DeltaMusic.utils.database import get_assistant


photo = [
    "https://te.legra.ph/file/758a5cf4598f061f25963.jpg",
    "https://te.legra.ph/file/30a1dc870bd1a485e3567.jpg",
    "https://te.legra.ph/file/d585beb2a6b3f553299d2.jpg",
    "https://te.legra.ph/file/7df9e128dd261de2afd6b.jpg",
    "https://te.legra.ph/file/f60ebb75ad6f2786efa4e.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "Grup Privat"
                )
                msg = (
                    f"**📝Bot Musik Ditambahkan Di #Grup_Baru**\n\n"
                    f"**📌Nama Chat:** {message.chat.title}\n"
                    f"**🍂ID Chat:** {message.chat.id}\n"
                    f"**🔐Username Chat:** @{username}\n"
                    f"**📈Jumlah Anggota:** {count}\n"
                    f"**🤔Ditambahkan Oleh:** {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"Ditambahkan Oleh",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")
