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
        [InlineKeyboardButton(text="🔄 Perbarui", callback_data="refresh_cat")],
        [InlineKeyboardButton(text="❌ Tutup", callback_data="close")],
    ]
)


@app.on_message(filters.command("cat") & ~BANNED_USERS)
async def cat(_client: Client, message: Message):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.status_code == 200:
        data = r.json()
        cat_url = data[0]["url"]
        if cat_url.endswith(".gif"):
            await message.reply_animation(
                cat_url, caption="🐱 Miaw", reply_markup=close_keyboard
            )
        else:
            await message.reply_photo(cat_url, caption="🐱 Miaw", reply_markup=close_keyboard)
    else:
        await message.reply_text("🙀 Gagal mencari foto kucing!")


@app.on_callback_query(filters.regex("refresh_cat") & ~BANNED_USERS)
async def refresh_cat(_client: Client, callback_query: CallbackQuery):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.status_code == 200:
        data = r.json()
        cat_url = data[0]["url"]
        if cat_url.endswith(".gif"):
            await callback_query.edit_message_media(
                InputMediaAnimation(media=cat_url, caption="🐱 Miaw"),
                reply_markup=close_keyboard,
            )
        else:
            await callback_query.edit_message_media(
                InputMediaPhoto(media=cat_url, caption="🐱 Miaw"),
                reply_markup=close_keyboard,
            )
    else:
        await callback_query.edit_message_text("🙀 Gagal mencari foto kucing!")