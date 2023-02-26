import datetime
import sys
from pyrogram import Client

from utils.config import *

if __name__ == "__main__":
    app = Client(
        "my_account_1",
        api_id=API_ID_1,
        api_hash=API_HASH_1,
        hide_password=True,
    )

    app.start()
    try:
        app.send_message(
            "me",
            f"[{datetime.datetime.now()}] zxc-Userbot launched! \n"
        )
    except Exception:
        pass
    app.stop()
