from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command("loveraid") & filters.me)
async def loveraid(client, message):
    text = "❤️ Love you ❤️"
    for _ in range(10):
        await message.reply(text)
        await asyncio.sleep(0.3)
