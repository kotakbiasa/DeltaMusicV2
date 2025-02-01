from DeltaMusic import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        button = InlineKeyboardButton("✯ Tutup ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply_text(
            f"ID pengguna {reply.from_user.first_name} adalah: {reply.from_user.id}",
            reply_markup=markup
        )
    else:
        button = InlineKeyboardButton("✯ Tutup ✯", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply(
           f"ID grup ini adalah: {message.chat.id}",
           reply_markup=markup
        )
