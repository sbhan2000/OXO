

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


@app.on_message(filters.command(["شباب", "افتارات شباب"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/foravaboys/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار افتارات شباب اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

@app.on_message(filters.command(["بنات", "افتارات بنات"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار افتارات بنات اليك**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



@app.on_message(filters.command(["اطفال", "افتارات اطفال"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/N_Z_23/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار افتارات اطفال اليك**",
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



@app.on_message(filters.command(["عيال","افتارات عيال"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/foravaboys/{rl}"
    await client.send_photo(message.chat.id,url,caption="**🥤| تم اختيار افتارات عيال اليك**",
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


@app.on_message(filters.command(["تويت", "كت"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
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


@app.on_message(filters.command(["رواية","روايه","روايات"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "reaylop"
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




@app.on_message(filters.command(["مزاج","مزاجيات"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "message_voice"
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


@app.on_message(filters.command(["خطبة","خطب","خطبه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "fresdewi"
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




@app.on_message(filters.command(["كت بالصوره","تويت بالصورة","كت بالصورة","تويت بالصوره","كتص","كتص"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "cat_tuet"
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




@app.on_message(filters.command(["ميمز","ميمز"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "memzwatan"
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




@app.on_message(filters.command(["راب","راب"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "RapEthan"
   t = message.chat.id
   d = randint(2,100)
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




@app.on_message(filters.command(["حديث","احاديث"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "TheIslamicProphet"
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




@app.on_message(filters.command(["دعاء"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "aerty_yu"
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




@app.on_message(filters.command(["ايه","اية"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "jcoef"
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





@app.on_message(filters.command(["افتارات رمضان","افتار رمضان","رمضان"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_7(client, message):
   f = "ramad_any"
   t = message.chat.id
   d = randint(2,100)
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




@app.on_message(filters.command(["افتارات دينيه", "افتارات دينية"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "ahmeddeeny"
   t = message.chat.id
   d = randint(2,140)
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


@app.on_message(filters.command(["افتارات كرتون"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "l_b15"
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


@app.on_message(filters.command(["افتارات سينمائية","افتارات سينمائيه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "X4_CP"
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



@app.on_message(filters.command(["افتارات رسم"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "kebsjnsans"
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



@app.on_message(filters.command(["افتارات فكتوري"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "LoreBots6"
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



@app.on_message(filters.command(["نكتة","نكته","نكت"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "X4_GX"
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


@app.on_message(filters.command(["خلفيات","خلفيات"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "X4_WX"
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


@app.on_message(filters.command(["حالات","حالات واتس"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "RSHDO5"
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



@app.on_message(filters.command(["رمادي","افتارات رمادي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "shababbbbR"
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



@app.on_message(filters.command(["رماديه","افتارات رماديه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "banatttR"
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



@app.on_message(filters.command(["تطقيم","تطقيم بنات"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "Tatkkkkkim"
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



@app.on_message(filters.command(["حب","افتارات حب"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "tatkkkkkimh"
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


@app.on_message(filters.command(["معلومات","معلومه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(client, message):
   f = "A_l3l"
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



@app.on_message(filters.command(["تتويت"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def game_6(m):
            tweet = [
                "كت تويت ‏| تخيّل لو أنك سترسم شيء وحيد فيصبح حقيقة، ماذا سترسم؟",
                "كت تويت | أكثر شيء يُسكِت الطفل برأيك؟",
                "كت تويت | الحرية ل ... ؟",
                "كت تويت | قناة الكرتون المفضلة في طفولتك؟",
                "كت تويت ‏| كلمة للصُداع؟",
                "كت تويت ‏| ما الشيء الذي يُفارقك؟",
                "كت تويت | موقف مميز فعلته مع شخص ولا يزال يذكره لك؟",
                "كت تويت ‏| أيهما ينتصر، الكبرياء أم الحب؟",
                "كت تويت | بعد ١٠ سنين ايش بتكون ؟",
                "كت تويت ‏| مِن أغرب وأجمل الأسماء التي مرت عليك؟",
                "‏كت تويت | عمرك شلت مصيبة عن شخص برغبتك ؟",
                "كت تويت | أكثر سؤال وجِّه إليك مؤخرًا؟",
                "‏كت تويت | ما هو الشيء الذي يجعلك تشعر بالخوف؟",
                "‏كت تويت | وش يفسد الصداقة؟",
                "‏كت تويت | شخص لاترفض له طلبا ؟",
                "‏كت تويت | كم مره خسرت شخص تحبه؟.",
                "‏كت تويت | كيف تتعامل مع الاشخاص السلبيين ؟",
                "‏كت تويت | كلمة تشعر بالخجل اذا قيلت لك؟",
                "‏كت تويت | جسمك اكبر من عٌمرك او العكسّ ؟!",
                "‏كت تويت |أقوى كذبة مشت عليك ؟",
                "‏كت تويت | تتأثر بدموع شخص يبكي قدامك قبل تعرف السبب ؟",
                "كت تويت | هل حدث وضحيت من أجل شخصٍ أحببت؟",
                "‏كت تويت | أكثر تطبيق تستخدمه مؤخرًا؟",
                "‏كت تويت | ‏اكثر شي يرضيك اذا زعلت بدون تفكير ؟",
                "‏كت تويت | وش محتاج عشان تكون مبسوط ؟",
                "‏كت تويت | مطلبك الوحيد الحين ؟",
                "‏كت تويت | هل حدث وشعرت بأنك ارتكبت أحد الذنوب أثناء الصيام؟",
                "‏كت تويت | كم عمرك ؟",
                "‏كت تويت | اسم تحب الكل يناديك فيه ؟",
                "‏كت تويت | تاريخ تحبه ؟",
                "‏كت تويت | يوم من أيام الأسبوع تحبه ؟",
                "‏كت تويت | أحلى مطعم عندك ؟",
                "‏كت تويت | أفضل سنه دراسية عندك ؟",
                "‏كت تويت | أفضل مغني تحبه ؟",
                "‏كت تويت | نوم ولا أكل ؟",
                "‏كت تويت | الحباة ما تمشي بدون ؟",
                "‏كت تويت | حساب لازم تتابعه كل يوم ؟",
                "‏كت تويت | تاريخ ما تنساه ؟",
                "‏كت تويت | عندك استعداد تخسر كل شيء الا ؟",
                "‏كت تويت | منشن ل اقرب شخص لك بالتليجرام ؟",
                "‏كت تويت | شيل اول حرف من اسمك واخر حرف وشوف هيبقى اى ؟",
                "‏كت تويت | كيف حال قلبك الان ؟",
                "‏كت تويت | كم الساعه بهاتفك الان ؟",
                "‏كت تويت | اسم اول حب بحياتك ؟",
                "‏كت تويت | ماهو افضل بوت على التليجرام ؟"

            ]
            await m.reply_text(random.choice(tweet), reply_to_message_id=m.message_id)

