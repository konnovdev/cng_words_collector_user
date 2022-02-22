import json
import logging

import requests
from pyrogram.types import Message


base_url = "https://api.cng.tw/v1/"


def save_message(message: Message):
    messages_url = base_url + "messages?token=uiehJSeqwWRWEOVP31WQsfafh23F"

    try:
        object_to_send = json.dumps(
            {
                "telegramSenderId": f"{str(message.from_user.id)}",
                "telegramChatId": f"{str(message.chat.id)}",
                "telegramMessageId": f"{str(message.message_id)}",
                "text": f"{str(message.text)}",
                "timestamp": f"{int(message.date)}"
            }
        )
        headers = {'Content-type': 'application/json', 'Accept': '*/*', 'Connection': 'keep-alive'}
        logging.debug(f"body: {str(object_to_send)}")
        requests.post(messages_url, data=object_to_send, headers=headers)
    except:
        pass


async def get_top_hanzi():
    hanzi_url = base_url + "hanzi"

    try:
        response = requests.get(hanzi_url)
        json_full_object = response.json()[:50]
        rank = ""
        index = 1
        for hanzi in json_full_object:
            rank += f"{index}) {hanzi.get('char')}, count: {hanzi.get('count')}\n"
            index += 1
        return rank
    except:
        pass
