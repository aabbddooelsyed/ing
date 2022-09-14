## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABE88UUIfuq0SJyfiB5TxVNwj_H-j3vv-UEaDk174f0iXHTYcIJLU9IYCj3jxeyf-jA_Fjgb16-Y4XHtPvNlX8kC6yhpzIbX5jk89xmFkncJ4l-ciPU1Vi2K0Ql9tgHvPzn2leI2XYvG3u0hfeNmkC-hRVqRMq-ts9CB_1EuKMueZ9UbrAF5Q-YkZqqd1-AQBIUNhwyvZxqOdgdDh7cUtln5UWvtLPy8OBKfMrMdSj8YHDHov4ZPGoJEeL1Z6dEMwW6gbdYTzGnRDRJ3-X7Nf_K6CStRkwQRO86yYcYRUmjqROfW9rhPR1sjf1nGygl6J_xG0h0jwzyVpOYy3jbNA-YAAAAAUU0PQAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5611447282:AAER77vd0VqY_Amcx9DFnwgQbGMrQZ0HTes")
BOT_NAME = getenv("BOT_NAME", "SPONG")
API_ID = int(getenv("API_ID", "6306086"))
API_HASH = getenv("API_HASH", "b07fa3d6c2499770c9c908c53fd6343e")
OWNER_NAME = getenv("OWNER_NAME", "✘ 𝙏𝙝𝙀 𝘽𝘼𝘽𝙇𝙊𝙊 ⍣⃝🇸🇮")
OWNER_USERNAME = getenv("OWNER_USERNAME", "AC_BABLOO")
ALIVE_NAME = getenv("ALIVE_NAME", "BABLOO")
BOT_USERNAME = getenv("BOT_USERNAME", "SPONG_POP_bot")
OWNER_ID = getenv("OWNER_ID", "5041044821")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝐌𝐔𝐒𝐈𝐂 ✘𝘽𝘼𝘽𝙇𝙊𝙊")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/BA_BLOO")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/BA_BLOO")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5041044821").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
