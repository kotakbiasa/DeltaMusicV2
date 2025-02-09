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

# Available SFW categories (you can add more if the API supports them)
sfw_categories = [
    "awoo", "bite", "blush", "bonk", "bully", "cringe", "cry", "cuddle",
    "dance", "glomp", "hanhold", "happy", "highfive", "hug", "kick",
    "kill", "kiss", "lick", "megumin", "neko", "nom", "pat", "poke",
    "shinubo", "slap", "smile", "smug", "waifu", "wave", "wink", "yeet"
]

close_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="🔄 Perbarui", callback_data="refresh_anime")],
        [InlineKeyboardButton(text="❌ Tutup", callback_data="close")],
    ]
)


@app.on_message(filters.command("sfw") & ~BANNED_USERS)
async def anime(_client: Client, message: Message):
    category = message.command[1] if len(message.command) > 1 else "waifu" # Default to "waifu"
    if category not in sfw_categories:
        available_categories = ", ".join(sfw_categories)
        return await message.reply_text(f"Kategori tidak valid. Kategori yang tersedia: {available_categories}")

    try:
        r = requests.get(f"https://api.safone.co/anime/sfw/{category}", timeout=10)
        r.raise_for_status()
        data = r.json()
        anime_url = data["url"]

        if anime_url.endswith((".gif", ".mp4")):
            await message.reply_animation(anime_url, reply_markup=close_keyboard)
        else:
            await message.reply_photo(anime_url, reply_markup=close_keyboard)

    except requests.exceptions.RequestException as e:
        await message.reply_text(f"🌸 Gagal mendapatkan gambar anime! Error: {e}")
    except KeyError as e:
        await message.reply_text(f"🌸 Gagal mendapatkan gambar anime! Data tidak valid: {e}")


@app.on_callback_query(filters.regex("refresh_anime") & ~BANNED_USERS)
async def refresh_anime(_client: Client, callback_query: CallbackQuery):
    original_message = callback_query.message.reply_to_message  # Get the original message

    category = original_message.command[1] if len(original_message.command) > 1 else "waifu"
    if category not in sfw_categories:
        available_categories = ", ".join(sfw_categories)
        return await callback_query.answer(f"Kategori tidak valid. Kategori yang tersedia: {available_categories}", show_alert=True)


    try:
        r = requests.get(f"https://api.safone.co/anime/sfw/{category}", timeout=10)  # Use category from original message
        r.raise_for_status()
        data = r.json()
        anime_url = data["url"]

        if anime_url.endswith((".gif", ".mp4")):
            await callback_query.edit_message_media(InputMediaAnimation(media=anime_url), reply_markup=close_keyboard)
        else:
            await callback_query.edit_message_media(InputMediaPhoto(media=anime_url), reply_markup=close_keyboard)

    except requests.exceptions.RequestException as e:
        await callback_query.edit_message_text(f"🌸 Gagal mendapatkan gambar anime! Error: {e}")
    except KeyError as e:
        await callback_query.edit_message_text(f"🌸 Gagal mendapatkan gambar anime! Data tidak valid: {e}")

