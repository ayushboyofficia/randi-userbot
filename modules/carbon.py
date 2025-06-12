from pyrogram import Client, filters
import requests

@Client.on_message(filters.command("carbon") & filters.me)
async def carbon_func(client, message):
    code = message.reply_to_message.text if message.reply_to_message else None
    if not code:
        await message.reply("Reply to a message containing code.")
        return

    await message.reply("Generating carbon image...")

    response = requests.get("https://carbonara.solopov.dev/api/cook", json={"code": code})
    if response.status_code == 200:
        await message.reply_photo(response.content)
    else:
        await message.reply("Failed to generate carbon image.")
