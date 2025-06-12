from pyrogram import Client, filters
from datetime import datetime

afk_users = {}

@Client.on_message(filters.command("afk") & filters.me)
async def set_afk(client, message):
    afk_users[message.from_user.id] = datetime.now()
    await message.reply("AFK mode enabled.")

@Client.on_message(filters.private & ~filters.me)
async def check_afk(client, message):
    if afk_users.get(message.to_user.id):
        await message.reply("User is AFK.")
