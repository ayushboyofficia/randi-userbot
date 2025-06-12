from pyrogram import Client, filters

@Client.on_message(filters.command("help") & filters.me)
async def help_command(client, message):
    help_text = """
**Available Commands:**
/ping - Ping check
/afk - Set AFK
/approve - Approve PM
/shayari - Send Shayari
/magic - Magic Animation
/laugh - Laughing emoji
/spam [n] [text] - Spam text
/carbon - Carbon code image
/fakehack - Fake Hacking
/loveraid - Love spam
/galiraid - Gaali spam
"""
    await message.reply(help_text)
