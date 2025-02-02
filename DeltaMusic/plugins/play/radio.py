import logging

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import Message, InlineQueryResultArticle, InputTextMessageContent

from config import BANNED_USERS, adminlist
from strings import get_string
from DeltaMusic import app
from DeltaMusic.misc import SUDOERS
from DeltaMusic.utils.database import (
    get_assistant,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
)
from DeltaMusic.utils.logger import play_logs
from DeltaMusic.utils.stream.stream import stream

RADIO_STATION = {
    "The Rockin Life": "https://n10.radiojar.com/7csmg90fuqruv?rj-ttl=5&rj-tok=AAABlLLRtm0A79_IvCfOpTBeBw",
    "i-Radio": "https://n0d.radiojar.com/4ywdgup3bnzuv?rj-ttl=5&rj-tok=AAABlLLWuAUAXZtQLiTbz29MeA",
    "Radio Elshinta": "https://stream-ssl.arenastreaming.com:8000/jakarta.m3u",
    "90.4 FM": "https://stream.radiojar.com/u7d8heq3bnzuv",
    "OZ Radio": "https://streaming.ozradiojakarta.com:8443/ozjakarta",
    "Radio Sonora": "https://streaming.brol.tech/rtfmlounge",
    "Hot 93.2 FM": "https://wz.mari.co.id:1936/web_hotfm/hotfm/playlist.m3u8",
    "KISI FM": "http://live.serverstreaming.net:9340/kisifm",
    "Smart FM": "https://streaming.brol.tech/rtfmlounge",
}

valid_stations = "\n".join([f"`{name}`" for name in sorted(RADIO_STATION.keys())])

TV_STATION = {
    "Trans 7": "https://video.detik.com/trans7/smil:trans7.smil/index.m3u8",
    "TransTV": "https://video.detik.com/transtv/smil:transtv.smil/index.m3u8",
    "CNBC Indonesia": "https://live.cnbcindonesia.com/livecnbc/smil:cnbctv.smil/master.m3u8",
    "KompasTV": "http://op-group1-swiftservehd-1.dens.tv/h/h234/01.m3u8",
    "One Piece": "http://cfd-v4-service-channel-stitcher-use1-1.prd.pluto.tv/stitch/hls/channel/5f7790b3ed0c88000720b241/master.m3u8?appName=web&appVersion=unknown&clientTime=0&deviceDNT=0&deviceId=6c2a7816-30d3-11ef-9cf5-e9ddff8ff496&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&serverSideAds=false&sid=4b38ba42-6f97-4a17-b657-1277978d366c",
    "CNN Indonesia": "https://live.cnnindonesia.com/livecnn/smil:cnntv.smil/master.m3u8",
    "Indosiar": "http://op-group1-swiftservehd-1.dens.tv/h/h207/02.m3u8",
    "ANTV": "http://op-group1-swiftservehd-1.dens.tv/h/h235/02.m3u8",
    "MDTV": "http://op-group1-swiftservehd-1.dens.tv/h/h223/02.m3u8",
}

valid_tv_stations = "\n".join([f"`{name}`" for name in sorted(TV_STATION.keys())])


