from pyrogram import Client, filters
from pyrogram.types import Message

from tools.cng_api import save_message

SITES_REGEX = (
    r"^((?:https?:)?\/\/)"
    r"?((?:www|m)\.)"
    r"?((?:youtube\.com|youtu\.be|soundcloud\.com|mixcloud\.com))"
    r"(\/)([-a-zA-Z0-9()@:%_\+.~#?&//=]*)([\w\-]+)(\S+)?$"
)
EXCLUDE_PLAYLISTS = (
    r"\/playlist\?list=|&list=|\/sets\/"
)


@Client.on_message(filters.text
                   & filters.incoming
                   & ~filters.edited
                   & ~filters.regex(r"^(p|P)ing$")
                   & ~filters.regex(r"^(u|U)ptime$")
                   & ~filters.regex(SITES_REGEX)
                   & ~filters.regex(EXCLUDE_PLAYLISTS))
async def log_message(_, message: Message):
    save_message(message)
