from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


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