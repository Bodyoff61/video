import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "UU_O_F")
ALIVE_NAME = getenv("ALIVE_NAME", "B O D Y ,")
BOT_USERNAME = getenv("BOT_USERNAME", "bodamusic_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "boda_music9")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "party_body")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "zkryat_zman")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "6000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/islam-20055/video")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/6a91aea34abd0cfe22df9.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6a91aea34abd0cfe22df9.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/6a91aea34abd0cfe22df9.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/6a91aea34abd0cfe22df9.jpg")
