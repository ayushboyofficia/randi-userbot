from pyrogram import Client, filters

@Client.on_message(filters.command("spam") & filters.me)
async def spam(client, message):
    try:
        count = int(message.command[1])
        text = " ".join(message.command[2:])
        for _ in range(count):
            await message.reply(text)
    except:
        await message.reply("Usage: /spam [count] [text]")
