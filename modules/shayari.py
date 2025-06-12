from pyrogram import Client, filters
import random

SHAYARIS = [
    "Dil se dil tak baat pohchi 💖",
    "Mohabbat ek nasha hai 🥀",
    "Tere bina zindagi se koi shikwa to nahi 💔"
]

@Client.on_message(filters.command("shayari") & filters.me)
async def shayari(client, message):
    await message.reply(random.choice(SHAYARIS))
