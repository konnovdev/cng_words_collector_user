from pyrogram.types import Message

from pyrogram import Client, filters
from tools.cng_api import get_top_hanzi


@Client.on_message(filters.command(["rankhanzi"])
                   & filters.incoming
                   & ~filters.edited)
async def handleCommand(message: Message):
    await message.reply(await get_top_hanzi())
