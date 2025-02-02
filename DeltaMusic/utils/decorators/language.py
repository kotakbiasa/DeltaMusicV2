from strings import get_string
from DeltaMusic.misc import SUDOERS
from DeltaMusic.utils.database import get_lang, is_maintenance
from pyrogram.errors import FloodWait
import asyncio


def language(mystic):
    async def wrapper(_, message, **kwargs):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} sedang dalam pemeliharaan, kunjungi <a href={SUPPORT_CHAT}>obrolan dukungan</a> untuk mengetahui alasannya.",
                    disable_web_page_preview=True,
                )
        try:
            await message.delete()
        except:
            pass

        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await wrapper_with_retry(_, message, language)

    async def wrapper_with_retry(_, message, language):
        try:
            return await mystic(_, message, language)
        except FloodWait as e:
            print(f"Flood wait of {e.x} seconds required")
            await asyncio.sleep(e.x)
            return await wrapper_with_retry(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    f"{app.mention} sedang dalam pemeliharaan, kunjungi obrolan dukungan untuk mengetahui alasannya.",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await wrapper_with_retry(_, CallbackQuery, language)

    async def wrapper_with_retry(_, CallbackQuery, language):
        try:
            return await mystic(_, CallbackQuery, language)
        except FloodWait as e:
            print(f"Flood wait of {e.x} seconds required")
            await asyncio.sleep(e.x)
            return await wrapper_with_retry(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await wrapper_with_retry(_, message, language)

    async def wrapper_with_retry(_, message, language):
        try:
            return await mystic(_, message, language)
        except FloodWait as e:
            print(f"Flood wait of {e.x} seconds required")
            await asyncio.sleep(e.x)
            return await wrapper_with_retry(_, message, language)

    return wrapper
