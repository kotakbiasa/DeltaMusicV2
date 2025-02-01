import io

from gtts import gTTS
from pyrogram import filters

from DeltaMusic import app

@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "Silakan berikan beberapa teks untuk diubah menjadi suara."
        )

    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang="id")
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    audio_file = io.BytesIO(audio_data.read())
    audio_file.name = "audio.mp3"
    await message.reply_audio(audio_file)

__HELP__ = """
**Perintah Bot Teks ke Suara**

Gunakan perintah `/tts` untuk mengubah teks menjadi suara.

- `/tts <teks>`: Mengubah teks yang diberikan menjadi suara dalam bahasa Indonesia.

**Contoh:**
- `/tts Halo Dunia`

**Catatan:**
Pastikan untuk memberikan beberapa teks setelah perintah `/tts`.
"""

__MODULE__ = "TTS"
