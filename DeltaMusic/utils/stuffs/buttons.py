from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("ChatGPT", callback_data="mplus HELP_ChatGPT"),
            InlineKeyboardButton("Riwayat", callback_data="mplus HELP_History"),
            InlineKeyboardButton("Reel", callback_data="mplus HELP_Reel")
        ],
        [
            InlineKeyboardButton("Tag Semua", callback_data="mplus HELP_TagAll"),
            InlineKeyboardButton("Info", callback_data="mplus HELP_Info"),
            InlineKeyboardButton("Ekstra", callback_data="mplus HELP_Extra")
        ],
        [
            InlineKeyboardButton("Pasangan", callback_data="mplus HELP_Couples"),
            InlineKeyboardButton("Aksi", callback_data="mplus HELP_Action"),
            InlineKeyboardButton("Cari", callback_data="mplus HELP_Search")
        ],
        [
            InlineKeyboardButton("Font", callback_data="mplus HELP_Font"),
            InlineKeyboardButton("Bot", callback_data="mplus HELP_Bots"),
            InlineKeyboardButton("T-Graph", callback_data="mplus HELP_TG")
        ],
        [
            InlineKeyboardButton("Sumber", callback_data="mplus HELP_Source"),
            InlineKeyboardButton("Truth-Dare", callback_data="mplus HELP_TD"),
            InlineKeyboardButton("Kuis", callback_data="mplus HELP_Quiz")
        ],
        [
            InlineKeyboardButton("TTS", callback_data="mplus HELP_TTS"),
            InlineKeyboardButton("Radio", callback_data="mplus HELP_Radio"),
            InlineKeyboardButton("Quotly", callback_data="mplus HELP_Q")
        ],
        [
            InlineKeyboardButton("◁", callback_data="settings_back_helper"),
            InlineKeyboardButton("↻ Kembali ↻", callback_data="mbot_cb"),
            InlineKeyboardButton("▷", callback_data="managebot123 settings_back_helper"),
        ]
    ]
