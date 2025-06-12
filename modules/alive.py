from pyrogram import Client, filters
from config.env_config import BOT_NAME

@Client.on_message(filters.command("alive") & filters.me)
async def alive(client, message):
    await message.reply(f"🤖 {BOT_NAME} is Alive and Working!")
