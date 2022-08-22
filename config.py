## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgB4pssidoDH4m24hOgLGFTIW-gDFWmIKWHOuBVK-ZzjXujY-WPz8-nVNtG5GdDcewBKHEMc_wCGLmOEC8VZqEohT10_as7cEhIO9evoOZL3v0Toe5BRc2chcD56FVv3Nq0Fq0s1Z8wxT4Ml_4SMQ6Hp6zrJOdA5AJB5OlZorI1PTCb5BlI5rcl6y3zKJdTQJCyY2w0qqu4oPn2WOZ22FaSiPxjCHX22CFpPYIym2oLVVSN0rSyqCzw8HRtkYF1tz9nntMZU6LiVC6afFriWAJOTHrYzhqyydEYddrFoJkvAByQJrxzYfN1j1qLQ-xjbcVZeRNcQp0XnlBv1UGYdnxmWAAAAATR-cfMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5309805590:AAHV4VS0WN2qGhAKVXvqBjf46LVcVbsfNrI")
BOT_NAME = getenv("BOT_NAME", "BABLOO ")
API_ID = int(getenv("API_ID", "13073962"))
API_HASH = getenv("API_HASH", "50244b5474c1f5f6a50865dd756f2910")
OWNER_NAME = getenv("OWNER_NAME", "BABLOO ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "AC_BABLOO")
ALIVE_NAME = getenv("ALIVE_NAME", "BABLOO ")
BOT_USERNAME = getenv("BOT_USERNAME", "Music_BaBLOO_bot")
OWNER_ID = getenv("OWNER_ID", "5041044821")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝐌𝐔𝐒𝐈𝐂 ✘𝘽𝘼𝘽𝙇𝙊𝙊")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/hsjabaavanvsb")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/BA_BLOO")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5041044821").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split(/)
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
