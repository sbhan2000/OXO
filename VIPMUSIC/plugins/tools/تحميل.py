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

from VIPMUSIC import YouTube, app
from VIPMUSIC.utils.decorators.language import language, languageCB
from VIPMUSIC.utils.formatters import convert_bytes
from VIPMUSIC.utils.inline.song import song_markup
from config import BANNED_USERS

# Command


@app.on_message(filters.command("vd") & filters.group & ~BANNED_USERS)
@language
async def song_commad_group(client, message: Message, _):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_2"],
                    url=f"https://t.me/{app.username}?start=song",
                ),
            ]
        ]
    )
    await message.reply_text(_["song_1"], reply_markup=upl)

