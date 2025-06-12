from pyrogram import Client
from config.env_config import API_ID, API_HASH, SESSION

app = Client(
    "ultra_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)
