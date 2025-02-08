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
        [InlineKeyboardButton(text="🔄 Perbarui", callback_data="refresh_fox")],
        [InlineKeyboardButton(text="❌ Tutup", callback_data="close")],
    ]
)


@app.on_message(filters.command(["fox"]) & ~BANNED_USERS)
async def fox(_client: Client, message: Message):
    try:
        r = requests.get("https://randomfox.ca/floof/", timeout=10)
        r.raise_for_status()
        data = r.json()
        fox_url = data["image"] # Extract image URL

        if fox_url.endswith((".gif", ".mp4")):  # Check for both GIF and MP4
            await message.reply_animation(fox_url, reply_markup=close_keyboard)
        else:
            await message.reply_photo(fox_url, reply_markup=close_keyboard)

    except requests.exceptions.RequestException as e:
        await message.reply_text(f"🦊 Gagal mencari foto rubah! Error: {e}")
    except KeyError as e:
        await message.reply_text(f"🦊 Gagal mencari foto rubah! Data tak valid: {e}")




@app.on_callback_query(filters.regex("refresh_fox") & ~BANNED_USERS)
async def refresh_fox(_client: Client, callback_query: CallbackQuery):
    try:
        r = requests.get("https://randomfox.ca/floof/", timeout=10)
        r.raise_for_status()
        data = r.json()
        fox_url = data["image"] # Extract image URL

        if fox_url.endswith((".gif", ".mp4")):  # Check for both GIF and MP4
            await callback_query.edit_message_media(InputMediaAnimation(media=fox_url), reply_markup=close_keyboard)
        else:
            await callback_query.edit_message_media(InputMediaPhoto(media=fox_url), reply_markup=close_keyboard)

    except requests.exceptions.RequestException as e:
        await callback_query.edit_message_text(f"🦊 Gagal mencari foto rubah! Error: {e}")
    except KeyError as e:
        await callback_query.edit_message_text(f"🦊 Gagal mencari foto rubah! Data tak valid: {e}")

