# helper for strings

class Helper(object):
    HELP_M = '''Pilih kategori untuk mendapatkan bantuan.
Ajukan pertanyaan Anda di chat dukungan.

Semua perintah dapat digunakan dengan: /'''
    HELP_ChatGPT = '''ChatGPT

Perintah ChatGPT:

/ask ➠ Mengajukan pertanyaan ke model AI untuk mendapatkan jawaban.
'''

    HELP_Reel = '''Reel

Perintah Reel:

/ig [URL] ➠ Unduh reel Instagram. Berikan URL reel Instagram setelah perintah.
/instagram [URL] ➠ Unduh reel Instagram. Berikan URL reel Instagram setelah perintah.
/reel [URL] ➠ Unduh reel Instagram. Berikan URL reel Instagram setelah perintah.
'''

    HELP_Info = '''Info

Perintah Info:

/id ➠ Dapatkan ID grup saat ini. Jika digunakan dengan membalas pesan, mendapatkan ID pengguna tersebut.
/info ➠ Dapatkan informasi tentang pengguna.
'''
    HELP_History = '''Riwayat

Perintah Riwayat:

Ini adalah perintah manajemen grup yang tersedia:

⦿ /sg atau /History
Deskripsi:
⦿ Mengambil pesan acak dari riwayat pesan pengguna.

Penggunaan:
⦿ /sg [username/ID/balas]

Detail:
⦿ Mengambil pesan acak dari riwayat pesan pengguna yang ditentukan.
⦿ Dapat digunakan dengan memberikan username, ID pengguna, atau membalas pesan dari pengguna.
⦿ Hanya dapat diakses oleh asisten bot.

Contoh:
⦿ /sg username
⦿ /sg user_id
⦿ /sg [balas pesan]
'''

    HELP_Couples = '''Pasangan

Perintah Pasangan:

/couples ➠ Memilih 2 pengguna dan mengirimkan nama mereka sebagai pasangan di chat Anda.
'''

    HELP_Extra = '''Ekstra

Perintah Ekstra:

⦿ /tgm ➠ Mengunggah foto (di bawah 5MB) ke cloud dan memberikan tautan.
⦿ /paste ➠ Mengunggah cuplikan teks ke cloud dan memberikan tautan.
⦿ /tr ➠ Menerjemahkan teks.
'''
    HELP_Action = '''Aksi

Perintah Aksi:

Perintah yang tersedia untuk Ban & Mute:

❍ /kickme ➠ Mengeluarkan pengguna yang mengeluarkan perintah

Hanya Admin:
❍ /ban <userhandle> ➠ Melarang pengguna. (via handle, atau balasan)
❍ /sban <userhandle> ➠ Melarang pengguna secara diam-diam. Menghapus perintah, pesan yang dibalas, dan tidak membalas. (via handle, atau balasan)
❍ /tban <userhandle> x(m/h/d) ➠ Melarang pengguna untuk waktu x. (via handle, atau balasan). m = menit, h = jam, d = hari.
❍ /unban <userhandle> ➠ Membatalkan larangan pengguna. (via handle, atau balasan)
❍ /kick <userhandle> ➠ Mengeluarkan pengguna dari grup, (via handle, atau balasan)
❍ /mute <userhandle> ➠ Membisukan pengguna. Dapat juga digunakan sebagai balasan, membisukan pengguna yang dibalas.
❍ /tmute <userhandle> x(m/h/d) ➠ Membisukan pengguna untuk waktu x. (via handle, atau balasan). m = menit, h = jam, d = hari.
❍ /unmute <userhandle> ➠ Membatalkan bisu pengguna. Dapat juga digunakan sebagai balasan, membisukan pengguna yang dibalas.
__
Perintah Khusus Mendukung Semua Contoh - DeltaMusic Ban DeltaMusic Mute DeltaMusic Promote ..... dll
'''
    HELP_Search = '''Pencarian

Perintah Pencarian:

• /google <query> ➠ Mencari di Google untuk query yang diberikan.
• /image (/imgs) <query> ➠ Mendapatkan gambar terkait query Anda.

Contoh:
• /google pyrogram ➠ Mengembalikan 5 hasil teratas.
'''

    HELP_Font = '''Font

Bantuan untuk modul font:

Modul font:

Dengan menggunakan modul ini Anda dapat mengubah font teks apa pun!

◌ /font [teks]
'''
    HELP_Bots = '''Bot

Bantuan untuk modul Bot:

Modul permainan:

◌ /bots ➠ Mendapatkan daftar bot di grup.
'''
    HELP_TG = '''T-Graph

Perintah T-Graph:

Membuat tautan telegra.ph untuk media apa pun!

◌ /tgm [balas media apa pun]
◌ /tgt [balas media apa pun]
'''
    HELP_Source = '''Sumber

Modul ini menyediakan perintah utilitas bagi pengguna untuk berinteraksi dengan bot:

Modul Sumber:

◌ /repo ➠ Mendapatkan tautan ke repositori kode sumber bot.
'''
    HELP_TD = '''Truth-Dare

Bantuan untuk modul Truth-Dare:

Truth dan Dare:
◌ /truth ➠ Mengirimkan pertanyaan truth acak.
◌ /dare ➠ Mengirimkan tantangan dare acak.
'''
    HELP_Quiz = '''Kuis

Bantuan untuk modul Kuis:

Kuis:
◌ /quiz ➠ Mendapatkan kuis acak.
'''
    HELP_TTS = '''TTS

Bantuan untuk modul TTS:

TTS:
◌ /tts [teks]

Penggunaan ➛ Teks ke audio
'''
    HELP_Radio = '''Radio

Bantuan untuk modul Radio:

◌ /radio ➠ Memutar radio di obrolan suara.
'''
    HELP_Q = '''Quotly

Bantuan untuk modul Quotly:

◌ /q ➠ Membuat kutipan dari pesan

◌ /q r ➠ Membuat kutipan dari pesan dengan balasan
'''
    
    fullpromote = {
    'can_change_info': True,
    'can_post_messages': True,
    'can_edit_messages': True,
    'can_delete_messages': True,
    'can_invite_users': True,
    'can_restrict_members': True,
    'can_pin_messages': True,
    'can_promote_members': True,
    'can_manage_chat': True,
}

    promoteuser = {
    'can_change_info': False,
    'can_post_messages': True,
    'can_edit_messages': True,
    'can_delete_messages': False,
    'can_invite_users': True,
    'can_restrict_members': False,
    'can_pin_messages': False,
    'can_promote_members': False,
    'can_manage_chat': True,
}
