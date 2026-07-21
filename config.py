# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8154426339")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002170811388")) #Your db channel Id
OWNER = os.environ.get("OWNER", "sewxiy") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "7328629001")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluooo")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "60"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/CodeflixSupport")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/0R9k9x4M/tmpbtpr7q0.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/sdYHCnBC/tmp9peum4mg.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @As_Networks\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n└/commands: ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Animes_Station>ᴀɴɪᴍᴇ sᴛᴀᴛɪᴏɴ</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/animes_station>ᴀɴɪᴍᴇ sᴛᴀᴛɪᴏɴ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/as_networks>ᴀs ɴᴇᴛᴡᴏʀᴋ</a>\n◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+fD0wqOhZnqNmZmQ9>ᴀɴɪᴍᴇ sᴛᴀᴛɪᴏɴ</a>\n◈ ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+x9G79j7Cc2QyYjc1>ᴍᴏᴠɪᴇs sᴛᴀᴛɪᴏɴ</a>\n◈ ʜᴇɴᴛᴀɪ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Adults_Station>ʜᴇɴᴛᴀɪ sᴛᴀᴛɪᴏɴ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Animes_station>ᴀɴɪᴍᴇ sᴛᴀᴛɪᴏɴ</a></blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʏ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄᴏᴍᴍᴜɴɪᴛʏ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴜᴘᴘᴏʀᴛ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ ʏᴏᴜ ᴄᴀɴ ᴅᴏ sᴏ ʙʏ sᴜʙsᴄʀɪʙɪɴɢ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ\nᴛʜᴀɴᴋs ғᴏʀ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ</b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><blockquote>ʜᴇʟʟᴏ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <a href='https://t.me/Ecchi_Dex'>ᴇᴄᴄʜɪ ᴅᴇx</a></blockquote>ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ғɪʀsᴛ, ᴘʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ ʙᴏᴛ ᴀɢᴀɪɴ<blockquote>ʜᴏᴡ ᴛᴏ ᴜsᴇ ʙᴏᴛ <a href=https://t.me/NexusTutorial/6>ᴛᴜᴛᴏʀɪᴀʟ ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></blockquote></b>")

CMD_TXT = """<blockquote><b>» ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /start :</b> start the bot or get posts
<b>›› /batch :</b> create link for more than one posts
<b>›› /custom_batch :</b> create custom batch from channel/group
<b>›› /genlink :</b> create link for one post
<b>›› /users :</b> view bot statistics
<b>›› /broadcast :</b> broadcast any messages to bot users
<b>›› /pbroadcast :</b> broadcast and pin any messages to bot users
<b>›› /fbroadcast :</b> forward broadcast any messages to bot users
<b>›› /dbroadcast :</b> broadcast any messages with auto delete
<b>›› /stats :</b> check your bot uptime
<b>›› /dlt_time :</b> set auto delete time for files
<b>›› /check_dlt_time :</b> check current delete time setting
<b>›› /ban :</b> ban a user from using the bot
<b>›› /unban :</b> unban a previously banned user
<b>›› /banlist :</b> get list of banned users
<b>›› /addchnl :</b> add a channel for force subscription
<b>›› /delchnl :</b> remove a force subscribe channel
<b>›› /listchnl :</b> view all added force subscribe channels
<b>›› /fsub_mode :</b> toggle force subscribe on or off
<b>›› /add_admin :</b> add a new admin
<b>›› /deladmin :</b> remove an admin
<b>›› /admins :</b> list all current admins"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @nova_flix</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Sᴏʀʀʏ... ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀ sɪɢᴍᴀ"
#--------------------------------------------


LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
