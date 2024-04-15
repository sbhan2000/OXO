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





REPLY_MESSAGE = "**صلي علي النبي وتبسم ♥️🌿**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("القسم الديني"),
              ("قسم السورس")
          ],
          [
             ("قسم الالعاب المتطورة")
          ],
          [
             ("قسم الرمزيات"),
              ("قسم التسلية")
          ],
          [
             ("اخفاء الكيبورد")
    ]
]

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.command(["اخفاء الكيبورد"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""**🥤| تم اخفاء الكيبورد بنحاح\n\n🥤| لعرض الكيبورد مرة اخرى ارسل /start **""",
        reply_markup=ReplyKeyboardRemove(selective=True))


REPLY_MESSAGE = "**صلي علي النبي وتبسم ♥️🌿**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("القسم الديني"),
              ("قسم السورس")
          ],
          [
             ("قسم الالعاب المتطورة")
          ],
          [
             ("قسم الرمزيات"),
              ("قسم التسلية")
          ],
          [
             ("اخفاء الكيبورد")
    ]
]

@app.on_message(filters.regex("^رجوع"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

