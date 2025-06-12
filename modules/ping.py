from pyrogram import Client, filters
import time

@Client.on_message(filters.command("ping") & filters.me)
async def ping(client, message):
    start = time.time()
    msg = await message.reply("Pinging...")
    end = time.time()
    await msg.edit(f"Pong! {round(end - start, 3)}s")
