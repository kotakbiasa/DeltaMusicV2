import requests
from SafoneAPI import SafoneAPI  # Use SafoneAPI
from DeltaMusic import app
from pyrogram import filters, Client
from pyrogram.enums import ChatAction
from pyrogram.types import Message

gemini_conversations = {}  # Store conversation history

@app.on_message(filters.command(["gemini"]))
async def gemini_handler(_client: Client, message: Message):
    await app.send_chat_action(message.chat.id, ChatAction.TYPING)

    user_id = message.from_user.id if message.from_user else message.sender_chat.id

    if (
        message.text.startswith(f"/gemini@{app.username}")
        and len(message.text.split(" ", 1)) > 1
    ):
        user_input = message.text.split(" ", 1)[1]
    elif message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    elif len(message.command) > 1:
        user_input = " ".join(message.command[1:])
    else:
        await message.reply_text("Contoh: `/gemini siapa itu dewa ram`")
        return

    msg = await message.reply_text("🤔 Mencari jawaban...")

    try:
        safone_api = SafoneAPI()

        if user_id not in gemini_conversations:
            # Start a new conversation
            initial_prompt = "Kamu adalah AI dengan karakter mirip Anime bernama Delta yang diciptakan oleh Kotak Biasa untuk membantu manusia mencari informasi dan gunakan bahasa sesuai yang saya katakan."
            gemini_conversations[user_id] = [{"role": "system", "content": initial_prompt}, {"role": "user", "content": user_input}]
        else:
            # Continue existing conversation
            gemini_conversations[user_id].append({"role": "user", "content": user_input})

        response = await safone_api.gemini(gemini_conversations[user_id])  # Pass the conversation history

        if response and "response" in response:  # Check for successful response and 'response' key
            ai_response = response["response"]

            await msg.edit_text(ai_response, quote=True)
            gemini_conversations[user_id].append({"role": "assistant", "content": ai_response}) # Store bot's response

        else:
            await msg.edit_text("Maaf! Coba lagi. API mungkin mengembalikan data yang tidak valid.")

            # Remove the last user message if the API call failed
            gemini_conversations[user_id].pop()
            if not gemini_conversations[user_id]:  # If conversation is empty, remove it
                 del gemini_conversations[user_id]


    except requests.exceptions.RequestException as e:
        await msg.edit_text(f"Gagal memproses permintaan: {e}")
        gemini_conversations.pop(user_id, None) # Handle error (optional: remove the user from conversations)
    except Exception as e:  # Catch other potential exceptions
        await msg.edit_text(f"Terjadi kesalahan yang tidak terduga: {e}")
        gemini_conversations.pop(user_id, None)
