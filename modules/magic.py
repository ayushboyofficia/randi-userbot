from pyrogram import Client, filters
from core.utils import animate_text

@Client.on_message(filters.command("magic") & filters.me)
async def magic_animation(_, message):
    frames = ["✨", "🔮", "🪄", "✨🪄✨", "💥"]
    await animate_text(message, frames)
