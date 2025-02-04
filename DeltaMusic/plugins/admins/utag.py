import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from DeltaMusic import app
from DeltaMusic.utils.delta_ban import admin_filter

SPAM_CHATS = {}

@app.on_message(
    filters.command(["utag", "uall"], prefixes=["/", "@", ".", "#"]) & admin_filter
)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if len(message.text.split()) == 1:
        await message.reply_text(
            "Berikan teks untuk menandai semua, seperti » `@utag Hai Teman-teman`"
        )
        return

    text = message.text.split(None, 1)[1]
    if text:
        await message.reply_text(
            "Penandaan tanpa batas dimulai dengan sukses!\n\nMenandai dengan jeda 7 detik.\n\nMatikan penandaan dengan » /stoputag"
        )

    SPAM_CHATS[chat_id] = True
    f = True
    while f:
        if SPAM_CHATS.get(chat_id) == False:
            await message.reply_text("Penandaan tanpa batas berhasil dihentikan.")
            break
        usernum = 0
        usertxt = ""
        try:
            async for m in app.get_chat_members(message.chat.id):
                if m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 5:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}\n\n|| Matikan penandaan dengan » /stoputag ||",
                    )
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(7)
        except Exception as e:
            print(e)

@app.on_message(
    filters.command(
        ["stoputag", "stopuall", "offutag", "offuall", "utagoff", "ualloff"],
        prefixes=["/", ".", "@", "#"],
    )
    & admin_filter
)
async def stop_tagging(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if SPAM_CHATS.get(chat_id) == True:
        SPAM_CHATS[chat_id] = False
        return await message.reply_text("Tunggu sebentar, menghentikan penandaan tanpa batas...")
    else:
        await message.reply_text("Proses penandaan tidak aktif.")
