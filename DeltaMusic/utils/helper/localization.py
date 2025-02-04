import inspect
import os.path
from functools import partial, wraps

from pyrogram.enums import ChatType
from pyrogram.types import CallbackQuery, ChatMemberUpdated, InlineQuery, Message

from database.locale_db import get_db_lang

enabled_locales = [
    "en-US",  # English (United States)
    "id-ID",  # Indonesian
    "id-JW",  # Javanese
    "ru-RU",  # Russian
]

default_language = "en-US"

def use_chat_lang(context: str = None):
    if not context:
        cwd = os.getcwd()
        frame = inspect.stack()[1]

        fname = frame.filename

        if fname.startswith(cwd):
            fname = fname[len(cwd) + 1 :]
        context = fname.split(os.path.sep)[2].split(".")[0]

    def decorator(func):
        @wraps(func)
        async def wrapper(client, message):
            lang = await get_lang(message)

            dic = langdict.get(lang, langdict[default_language])

            lfunc = partial(get_locale_string, dic.get(context, {}), lang, context)
            return await func(client, message, lfunc)

        return wrapper

    return decorator