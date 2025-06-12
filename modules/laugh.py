from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command("laugh") & filters.me)
async def laugh_anim(client, message):
    text = ["😂", "🤣", "😆", "😁", "😂😂"]
    for i in range(5):
        await message.edit(text[i % len(text)])
        await asyncio.sleep(0.2)
