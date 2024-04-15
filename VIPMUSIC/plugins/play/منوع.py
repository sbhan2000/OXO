

import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VIPMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VIPMUSIC import app
from random import  choice, randint


@app.on_message(filters.command([f"شعر", "شع", "ش", "{BOT_USERNAME} شعر"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/saresnx/{rl}"
    await client.send_voice(message.chat.id,url,caption="**🥤| تـم اختيـار الشعر لـك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(filters.command(["غنيلي", "‹ غنيلي ›", "غ"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/proxMusicl/{rl}"
    await client.send_voice(message.chat.id,url,caption="**🥤| تم اختيار اغنية عشوائيه لك 🤍**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(filters.command(["صوره", "‹ صور ›","ص"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار صوره اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(filters.command(["‹ انمي ›", "انمي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار انمي اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(filters.command(["متحركه","‹ متحركه ›","متحركة"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="**🥤| تم اختيار المتحركه اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["اقتباس بالصوره","اقتبس"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار اقتباس اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["هيدرا", "‹ هيدرات ›","هيدرات"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار هيدرات اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(filters.command(["شباب", "افتار شباب"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/mlscc_dhsb/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار افتار شباب اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["‹ قران ›", "قران"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/lllIIlIllIlIIlI/{rl}"
    await client.send_voice(message.chat.id,url,caption="**🥤| تم اختيار ايـه قرآنيه اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )




@app.on_message(filters.command(["استوري", "‹ ستوريات ›","ستوري"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,50)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption="**🥤| تم اختيار استوري اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(filters.command(["صور جداريه", "صور جدارية","جداريات"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/bvdvdvdvb/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار صوره جدارية اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



@app.on_message(filters.command(["عيال","افتار عيال"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/foravaboys/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار افتار عيال اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )






@app.on_message(filters.command(["كتاب اسلامي", "كتاب"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_5(client, message):
   f = "kotobeslameah"
   t = message.chat.id
   d = randint(2,190)
   await app.copy_message(
      t,
      f,
      d,
      reply_to_message_id=message.id,
      reply_markup=InlineKeyboardMarkup(
      [
      [
      InlineKeyboardButton(message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
      ]
      ]
      )
   )


@app.on_message(filters.command(["تويتت", "كتت"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "zczzf"
   t = message.chat.id
   d = randint(2,190)
   await app.copy_message(
      t,
      f,
      d,
      reply_to_message_id=message.id,
      reply_markup=InlineKeyboardMarkup(
      [
      [
      InlineKeyboardButton(message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
      ]
      ]
      )
   )


@app.on_message(filters.command(["اقتباس"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "quotes555v"
   t = message.chat.id
   d = randint(2,190)
   await app.copy_message(
      t,
      f,
      d,
      reply_to_message_id=message.id,
      reply_markup=InlineKeyboardMarkup(
      [
      [
      InlineKeyboardButton(message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
      ]
      ]
      )
   )


EMOJIS = list("😭🤣😂😅😆😁😄😃😀🥳🤩🤩😍🥰😘😚😙😗😉🤪😜😝😛😋🥲🙂🙃😶😐😑🫣🤭")
@app.on_message(filters.regex("^الاسرع$") & filters.group)
@app.on_edited_message(filters.regex("^الاسرع$") & filters.group)
async def game_1(client, message):
   emoji = choice(EMOJIS)
   re = f"^{emoji}$"
   ASK = await app.VIP(
     message.chat.id,
     "اسرع واحد يرسل الايموجي : `{}`".format(emoji),
     reply_to_message_id=message.id,
     filters=filters.regex(re)
   )
   await app.send_message(
      message.chat.id,
      "المستخدم {} كفو اجابتك صح".format(ASK.from_user.mention),
      reply_to_message_id=VIP.id
   )


EMO = [
  "👞:حذاء",
  "⭐:نجمة",
  "🕞:ساعة",
  "🍑:خوخ",
  "🛢️:نفط",
  "🎂:كيكة",
  "⚽:كورة",
  "🩳:شورت",
  "📒:دفتر",
  "🌹:وردة",
  "✏️:قلم",
  "🔥:نار",
  "💸:فلوس",
  "💻:لاب"
]
@app.on_message(filters.regex("^معاني$") & filters.group)
@app.on_edited_message(filters.regex("^معاني$") & filters.group)
async def game_3(client, message):
   A = choice(EMO)
   emo = A.split(":")[0]
   print(emo)
   ans = A.split(":")[1]
   print(ans)
   re = f"^{ans}$"
   ASK = await app.VIP(
     message.chat.id,
     "اسرع واحد يرسل معنى الايموجي {}".format(emo),
     reply_to_message_id=message.id,
     filters=filters.regex(re)
   )
   await ASK.reply(
    f"كفو {ASK.from_user.mention} اجابتك صحيحة"
   )


FLAGS = [
  "🇦🇪:الامارات",
  "🇧🇭:البحرين",
  "🇪🇬:مصر",
  "🇮🇶:العراق",
  "🇱🇧️:لبنان",
  "🇱🇺:لوكسمبورغ",
  "🇵🇰:باكستان",
  "🇹🇷:تركيا",
  "🇾🇪:اليمن",
  "🇸🇩:السودان",
  "🇸🇦:السعودية",
  "🇵🇸:فلسطين",
  "🇴🇲:سلطنة عمان",
  "🇯🇵:اليابان"
]
@app.on_message(filters.regex("^اعلام دول$") & filters.group)
@app.on_edited_message(filters.regex("^اعلام دول$") & filters.group)
async def game_4(client, message):
   A = choice(FLAGS)
   emo = A.split(":")[0]
   print(emo)
   ans = A.split(":")[1]
   print(ans)
   re = f"^{ans}$"
   VIP = await app.VIP(
     message.chat.id,
     "اسرع واحد يرسل اسم الدولة {}".format(emo),
     reply_to_message_id=message.id,
     filters=filters.regex(re)
   )
   await VIP.reply(
    f"كفو {VIP.from_user.mention} اجابتك صحيحة"
   )
