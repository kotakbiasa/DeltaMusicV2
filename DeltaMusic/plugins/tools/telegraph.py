import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DeltaMusic import app
import requests


def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"Error: {response.status_code} - {response.text}"


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Silakan balas pesan media untuk mengunggah ke Telegraph"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("Silakan berikan file media di bawah 200MB.")

    try:
        text = await message.reply("Sedang memproses...")

        async def progress(current, total):
            try:
                await text.edit_text(f"📥 Mengunduh... {current * 100 / total:.1f}%")
            except Exception:
                pass

        try:
            local_path = await media.download(progress=progress)
            await text.edit_text("📤 Mengunggah ke Telegraph...")

            success, upload_path = upload_file(local_path)

            if success:
                await text.edit_text(
                    f"🌐 | [Tautan Unggahan]({upload_path})",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "File Unggahan",
                                    url=upload_path,
                                )
                            ]
                        ]
                    ),
                )
            else:
                await text.edit_text(
                    f"Terjadi kesalahan saat mengunggah file Anda\n{upload_path}"
                )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await text.edit_text(f"❌ Gagal mengunggah file\n\n<i>Alasan: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass


__HELP__ = """
**Perintah Bot Unggahan Telegraph**

Gunakan perintah ini untuk mengunggah media ke Telegraph:

- `/tgm`: Unggah media yang dibalas ke Telegraph.
- `/tgt`: Sama seperti `/tgm`.
- `/telegraph`: Sama seperti `/tgm`.
- `/tl`: Sama seperti `/tgm`.

**Contoh:**
- Balas foto atau video dengan `/tgm` untuk mengunggahnya.

**Catatan:**
Anda harus membalas file media agar unggahan berfungsi.
"""

__MODULE__ = "Telegraph"