@app.on_message(
    filters.command(["radioplayforce", "radio", "cradio"])
    & filters.group
    & ~BANNED_USERS
    | filters.InlineQuery
)
async def radio(client, message: Message):
    msg = await message.reply_text("Tunggu sebentar....")
    try:
        try:
            userbot = await get_assistant(message.chat.id)
            get = await app.get_chat_member(message.chat.id, userbot.id)
        except ChatAdminRequired:
            return await msg.edit_text(
                f"Saya tidak memiliki izin untuk mengundang pengguna melalui tautan untuk mengundang {userbot.mention} asisten ke {message.chat.title}."
            )
        if get.status == ChatMemberStatus.BANNED:
            return await msg.edit_text(
                text=f"{userbot.mention} asisten diblokir di {message.chat.title}\n\n𖢵 ID : `{userbot.id}`\n𖢵 Nama : {userbot.mention}\n𖢵 Username : @{userbot.username}\n\nSilakan buka blokir asisten dan coba lagi...",
            )
    except UserNotParticipant:
        if message.chat.username:
            invitelink = message.chat.username
            try:
                await userbot.resolve_peer(invitelink)
            except Exception as ex:
                logging.exception(ex)
        else:
            try:
                invitelink = await client.export_chat_invite_link(message.chat.id)
            except ChatAdminRequired:
                return await msg.edit_text(
                    f"Saya tidak memiliki izin untuk mengundang pengguna melalui tautan untuk mengundang {userbot.mention} asisten ke {message.chat.title}."
                )
            except InviteRequestSent:
                try:
                    await app.approve_chat_join_request(message.chat.id, userbot.id)
                except Exception as e:
                    return await msg.edit(
                        f"Gagal mengundang {userbot.mention} asisten ke {message.chat.title}.\n\n**Alasan :** `{ex}`"
                    )
            except Exception as ex:
                if "channels.JoinChannel" in str(ex) or "Username not found" in str(ex):
                    return await msg.edit_text(
                        f"Saya tidak memiliki izin untuk mengundang pengguna melalui tautan untuk mengundang {userbot.mention} asisten ke {message.chat.title}."
                    )
                else:
                    return await msg.edit_text(
                        f"Gagal mengundang {userbot.mention} asisten ke {message.chat.title}.\n\n**Alasan :** `{ex}`"
                    )
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
        anon = await msg.edit_text(
            f"Tunggu sebentar...\n\nMengundang {userbot.mention} ke {message.chat.title}."
        )
        try:
            await userbot.join_chat(invitelink)
            await asyncio.sleep(2)
            await msg.edit_text(
                f"{userbot.mention} berhasil bergabung,\n\nmemulai streaming..."
            )
        except UserAlreadyParticipant:
            pass
        except InviteRequestSent:
            try:
                await app.approve_chat_join_request(message.chat.id, userbot.id)
            except Exception as e:
                return await msg.edit(
                    f"Gagal mengundang {userbot.mention} asisten ke {message.chat.title}.\n\n**Alasan :** `{ex}`"
                )
        except Exception as ex:
            if "channels.JoinChannel" in str(ex) or "Username not found" in str(ex):
                return await msg.edit_text(
                    f"Saya tidak memiliki izin untuk mengundang pengguna melalui tautan untuk mengundang {userbot.mention} asisten ke {message.chat.title}."
                )
            else:
                return await msg.edit_text(
                    f"Gagal mengundang {userbot.mention} asisten ke {message.chat.title}.\n\n**Alasan :** `{ex}`"
                )

        try:
            await userbot.resolve_peer(invitelink)
        except:
            pass
    await msg.delete()
    station_name = " ".join(message.command[1:])
    RADIO_URL = RADIO_STATION.get(station_name)
    if RADIO_URL:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_12"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None

        video = None
        mystic = await message.reply_text(
            _["play_2"].format(channel) if channel else _["play_1"]
        )
        try:
            await stream(
                _,
                mystic,
                message.from_user.id,
                RADIO_URL,
                chat_id,
                message.from_user.mention,
                message.chat.id,
                video=video,
                streamtype="index",
            )
        except Exception as e:
            ex_type = type(e).__name__
            err = e if ex_type == "AssistantErr" else _["general_3"].format(ex_type)
            return await mystic.edit_text(err)
        return await play_logs(message, streamtype="M3u8 atau Index Link")
    else:
        await message.reply(
            f"Berikan saya nama stasiun untuk memutar radio\nBerikut adalah beberapa nama stasiun:\n{valid_stations}"
        )


