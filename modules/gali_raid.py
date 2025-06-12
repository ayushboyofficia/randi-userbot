from pyrogram import Client, filters
import asyncio
GALI_LIST = ["BC", "MC", "chutiya", "madarchod"]

@Client.on_message(filters.command("galiraid") & filters.me)
async def gali_raid(client, message):
    for i in range(10):
        for gali in GALI_LIST:
            await message.reply(gali)
            await asyncio.sleep(0.2)
