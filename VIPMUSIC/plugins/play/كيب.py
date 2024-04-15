import asyncio
from pyrogram import Client, filters
from strings import get_string
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from VIPMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from random import choice
from pyrogram import filters
from strings import get_command
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

@app.on_message(filters.regex("^رجوع"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



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

@app.on_message(filters.regex("^القسم الديني"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



REPLY_MESSAGE = "**🥤| اهلا بك عزيزي العضو في قسم السورس**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("المبرمج")
          ],
          [
             ("السورس"),
              ("المطور")
          ],
          [
             ("رجوع")
    ]
]

@app.on_message(filters.regex("^قسم السورس"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



REPLY_MESSAGE = "**🥤| اهلا بك عزيزي العضو في قسم العاب المتطورة**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("المبرمج")
          ],
          [
             ("السورس"),
              ("المطور")
          ],
          [
             ("رجوع")
    ]
]

@app.on_message(filters.regex("^قسم الالعاب المتطورة"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



REPLY_MESSAGE = "**🥤| اهلا بك عزيزي العضو في قسم الرمزيات**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("خلفيات"),
              ("متحركه")
          ],
          [
             ("هيدرات"),
              ("ستوري")
          ],
          [
             ("جداريات"),
              ("رواية")
          ],
          [
             ("اقتباس"),
              ("اقتبس")
          ],
          [
             ("غنيلي"),
              ("راب")
          ],
          [
             ("ميمز"),
              ("شعر")
          ],
          [
             ("مزاجيات"),
              ("انمي")
          ],
          [
             ("افتاري"),
              ("صوره")
          ],
          [
             ("افتارات بنات"),
              ("افتارات شباب")
          ],
          [
             ("افتارات اطفال"),
              ("افتارات عيال")
          ],
          [
             ("افتارات دينيه"),
              ("افتارات رمضان")
          ],
          [
             ("افتارات رسم"),
              ("افتارات سينمائيه")
          ],
          [
             ("افتارات فكتوري"),
              ("افتارات كرتون")
          ],
          [
             ("رجوع")
    ]
]

@app.on_message(filters.regex("^قسم الرمزيات"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



REPLY_MESSAGE = "**🥤| اهلا بك عزيزي العضو في قسم التسلية**"
REPLY_MESSAGE_BUTTONS = [
    [
             ("كت"),
              ("كتص")
          ],
          [
             ("لو خيروك"),
              ("حروف")
          ],
          [
             ("صراحه"),
              ("نكته")
          ],
          [
             ("نصيحه"),
              ("حكمه")
          ],
          [
             ("رجوع")
    ]
]

@app.on_message(filters.regex("^قسم التسلية"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )
