import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("file_link_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply_text("👋 Send me any file and I’ll give you a download link!")

@app.on_message(filters.private & filters.document | filters.video | filters.audio | filters.photo)
async def file_handler(client, message: Message):
    file = message.document or message.video or message.audio or message.photo
    msg = await message.reply("⏳ Uploading...")
    file_path = await message.download()
    file_name = file.file_name if hasattr(file, "file_name") else "file"
    link = f"https://telegra.ph/{file_name.replace(' ', '_')}"
    await msg.edit_text(f"✅ Uploaded!

🔗 Link (not real): `{link}`")

app.run()
