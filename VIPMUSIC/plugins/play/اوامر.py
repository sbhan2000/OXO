import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_CHANNEL, SUPPORT_CHAT
from VIPMUSIC import app
import config
from config import BANNED_USERS
from config import OWNER_ID
from strings import get_string
from VIPMUSIC import Telegram, YouTube, app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.plugins.play.playlist import del_plist_msg
from VIPMUSIC.plugins.sudo.sudoers import sudoers_list
from VIPMUSIC.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
                                       
                                       
                                       
@app.on_message(filters.command(["الاوامر","اوامر"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def mpdtsf(_, query: CallbackQuery):
   await msg.reply_photo(
        photo=f"https://te.legra.ph/file/4cd1170965414e0e53882.mp4",
        caption=f"""**<u>صلي علي النبي وتبسم ♥️🌿</u>**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "أضـف البوت لمجموعتڪ ✅", url=f"https://t.me/{app.username}?startgroup=true"),
                ],[
                    InlineKeyboardButton(
                        " قـناة الـبوت ⚙", url=f"{SUPPORT_CHANNEL}"),
                    InlineKeyboardButton(
                        "الـدعم", url=f"{SUPPORT_CHAT}"),
                ],[
                    InlineKeyboardButton(
                        " اوامر الـبوت 🌐", callback_data="settings_back_helper"),                        
                ],
            ]
        ),
    )

