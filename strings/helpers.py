HELP_1 = """<b><u>Perintah Admin:</b></u>

Tambahkan <b>c</b> di awal perintah untuk menggunakannya di channel.

/pause : Jeda streaming yang sedang diputar.

/resume : Lanjutkan streaming yang dijeda.

/skip : Lewati streaming yang sedang diputar dan mulai streaming lagu berikutnya dalam antrean.

/end atau /stop : Hapus antrean dan akhiri streaming yang sedang diputar.

/player : Dapatkan panel pemutar interaktif.

/queue : Tampilkan daftar lagu yang antre.

/lyrics [nama lagu] : Cari lirik untuk lagu yang diminta dan kirim hasilnya.
"""

HELP_2 = """
<b><u>Pengguna Otorisasi:</b></u>

Pengguna otorisasi dapat menggunakan hak admin di bot tanpa hak admin di chat.

/auth [username/user_id] : Tambahkan pengguna ke daftar otorisasi bot.
/unauth [username/user_id] : Hapus pengguna dari daftar otorisasi.
/authusers : Tampilkan daftar pengguna otorisasi grup.
"""

HELP_3 = """
<u><b>Fitur Broadcast</b></u> [Hanya untuk pengguna sudo]:

/broadcast [pesan atau balas ke pesan] : Siarkan pesan ke chat yang dilayani oleh bot.

<u>Mode Broadcast:</u>
<b>-pin</b> : Pin pesan yang disiarkan di chat yang dilayani.
<b>-pinloud</b> : Pin pesan yang disiarkan di chat yang dilayani dan kirim notifikasi ke anggota.
<b>-user</b> : Siarkan pesan ke pengguna yang telah memulai bot Anda.
<b>-assistant</b> : Siarkan pesan dari akun asisten bot.
<b>-nobot</b> : Paksa bot untuk tidak menyiarkan pesan.

<b>Contoh:</b> <code>/broadcast -user -assistant -pin Tes Broadcast</code>
"""

HELP_4 = """<u><b>Fitur Blacklist Chat:</b></u> [Hanya untuk pengguna sudo]

Batasi chat yang tidak diinginkan untuk menggunakan bot kami.

/blacklistchat [ID chat] : Blokir chat dari menggunakan bot.
/whitelistchat [ID chat] : Hapus blokir chat.
/blacklistedchat : Tampilkan daftar chat yang diblokir.
"""

HELP_5 = """
<u><b>Blokir Pengguna:</b></u> [Hanya untuk pengguna sudo]

Mulai mengabaikan pengguna yang diblokir, sehingga mereka tidak dapat menggunakan perintah bot.

/block [username atau balas ke pengguna] : Blokir pengguna dari bot kami.
/unblock [username atau balas ke pengguna] : Hapus blokir pengguna.
/blockedusers : Tampilkan daftar pengguna yang diblokir.
"""

HELP_6 = """
<u><b>Perintah Putar Channel:</b></u>

Anda dapat streaming audio/video di channel.

/cplay : Mulai streaming lagu yang diminta di video chat channel.
/cvplay : Mulai streaming video yang diminta di video chat channel.
/cplayforce atau /cvplayforce : Hentikan streaming yang sedang berlangsung dan mulai streaming lagu yang diminta.

/channelplay [username atau ID chat] atau [disable] : Hubungkan channel ke grup dan mulai streaming lagu dengan perintah yang dikirim di grup.
"""

HELP_7 = """
<u><b>Fitur Global Ban</b></u> [Hanya untuk pengguna sudo]:

/gban [username atau balas ke pengguna] : Blokir pengguna secara global dari semua chat yang dilayani dan blacklist mereka dari menggunakan bot.
/ungban [username atau balas ke pengguna] : Hapus blokir global pengguna.
/gbannedusers : Tampilkan daftar pengguna yang diblokir secara global.
"""

HELP_8 = """
<b><u>Loop Streaming:</b></u>

<b>Mulai streaming yang sedang berlangsung dalam loop</b>

/loop [enable/disable] : Aktifkan/nonaktifkan loop untuk streaming yang sedang berlangsung
/loop [1, 2, 3, ...] : Aktifkan loop untuk nilai yang diberikan.
"""

