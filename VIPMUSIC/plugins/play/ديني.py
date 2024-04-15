import asyncio
from pyrogram import Client, filters
from strings import get_string
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from VIPMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest



REPLY_MESSAGE = "**🥤| اهلا بك عزيزي العضو في القسم الديني**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("الختمة")
          ],
          [
             ("سورة عشوائية"),
              ("قران")
          ],
          [
             ("اية"),
              ("اذكار")
          ],
          [
             ("دعاء"),
              ("حديث")
          ],
          [
             ("خطبة"),
              ("كتاب اسلامي")
          ],
          [
             ("رجوع")
    ]
]

@app.on_message(filters.regex("^القسم الديني"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



          
