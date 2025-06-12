from pyrogram import Client, filters
from pyrogram.types import Message

approved_users = set()

@Client.on_message(filters.private & ~filters.me)
async def handle_pm(client, message: Message):
    user_id = message.from_user.id
    if user_id not in approved_users:
        await message.reply("⛔ PM not allowed. Type '/approve' to allow.")
    else:
        await message.reply("✅ You're approved!")

@Client.on_message(filters.command("approve") & filters.me)
async def approve_user(client, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        approved_users.add(user_id)
        await message.reply("✅ User approved!")
