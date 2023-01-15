import datetime
import sys
from pyrogram import Client

from utils.config import *

if __name__ == "__main__":
    app = Client(
        "my_account_2",
        api_id=API_ID_2,
        api_hash=API_HASH_2,
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
