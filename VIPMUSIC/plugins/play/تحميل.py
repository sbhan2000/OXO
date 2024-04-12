import os
import re

import yt_dlp
from pykeyboard import InlineKeyboard
from pyrogram import enums, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaAudio,
    InputMediaVideo,
    Message,
)

from config import BANNED_USERS
from VIPMUSIC import YouTube, app
from VIPMUSIC.utils.decorators.language import language, languageCB
from VIPMUSIC.utils.formatters import convert_bytes
import time
from time import time
import asyncio
from pyrogram.errors import UserAlreadyParticipant
import random
from pyrogram.errors import UserNotParticipant
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch
import config
from VIPMUSIC import app
from VIPMUSIC.misc import _boot_
from VIPMUSIC.utils import bot_up_time
from VIPMUSIC.plugins.sudo.sudoers import sudoers_list
from VIPMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from VIPMUSIC.utils.decorators.language import LanguageStart
from VIPMUSIC.utils.formatters import get_readable_time
from VIPMUSIC.utils.inline import first_page, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string
from VIPMUSIC.utils.database import get_assistant
from time import time
import asyncio
from VIPMUSIC.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5
# Command


@app.on_message(filters.command("vi") & filters.group & ~BANNED_USERS)
@language
async def song_commad_group(client, message: Message, _):
    key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text= "‹ تحميل فيديو ›", callback_data=f"downloadvideo {query}"),
                        InlineKeyboardButton(text= "‹ تحميل صوت ›", callback_data=f"downloadaudio {query}"),
                
                    ],
                ]
            )

