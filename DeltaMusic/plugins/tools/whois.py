from DeltaMusic import app
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User


def cek_balasan(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


teks_info = (
    "[{full_name}](tg://user?id={user_id})\n\n"
    " ➻ ID Pengguna: `{user_id}`\n"
    " ➻ Nama Depan: `{first_name}`\n"
    " ➻ Nama Belakang: `{last_name}`\n"
    " ➻ Nama Pengguna: `@{username}`\n"
    " ➻ Terakhir kali online: `{last_online}`"
)


def last_online(user: User):
    if user.is_bot:
        return ""
    elif user.status == "recently":
        return "baru saja"
    elif user.status == "within_week":
        return "dalam minggu ini"
    elif user.status == "within_month":
        return "dalam bulan ini"
    elif user.status == "long_time_ago":
        return "sudah lama sekali :("
    elif user.status == "online":
        return "sedang online"
    elif user.status == "offline":
        return datetime.fromtimestamp(user.status.date).strftime(
            "%a, %d %b %Y, %H:%M:%S"
        )


def full_name(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


@app.on_message(filters.command("whois"))
async def whois(client, message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await message.reply("Tidak mengenal pengguna ini.")
        return
        desc = await client.get_chat(get_user)
        desc = desc.description
    await message.reply_text(
        infotext.format(
            full_name=full_name(user),
            user_id=user.id,
            user_dc=user.dc_id,
            first_name=user.first_name,
            last_name=user.last_name if user.last_name else "",
            username=user.username if user.username else "",
            last_online=last_online(user),
            bio=desc if desc else "Kosong.",
        ),
        disable_web_page_preview=True,
    )


__MODULE__ = "🆔 Info"
__HELP__ = """
**Perintah:**

• /whois - **Memeriksa informasi pengguna.**

**Informasi:**

- Bot ini menyediakan perintah untuk memeriksa informasi pengguna.
- Gunakan perintah /whois diikuti dengan membalas pesan atau User ID untuk mendapatkan informasi pengguna.

**Catatan:**

- Perintah /whois dapat digunakan untuk mengembalikan informasi tentang pengguna di chat.
- Informasi termasuk ID, Nama Depan, Nama Belakang, Username, dan status online.
"""