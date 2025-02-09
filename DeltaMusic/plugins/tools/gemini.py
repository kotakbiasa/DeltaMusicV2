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
        safone_api = SafoneAPI()  # Initialize SafoneAPI

        if user_id not in gemini_conversations:
            # Start a new conversation
            initial_prompt = "Kamu adalah AI dengan karakter mirip Anime bernama Delta yang diciptakan oleh Kotak Biasa untuk membantu manusia mencari informasi dan gunakan bahasa sesuai yang saya katakan."
            gemini_conversations[user_id] = [] # Start with an empty list

        # Build the dialog messages list of dictionaries
        dialog_messages = []
        for i in range(0, len(gemini_conversations[user_id]), 2):
            try:
                dialog_messages.append({"user": gemini_conversations[user_id][i]["content"], "bot": gemini_conversations[user_id][i+1]["content"]})
            except IndexError:
                 dialog_messages.append({"user": gemini_conversations[user_id][i]["content"], "bot": ""}) # Handle cases where bot hasn't replied yet

        # Add the current user input
        dialog_messages.append({"user": user_input, "bot": ""})

        # Make the API call using the correct payload structure
        payload = {
            "message": user_input,
            "chat_mode": "assistant",  # Or the appropriate mode
            "dialog_messages": dialog_messages # Pass the structured data
        }
        response = await safone_api.gemini(payload)

        if response and "response" in response:
            ai_response = response["response"]
            await msg.edit_text(ai_response, quote=True)

            # Store the conversation history correctly
            gemini_conversations[user_id].append({"role": "user", "content": user_input})
            gemini_conversations[user_id].append({"role": "assistant", "content": ai_response})
        else:
            await msg.edit_text("Maaf! Coba lagi. API mungkin mengembalikan data yang tidak valid.")
            if user_id in gemini_conversations: # Check if the key exists before trying to pop
                gemini_conversations[user_id].pop()
                if not gemini_conversations[user_id]:
                    del gemini_conversations[user_id]

    except requests.exceptions.RequestException as e:
        await msg.edit_text(f"Gagal memproses permintaan: {e}")
        gemini_conversations.pop(user_id, None) 
    except Exception as e:
        await msg.edit_text(f"Terjadi kesalahan yang tidak terduga: {e}")
        gemini_conversations.pop(user_id, None)
