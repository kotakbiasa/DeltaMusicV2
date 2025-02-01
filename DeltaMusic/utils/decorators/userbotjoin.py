import asyncio

from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from DeltaMusic import YouTube, app
from DeltaMusic.misc import SUDOERS
from DeltaMusic.utils.database import (
    get_assistant,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
    is_active_chat,
    is_maintenance,
)
from DeltaMusic.utils.inline import botplaylist_markup
from config import PLAYLIST_IMG_URL, SUPPORT_CHAT, adminlist
from strings import get_string

links = {}


def UserbotWrapper(command):
    async def wrapper(client, message):
        language = await get_lang(message.chat.id)
        _ = get_string(language)

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

        chat_id = message.chat.id

        if not await is_active_chat(chat_id):
            userbot = await get_assistant(chat_id)
            try:
                try:
                    get = await app.get_chat_member(chat_id, userbot.id)
                except ChatAdminRequired:
                    return await message.reply_text(
                        "➥ Tolong jadikan saya admin dan berikan izin mengundang pengguna untuk mengundang asisten saya ke obrolan ini."
                    )
                if (
                    get.status == ChatMemberStatus.BANNED
                    or get.status == ChatMemberStatus.RESTRICTED
                ):
                    return await message.reply_text(
                        _["call_2"].format(
                            app.mention, userbot.id, userbot.name, userbot.username
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text="Unban Asisten",
                                        callback_data=f"unban_assistant",
                                    )
                                ]
                            ]
                        ),
                    )
            except UserNotParticipant:
                if message.chat.username:
                    invitelink = message.chat.username
                    await userbot.join_chat(invitelink)
                else:
                    if chat_id in links:
                        invitelink = links[chat_id]
                        try:
                            await userbot.resolve_peer(invitelink)
                        except:
                            pass
                    else:
                        try:
                            invitelink = await app.export_chat_invite_link(chat_id)
                        except ChatAdminRequired:
                            return await message.reply_text(
                                "➥ Tolong jadikan saya admin dan berikan izin mengundang pengguna untuk mengundang asisten saya ke obrolan ini."
                            )
                        except Exception as e:
                            return await message.reply_text(
                                f"{app.mention} Asisten berhasil bergabung dengan grup ini.\n\nID: {userbot.mention}."
                            )

                if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+", "https://t.me/joinchat/"
                    )
                myu = await message.reply_text("Asisten sedang bergabung dengan obrolan ini...")
                try:
                    await asyncio.sleep(1)
                    await userbot.join_chat(invitelink)
                    await myu.delete()
                    await message.reply_text(
                        f"{app.mention} Asisten berhasil bergabung dengan grup ini.\n\nID: **@{userbot.username}**"
                    )
                except InviteRequestSent:
                    try:
                        await app.approve_chat_join_request(chat_id, userbot.id)
                    except Exception as e:
                        return await message.reply_text(
                            _["call_3"].format(app.mention, type(e).__name__)
                        )
                    await asyncio.sleep(3)
                    await myu.delete()
                    await message.reply_text(
                        f"{app.mention} Asisten berhasil bergabung dengan grup ini.\n\nID: **@{userbot.username}**"
                    )
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    return await message.reply_text(
                        f"{app.mention} Asisten berhasil bergabung dengan grup ini.\n\nID: **@{userbot.username}**"
                    )

                links[chat_id] = invitelink

                try:
                    await userbot.resolve_peer(chat_id)
                except:
                    pass

        return await command(client, message, _, chat_id)

    return wrapper