@app.on_message(
    filters.command(["tvplayforce", "tv", "ctv"])
    & filters.group
    & ~BANNED_USERS
    | filters.InlineQuery
)
async def tv(client, message: Message):
    msg = await message.reply_text("Tunggu sebentar....")
    try:
        try:
            userbot = await get_assistant(message.chat.id)
            get = await app.get_chat_member(message.chat.id, userbot.id)
        except ChatAdminRequired:
            return await msg.edit_text(
                f"Saya tidak memiliki izin untuk mengundang pengguna melalui tautan untuk mengundang {userbot.mention} asisten ke {message.chat.title}."
            )
        if get.status == ChatMemberStatus.BANNED:
            return await msg.edit_text(
                text=f"{userbot.mention} asisten diblokir di {message.chat.title}\n\n𖢵 ID : `{userbot.id}`\n𖢵 Nama : {userbot.mention}\n𖢵 Username : @{userbot.username}\n\nSilakan buka blokir asisten dan coba lagi...",
            )
    except UserNotParticipant:
        if message.chat.username:
            invitelink = message.chat.username
            try:
                await userbot.resolve_peer(invitelink)
            except Exception as ex:
                logging.exception(ex)
        else:
            try:
                invitelink = await client.export_chat_invite_link(message.chat.id)
            except ChatAdminRequired:
                return await msg.edit_text(
                    f"Saya tidak memiliki izin untuk mengundang pengguna melalui tautan untuk mengundang {userbot.mention} asisten ke {message.chat.title}."
                )
            except InviteRequestSent:
                try:
                    await app.approve_chat_join_request(message.chat.id, userbot.id)
                except Exception as e:
                    return await msg.edit(
                        f"Gagal mengundang {userbot.mention} asisten ke {message.chat.title}.\n\n**Alasan :** `{ex}`"
                    )
            except Exception as ex:
                if "channels.JoinChannel" in str(ex) or "Username not found" in str(ex):
                    return await msg.edit_text(
                        f"Saya tidak memiliki izin untuk mengundang pengguna melalui tautan untuk mengundang {userbot.mention} asisten ke {message.chat.title}."
                    )
                else:
                    return await msg.edit_text(
                        f"Gagal mengundang {userbot.mention} asisten ke {message.chat.title}.\n\n**Alasan :** `{ex}`"
                    )
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
        anon = await msg.edit_text(
            f"Tunggu sebentar...\n\nMengundang {userbot.mention} ke {message.chat.title}."
        )
        try:
            await userbot.join_chat(invitelink)
            await asyncio.sleep(2)
            await msg.edit_text(
                f"{userbot.mention} berhasil bergabung,\n\nmemulai streaming..."
            )
        except UserAlreadyParticipant:
            pass
        except InviteRequestSent:
            try:
                await app.approve_chat_join_request(message.chat.id, userbot.id)
            except Exception as e:
                return await msg.edit(
                    f"Gagal mengundang {userbot.mention} asisten ke {message.chat.title}.\n\n**Alasan :** `{ex}`"
                )
        except Exception as ex:
            if "channels.JoinChannel" in str(ex) or "Username not found" in str(ex):
                return await msg.edit_text(
                    f"Saya tidak memiliki izin untuk mengundang pengguna melalui tautan untuk mengundang {userbot.mention} asisten ke {message.chat.title}."
                )
            else:
                return await msg.edit_text(
                    f"Gagal mengundang {userbot.mention} asisten ke {message.chat.title}.\n\n**Alasan :** `{ex}`"
                )

        try:
            await userbot.resolve_peer(invitelink)
        except:
            pass
    await msg.delete()
    station_name = " ".join(message.command[1:])
    TV_URL = TV_STATION.get(station_name)
    if TV_URL:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_12"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None

        video = None
        mystic = await message.reply_text(
            _["play_2"].format(channel) if channel else _["play_1"]
        )
        try:
            await stream(
                _,
                mystic,
                message.from_user.id,
                TV_URL,
                chat_id,
                message.from_user.mention,
                message.chat.id,
                video=video,
                streamtype="index",
            )
        except Exception as e:
            ex_type = type(e).__name__
            err = e if ex_type == "AssistantErr" else _["general_3"].format(ex_type)
            return await mystic.edit_text(err)
        return await play_logs(message, streamtype="M3u8 atau Index Link")
    else:
        await message.reply(
            f"Berikan saya nama stasiun untuk memutar TV\nBerikut adalah beberapa nama stasiun:\n{valid_tv_stations}"
        )


@app.on_inline_query()
async def inline_query_handler(client, inline_query):
    query = inline_query.query.lower()
    results = []

    if query.startswith("radio "):
        station_name = query.split(" ", 1)[1]
        RADIO_URL = RADIO_STATION.get(station_name)
        if RADIO_URL:
            results.append(
                InlineQueryResultArticle(
                    title=f"Play Radio: {station_name}",
                    input_message_content=InputTextMessageContent(
                        f"/radio {station_name}"
                    ),
                    description=f"Play {station_name} radio station",
                )
            )
    elif query.startswith("tv "):
        station_name = query.split(" ", 1)[1]
        TV_URL = TV_STATION.get(station_name)
        if TV_URL:
            results.append(
                InlineQueryResultArticle(
                    title=f"Play TV: {station_name}",
                    input_message_content=InputTextMessageContent(
                        f"/tv {station_name}"
                    ),
                    description=f"Play {station_name} TV station",
                )
            )

    await inline_query.answer(results, cache_time=1, is_personal=True, switch_pm_text="Close", switch_pm_parameter="close")


__MODULE__ = "Radio dan TV"
__HELP__ = f"\n/radio [nama stasiun] - untuk memutar **radio di obrolan suara**\n\nBerikut adalah beberapa nama stasiun:\n{valid_stations}\n\n/tv [nama stasiun] - untuk memutar **TV di obrolan suara**\n\nBerikut adalah beberapa nama stasiun:\n{valid_tv_stations}\n\nInline commands:\n- `@botusername radio [nama stasiun]`\n- `@botusername tv [nama stasiun]`"
