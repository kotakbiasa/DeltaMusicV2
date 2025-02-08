from TheApi import api
from DeltaMusic import app
from config import BANNED_USERS
from pyrogram import filters, Client
from pyrogram.enums import ChatAction
from pyrogram.types import Message


@app.on_message(filters.command(["chatgpt", "ai", "ask"]) & ~BANNED_USERS)
async def chatgpt_chat(bot: Client, message: Message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "💡 **Contoh penggunaan:\n\n/ai tulis kode situs web sederhana menggunakan HTML, CSS, dan JS?`"
        )
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    results = api.chatgpt(user_input)
    await message.reply_text(f"🤖 **Respon:**\n\n{results}")


__MODULE__ = "🤖 ChatGPT"
__HELP__ = """
Perintah:

• /advice - Dapatkan saran acak dari bot
• /ai [pertanyaan Anda] - Ajukan pertanyaan ke AI ChatGPT
• /gemini [pertanyaan Anda] - Ajukan pertanyaan ke AI Gemini Google
• /bard [pertanyaan Anda] - Ajukan pertanyaan ke Bard AI Google
