import logging
from os import environ

# import logging
from pyrogram import Client, idle

API_ID = 18598239
API_HASH = "3501bc95d5d1ff38003fa4ecf04d552e"
SESSION_NAME = "wordlist"

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=dict(root="plugins"))
logging.basicConfig(level=logging.DEBUG)

app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
