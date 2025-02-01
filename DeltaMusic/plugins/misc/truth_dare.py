from pyrogram import Client, filters
import requests
import random
from DeltaMusic import app

# Truth or Dare API URLs
truth_api_url = "https://api.truthordarebot.xyz/v1/truth"
dare_api_url = "https://api.truthordarebot.xyz/v1/dare"

@app.on_message(filters.command("truth"))
def get_truth(client, message):
    try:
        # Make a GET request to the Truth API
        response = requests.get(truth_api_url)
        if response.status_code == 200:
            truth_question = response.json()["question"]
            message.reply_text(f"Pertanyaan Truth:\n\n{truth_question}")
        else:
            message.reply_text("Gagal mengambil pertanyaan truth. Silakan coba lagi nanti.")
    except Exception as e:
        message.reply_text("Terjadi kesalahan saat mengambil pertanyaan truth. Silakan coba lagi nanti.")

@app.on_message(filters.command("dare"))
def get_dare(client, message):
    try:
        # Make a GET request to the Dare API
        response = requests.get(dare_api_url)
        if response.status_code == 200:
            dare_question = response.json()["question"]
            message.reply_text(f"Tantangan Dare:\n\n{dare_question}")
        else:
            message.reply_text("Gagal mengambil tantangan dare. Silakan coba lagi nanti.")
    except Exception as e:
        message.reply_text("Terjadi kesalahan saat mengambil tantangan dare. Silakan coba lagi nanti.")
