import requests
from DeltaMusic import app
from config import BANNED_USERS
from pyrogram import filters, Client
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaAnimation,
    Message,
)

close_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="🔄 Perbarui", callback_data="refresh_dog")],
        [InlineKeyboardButton(text="❌ Tutup", callback_data="close")],
    ]
)


@app.on_message(filters.command(["fox"]) & ~BANNED_USERS)
async def dog(_client: Client, message: Message):
    r = requests.get("https://randomfox.ca/floof")
    if r.status_code == 200:
        data = r.json()
        dog_url = data["url"]
        if dog_url.endswith(".gif"):
            await message.reply_animation(dog_url, reply_markup=close_keyboard)
        else:
            await message.reply_photo(dog_url, reply_markup=close_keyboard)
    else:
        await message.reply_text("🦊 Gagal mencari foto rubah!")


@app.on_callback_query(filters.regex("refresh_dog") & ~BANNED_USERS)
async def refresh_dog(_client: Client, callback_query: CallbackQuery):
    try:
        r = requests.get("https://randomfox.ca/floof", timeout=10)  # Add timeout for robustness
        r.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = r.json()
        dog_url = data["url"]  # Access "url" directly

        if dog_url.endswith(".mp4"): # Check if it's an mp4, since random.dog sometimes returns videos
            await callback_query.edit_message_media(InputMediaVideo(media=dog_url), reply_markup=close_keyboard)
        elif dog_url.endswith(".gif"):
            await callback_query.edit_message_media(InputMediaAnimation(media=dog_url), reply_markup=close_keyboard)
        else:
            await callback_query.edit_message_media(InputMediaPhoto(media=dog_url), reply_markup=close_keyboard)

    except requests.exceptions.RequestException as e:
        await callback_query.edit_message_text(f"🦊 Gagal mencari foto rubah! Error: {e}")
    except KeyError as e:  # Handle potential KeyError if 'url' is missing
        await callback_query.edit_message_text(f"🦊 Gagal mencari foto rubah! Data tak valid: {e}")