HELP_9 = """
<u><b>Mode Pemeliharaan</b></u> [Hanya untuk pengguna sudo]:

/logs : Dapatkan log bot.

/logger [enable/disable] : Bot akan mulai mencatat aktivitas yang terjadi di bot.

/maintenance [enable/disable] : Aktifkan atau nonaktifkan mode pemeliharaan bot Anda.
"""

HELP_10 = """
<b><u>Ping & Statistik:</b></u>

/start : Mulai bot musik.
/help : Dapatkan menu bantuan dengan penjelasan perintah.

/ping : Tampilkan ping dan statistik sistem bot.

/stats : Tampilkan statistik keseluruhan bot.
"""

HELP_11 = """
<u><b>Perintah Putar:</b></u>

<b>v :</b> untuk video play.
<b>force :</b> untuk force play.

/play atau /vplay : Mulai streaming lagu yang diminta di video chat.

/playforce atau /vplayforce : Hentikan streaming yang sedang berlangsung dan mulai streaming lagu yang diminta.
"""

HELP_12 = """
<b><u>Acak Antrean:</b></u>

/shuffle : Acak antrean.
/queue : Tampilkan antrean yang diacak.
"""

HELP_13 = """
<b><u>Cari Streaming:</b></u>

/seek [durasi dalam detik] : Cari streaming ke durasi yang diberikan.
/seekback [durasi dalam detik] : Mundur cari streaming ke durasi yang diberikan.
"""

HELP_14 = """
<b><u>Unduh Lagu:</b></u>

/song [nama lagu/URL YouTube] : Unduh lagu dari YouTube dalam format MP3 atau MP4.
"""

HELP_15 = """
<b><u>Perintah Kecepatan:</b></u>

Anda dapat mengontrol kecepatan pemutaran streaming yang sedang berlangsung. [Hanya admin]

/speed atau /playback : Untuk menyesuaikan kecepatan pemutaran audio di grup.
/cspeed atau /cplayback : Untuk menyesuaikan kecepatan pemutaran audio di channel.
"""

HELP_16 = """
<b><u>ChatGPT:</b></u>

/advice - Dapatkan saran acak dari bot
/ai [pertanyaan Anda] - Ajukan pertanyaan ke AI ChatGPT
/gemini [pertanyaan Anda] - Ajukan pertanyaan ke AI Gemini Google
/bard [pertanyaan Anda] - Ajukan pertanyaan ke Bard AI Google
"""

HELP_17 = """
<b><u>Hewan:</b></u>

/fox : Dapatkan gambar rubah acak.
/cat : Dapatkan gambar kucing acak.
/dog : Dapatkan gambar anjing acak.
"""

HELP_18 = """
<b><u>Reel:</b></u>

Pengunduh Reels Instagram:

/ig [URL]: Unduh reels Instagram. Berikan URL reel setelah perintah
/instagram [URL]: Unduh reels Instagram. Berikan URL reel setelah perintah
/reel [URL]: Unduh reels Instagram. Berikan URL reel setelah perintah
"""

HELP_19 = """
<b><u>Perintah Anime:</b></u>

/anime [judul] : Cari anime dengan judul yang diberikan.
"""

HELP_20 = """
<b><u>Info:</b></u>

/whois - **Memeriksa informasi pengguna.**

**Informasi:**

- Bot ini menyediakan perintah untuk memeriksa informasi pengguna.
- Gunakan perintah /whois diikuti dengan balasan pesan atau ID Pengguna untuk mendapatkan informasi pengguna.

**Catatan:**

- Perintah /whois dapat digunakan untuk mengembalikan informasi tentang pengguna di chat.
- Informasi termasuk ID, Nama Pertama, Nama Akhir, Username, dan status online.
"""

HELP_21 = """
<b><u>Wallpaper:</b></u>

/wall - Unduh dan kirim wallpaper.

Informasi:

- Bot ini menyediakan perintah untuk mengunduh dan mengirim wallpaper.
- Gunakan perintah /wall dengan kata kunci untuk mencari dan mengirim wallpaper di chat.

Catatan:

- Perintah ini dapat digunakan untuk mengunduh dan mengirim wallpaper.
- Gunakan kata kunci untuk mencari wallpaper.
"""
