import re, os
from os import environ
from translation import LuciferMoringstar
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "on"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "off"]:
        return False
    else:
        return default

# ==================================
API_ID = int(2054877)
API_HASH =  "4227c1e45e462209a3dcc67ada88a44f"
B_KEYS = "5257335519:AAGBSBkxfuEQMVDg7j_Q3uhhNcrIn63Aeqw"
START_MSG = environ.get("START_MSG", LuciferMoringstar.DEFAULT_MSG)
BOT_PICS = (environ.get('PICS', 'https://telegra.ph/file/8d4e4693a8a907cb51797.jpg')).split()
SUPPORT = environ.get("SUPPORT", "t.me/trvpn")
SPELL_MODE = is_enabled((environ.get('SPELL_MODE', "on")), True)
SET_SPEL_M = environ.get("SPELL_MODE_TEXT", LuciferMoringstar.SPELL_CHECK)
LOG_CHANNEL = int(environ.get("LOG_CHANNEL",  -1001366123484))

FORCE = environ.get('FORCES_SUB')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", LuciferMoringstar.FILE_CAPTIONS)
DEV_NAME = environ.get("DEV_NAME", "Muhammed")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '957158815').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001594798134').split()]
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
DATABASE_URI = "mongodb+srv://trvpn:trvpn@cluster0.ve0u8.mongodb.net/?retryWrites=true&w=majority"
COLLECTION_NAME = 'Telegram_files'
DATABASE_NAME = "Cluster0"

# ==================================
# Empty 😂

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
BUTTONS = {}
CURRENT = int(environ.get("SKIP", 2))
CANCEL = False
FORCES_SUB = int(FORCE) if FORCE and id_pattern.search(FORCE) else FORCE

AUTH_USERS = (auth_users + ADMINS) if auth_users else []
# ==================================

team_name = os.environ.get('team_name', 'Mo Tech 🇮🇳')
team_link = os.environ.get('team_link', 't.me/Mo_Tech_YT')

# ==================================
# About Bot 🤖
class bot_info(object):
    BOT_NAME = None
    BOT_USERNAME = None
    BOT_ID = None


