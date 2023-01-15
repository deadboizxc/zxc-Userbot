import subprocess
import os
import sys
from pyrogram import *
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
from time import sleep
from utils.config import (
    API_ID_1,
    API_HASH_1,
    TOKEN_1,
    API_ID_2,
    API_HASH_2,
    channel_id
)
from utils.misc import prefix
from pathlib import Path
from importlib import import_module
import logging
import platform
import asyncio
import datetime
import time
from utils.db import db
from utils.misc import userbot_version
from utils.scripts import restart


logging.basicConfig(level=logging.INFO)

app = Client("my_account_2",
              api_id=API_ID_2,
              api_hash=API_HASH_2,
              bot_token=TOKEN_1,
              plugins=dict(root="modules")
             )

#text = f"<b>[{datetime.datetime.now()}] Userbot launched! </b>\n"
logging.info("zxc-Userbot started!")
data = datetime.datetime.now().strftime("%Y-%m-%d"+" "+"%H:%M:%S")

app.start()
app.send_message("me", f"<b>[{data}]</b> zxc-Userbot launched! \n")
app.stop()
app.run()
