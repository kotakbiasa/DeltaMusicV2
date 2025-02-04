import asyncio

from pyrogram import Client, errors, filters
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.errors import MessageDeleteForbidden

import config

from ..logging import LOGGER

data = {}

async def task(msg, warn=False, sec=None):
    if warn:
        user = msg.from_user or msg.sender_chat
        ids = await msg.reply(
            f"Maaf {user.mention if msg.from_user else msg.sender_chat.title} [<code>{user.id}</code>], Anda harus menunggu selama {sec} detik sebelum menggunakan fitur ini lagi.."
        )
        try:
            await msg.delete()
        except MessageDeleteForbidden:
            pass
        await asyncio.sleep(sec)
        await ids.edit(
            f"Baiklah {user.mention if msg.from_user else msg.sender_chat.title} [<code>{user.id}</code>], waktu tunggu Anda telah berakhir, Anda dapat menggunakan perintah lagi.",
            del_in=3,
        )

def wait(sec):
    async def ___(flt, _, msg):
        user_id = msg.from_user.id if msg.from_user else msg.sender_chat.id
        if user_id in config.SUDO or user_id == config.OWNER_ID:
            return True
        if user_id in data:
            if msg.date.timestamp() >= data[user_id]["timestamp"] + flt.data:
                data[user_id] = {"timestamp": msg.date.timestamp(), "warned": False}
                return True
            else:
                if not data[user_id]["warned"]:
                    data[user_id]["warned"] = True
                    asyncio.ensure_future(
                        task(msg, True, flt.data)
                    )  # for super accuracy use (future - time.time())
                    return False  # cause we dont need delete again

                asyncio.ensure_future(task(msg))
                return False
        else:
            data.update({user_id: {"timestamp": msg.date.timestamp(), "warned": False}})
            return True

    return filters.create(___, data=sec)

class Hotty(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Memulai Bot...")
        super().__init__(
            name="DeltaMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} Bot dimulai :</b><u>\n\nID : <code>{self.id}</code>\nNama : {self.name}\nUsername : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot gagal mengakses grup/saluran log. Pastikan Anda telah menambahkan bot Anda ke grup/saluran log Anda."
            )

        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot gagal mengakses grup/saluran log.\n  Alasan : {type(ex).__name__}."
            )

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Silakan promosikan bot Anda sebagai admin di grup/saluran log Anda."
            )

        LOGGER(__name__).info(f"Bot Musik Dimulai sebagai {self.name}")

    async def stop(self):
        await super().stop()
