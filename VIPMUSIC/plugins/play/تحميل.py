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
import os
import requests
from random import randint
from VIPMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)

from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton, CallbackQuery,
                            InlineKeyboardMarkup, Message)
from VIPMUSIC.utils import close_markup
from config import BANNED_USERS, SERVER_PLAYLIST_LIMIT
from VIPMUSIC import Carbon, app
from VIPMUSIC.utils.decorators.language import language, languageCB
from VIPMUSIC.utils.inline.playlist import (botplaylist_markup,
                                              get_playlist_markup,
                                              warning_markup)
from VIPMUSIC.utils.pastebin import VIPBin
import time
import asyncio
import yt_dlp
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos

from VIPMUSIC.utils.stream.stream import stream
from typing import Dict, List, Union
from time import time
import asyncio
from VIPMUSIC.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5
from VIPMUSIC.core.mongo import mongodb


yt = YouTube(f"https://youtu.be/{videoid}")
                title = yt.title
                duration = yt.length
                thumbnail = f"https://img.youtube.com/vi/{videoid}/maxresdefault.jpg"
                plist = {
                    "videoid": videoid,
                    "title": title,
                    "duration": duration,
                }
                await save_playlist(user_id, videoid, plist)


@app.on_message(filters.command("vi") & filters.group & ~BANNED_USERS)
@language
async def song_commad_group(client, message: Message, _):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                text= "‹ تـحميل فـيديو ›",
                callback_data=f"downloadvideo {videoid}"),
                InlineKeyboardButton(
                text= "‹ تـحميل صـوت ›",
                callback_data=f"downloadaudio {videoid}",
                ),
            ]
        ]
    )
    await message.reply_text(_["song_1"], reply_markup=upl)
