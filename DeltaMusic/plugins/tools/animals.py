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


@app.on_message(filters.command("cat", "kucing") & ~BANNED_USERS)
async def cat(_client: Client, message: Message):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.status_code == 200:
        data = r.json()
        cat_url = data[0]["url"]
        if cat_url.endswith(".gif"):
            await message.reply_animation(
                cat_url, caption="🐱 **𝗠𝗲𝗼𝘄**", reply_markup=close_keyboard
            )
        else:
            await message.reply_photo(cat_url, caption="🐱 **𝗠𝗲𝗼𝘄**", reply_markup=close_keyboard)
    else:
        await message.reply_text("🙀 **Gagal mencari foto kucing!**")

@app.on_message(filters.command(["dogs", "dog", "anjing"]) & ~BANNED_USERS)
async def dog(_client: Client, message: Message):
    r = requests.get("https://random.dog/woof.json")
    if r.status_code == 200:
        data = r.json()
        dog_url = data["url"]
        if dog_url.endswith(".gif"):
            await message.reply_animation(dog_url, reply_markup=close_keyboard)
        else:
            await message.reply_photo(dog_url, reply_markup=close_keyboard)
    else:
        await message.reply_text("🐕 **Gagal mencari foto anjing!**")

@app.on_callback_query(filters.regex("refresh_cat") & ~BANNED_USERS)
async def refresh_cat(_client: Client, callback_query: CallbackQuery):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.status_code == 200:
        data = r.json()
        cat_url = data[0]["url"]
        if cat_url.endswith(".gif"):
            await callback_query.edit_message_media(
                InputMediaAnimation(media=cat_url, caption="🐱 **𝗠𝗲𝗼𝘄**"),
                reply_markup=close_keyboard,
            )
        else:
            await callback_query.edit_message_media(
                InputMediaPhoto(media=cat_url, caption="🐱 **𝗠𝗲𝗼𝘄**"),
                reply_markup=close_keyboard,
            )
    else:
        await callback_query.edit_message_text("🙀 **Gagal mencari foto kucing!**")

@app.on_callback_query(filters.regex("refresh_dog") & ~BANNED_USERS)
async def refresh_dog(_client: Client, callback_query: CallbackQuery):
    r = requests.get("https://random.dog/woof.json")
    if r.status_code == 200:
        data = r.json()
        dog_url = data[0]["url"]
        if dog_url.endswith(".gif"):
            await callback_query.edit_message_media(
                InputMediaAnimation(media=dog_url),
                reply_markup=close_keyboard,
            )
        else:
            await callback_query.edit_message_media(
                InputMediaPhoto(media=dog_url),
                reply_markup=close_keyboard,
            )
    else:
        await callback_query.edit_message_text(
            "🐕 **Gagal mencari foto anjing!**")