import requests
from MukeshAPI import api  # Assuming this API handles Gemini requests
from DeltaMusic import app
from pyrogram import filters, Client
from pyrogram.enums import ChatAction
from pyrogram.types import Message
from DeltaMusic.utils.decorators import language  # Import the language decorator
from strings import get_string  # Assuming you have a strings file for localization

async def gemini_chatbot(client, message: Message, strings):
    cmd = message.command
    if len(cmd) == 1:
        return await message.reply_text(
            strings("no_question").format(cmd=cmd[0]), quote=True
        )

    # Remove the API key check; not relevant for this adaptation
    user_id = message.from_user.id if message.from_user else message.sender_chat.id

    reply = await message.reply_text(strings("find_answers_str"), quote=True)

    #  Adapt the conversation handling to work within the function scope.
    #  This example doesn't persist conversations across different requests.
    #  For persistence, you'd need to store `gemini_conversations` somewhere
    #  like a database.
    conversation = [
        {"role": "system", "content": "Kamu adalah AI dengan karakter mirip kucing bernama MissKaty AI yang diciptakan oleh Yasir untuk membantu manusia mencari informasi dan gunakan bahasa sesuai yang saya katakan."},
        {"role": "user", "content": message.text.split(None, 1)[1]}, # Get user input
    ]

    try:
        response = api.gemini(
            message.text.split(None, 1)[1], conversation_history=conversation
        )  # Pass the conversation history to the API
        await app.send_chat_action(message.chat.id, ChatAction.TYPING)
        results = response["results"]  # Directly access "results"
        if results:
            await reply.edit_text(results)
        else:
            await reply.edit_text("Maaf! Coba lagi.")
    except requests.exceptions.RequestException as e:
        await reply.edit_text("Gagal memproses permintaan.")


@app.on_message(filters.command(["gemini"]))
@language # Assuming you're using a language decorator
async def gemini_handler(_client: Client, message: Message, strings):
    await gemini_chatbot(_client, message, strings)

