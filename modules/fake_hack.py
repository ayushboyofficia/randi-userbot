from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command("hack") & filters.me)
async def fake_hack(client, message):
    msg = await message.reply("Hacking Target...")
    for i in range(0, 101, 10):
        await msg.edit(f"Hacking... {i}%")
        await asyncio.sleep(0.3)
    await msg.edit("💀 Target Hacked Successfully 💀")
