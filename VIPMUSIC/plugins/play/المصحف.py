from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb
from VIPMUSIC import app 
import json 
from config import BANNED_USERS
import requests 
from VIPMUSIC.core.call import VIP
import asyncio
import os
import time
import requests
from config import START_IMG_URL
import random
from VIPMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VIPMUSIC import app
from random import  choice, randint
import asyncio
import os
import time
import requests
import json
import urllib.parse
import urllib.request
from pyrogram import filters
from pyrogram import Client
from VIPMUSIC import app
from pyrogram.types import Message, InlineKeyboardMarkup



@app.on_message(filters.command(["المصحف"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def quran(c,msg):
    quran = json.loads(open("VIPMUSIC/assets/quran.json").read())["s"]
    keyboard = []
    list = []
    for i in range(1,11):
        if len(list) == 2:
            copy_list =list.copy()
            keyboard.append(copy_list)
            list.clear()
        name = quran[i-1]["surah"]
        list.append(ikb(name, callback_data = f"play-{i-1}"))
    keyboard.append(list)
    keyboard.append([ikb(". التالي .", callback_data = "next-1")])
    await msg.reply_photo(
        photo=f"https://telegra.ph/file/66dd6cfeb827ea98a9a84.png",
        caption=f"""**🥤| اهلا بك في قائمة اسماء سور القران الكريم.**""", reply_markup = ikm(keyboard))

@app.on_callback_query(filters.regex("next") & ~BANNED_USERS)
async def next_quran(c,cq):
    data = (cq.data.strip()).split("-")
    number = int(data[1])
    quran = json.loads(open("VIPMUSIC/assets/quran.json").read())["s"]
    keyboard = []
    list = []
    if (number*10) == 110:
        for i in range(1,5):
            if len(list) == 2:
                copy_list =list.copy()
                keyboard.append(copy_list)
                list.clear()
            name = quran[(i+(number*10))-1]["surah"]
            list.append(ikb(name, callback_data = f"play-{(i+(number*10))-1}"))
        keyboard.append(list)
        keyboard.append([ikb("‹ رجوع ›", callback_data = f"next-{number-1}")])
    elif number == 0:
        for i in range(1,11):
            if len(list) == 2:
                copy_list =list.copy()
                keyboard.append(copy_list)
                list.clear()
            name = quran[i-1]["surah"]
            list.append(ikb(name, callback_data = f"play-{i-1}"))
        keyboard.append(list)
        keyboard.append([ikb("‹ التالي ›", callback_data = "next-1")])
    else:
        for i in range(1,11):
            if len(list) == 2:
                copy_list =list.copy()
                keyboard.append(copy_list)
                list.clear()
            name = quran[(i+(number*10))-1]["surah"]
            list.append(ikb(name, callback_data = f"play-{(i+(number*10))-1}"))
        keyboard.append(list)
        keyboard.append([ikb("‹ رجوع ›", callback_data = f"next-{number-1}"), ikb(". التالي .", callback_data = f"next-{number+1}")])
    await cq.edit_message_reply_markup(ikm(keyboard))
            
@app.on_callback_query(filters.regex("play") & ~BANNED_USERS)
async def show_quran(c,cq):
    data = (cq.data.strip()).split("-")
    number = int(data[1])
    quran = json.loads(open("VIPMUSIC/assets/quran.json").read())["s"]
    keyboard = []
    list = []
    for i in range(0,10):
        if len(list) == 2:
            copy_list =list.copy()
            keyboard.append(copy_list)
            list.clear()
        name = quran[number]["sounds"][i]["name"]
        list.append(ikb(name, callback_data = f"runq-{number}-{i}"))
    keyboard.append(list)
    if number == 114:
        keyboard.append([ikb("‹ رجوع ›", callback_data = f"play-{number-1}")])
    elif number == 0:
        keyboard.append([ikb("‹ التالي ›", callback_data = f"play-{number+1}")])
    else:
        keyboard.append([ikb("‹ رجوع ›", callback_data = f"play-{number-1}"), ikb("‹ التالي ›", callback_data = f"play-{number+1}")])
    name_suarh = quran[number]["surah"]
    await cq.edit_message_text(f"**🥤| تم اختيار سورة {name_suarh} .\n🥤| قم باختيار الشيخ**", reply_markup = ikm(keyboard))

@app.on_callback_query(filters.regex("runq") & ~BANNED_USERS)
async def show_quran(c,cq):
    data = (cq.data.strip()).split("-")
    number = int(data[1])
    i = int(data[2])
    quran = json.loads(open("VIPMUSIC/assets/quran.json").read())["s"] 
    name = quran[number]["surah"]
    per_name = quran[number]["sounds"][i]["name"]
    file = requests.get(quran[number]["sounds"][i]["url"]).content
    open(f"{name}.mp3","wb").write(file)
    await app.send_audio(cq.message.chat.id,f"{name}.mp3",f"**🥤| سورة {name} بصوت الشيخ {per_name}**",reply_markup = ikm([[ikb("‹ تشغيل ›", callback_data=f"done-{number}-{i}")]]))


@app.on_callback_query(filters.regex("done") & ~BANNED_USERS)
async def show_quran(c,cq):
    data = (cq.data.strip()).split("-")
    number = int(data[1])
    i = int(data[2])
    quran = json.loads(open("VIPMUSIC/assets/quran.json").read())["s"]
    try:
        await VIP.join_call(cq.message.chat.id, cq.message.chat.id, quran[number]["sounds"][i]["url"], video=None)
        await cq.edit_message_reply_markup(ikm([[ikb("‹ ايقاف مؤقت ›", callback_data = f"ADMIN Pause|{cq.message.chat.id}"),ikb("‹ استئناف ›", callback_data=f"ADMIN Resume|{cq.message.chat.id}")],[ikb("‹ ايقاف ›", callback_data = f"ADMIN Stop|{cq.message.chat.id}")]]))
    except:
        await VIP.skip_stream(cq.message.chat.id, quran[number]["sounds"][i]["url"])
        await cq.edit_message_reply_markup(ikm([[ikb("‹ ايقاف مؤقت ›", callback_data = f"ADMIN Pause|{cq.message.chat.id}"),ikb("‹ استئناف ›", callback_data=f"ADMIN Resume|{cq.message.chat.id}")],[ikb("‹ ايقاف ›", callback_data = f"ADMIN Stop|{cq.message.chat.id}")]]))





@app.on_message(filters.command(["hmd"]))
async def start(client, message):
    await message.reply_text("مرحبًا! للبدء اختر الختمة.")

@app.on_message(filters.text & filters.private)
async def handle_message(client, message):
    text = message.text
    chat_id = message.chat.id
    msg_id = message.message_id

    if text == "الختمه" or text == "الختمة":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("البدء من جديد", callback_data="restart")],
            [InlineKeyboardButton("استئناف الختمه", callback_data="resume")]
        ])
        await message.reply_text("اختر احدى الازرار", reply_markup=keyboard)

@app.on_callback_query()
async def handle_callback(client, callback_query):
    data = callback_query.data
    chat_id = callback_query.message.chat.id
    msg_id = callback_query.message.message_id

    if data == "restart":
        readable = 0
        photo = "https://quran.ksu.edu.sa/png_big/1.png"
        caption = "الصفحه 1"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(" التالي ", callback_data="next")],
            [InlineKeyboardButton(" السابق ", callback_data="prev")]
        ])
        await bot.send_photo(chat_id, photo, caption=caption, reply_markup=keyboard)

    elif data == "next":
        readable += 1
        photo = f"https://quran.ksu.edu.sa/png_big/{readable}.png"
        caption = f'الصفحه {readable}'
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(" التالي ", callback_data="next")],
            [InlineKeyboardButton(" السابق ", callback_data="prev")]
        ])
        await bot.send_photo(chat_id, photo, caption=caption, reply_markup=keyboard)

    elif data == "prev":
        readable -= 1
        photo = f"https://quran.ksu.edu.sa/png_big/{readable}.png"
        caption = f'الصفحه {readable}'
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(" التالي ", callback_data="next")],
            [InlineKeyboardButton(" السابق ", callback_data="prev")]
        ])
        await bot.send_photo(chat_id, photo, caption=caption, reply_markup=keyboard)

    elif data == "resume":
        readable = 0
        photo = f"https://quran.ksu.edu.sa/png_big/{readable}.png"
        caption = f'الصفحه {readable}'
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(" التالي ", callback_data="next")],
            [InlineKeyboardButton(" السابق ", callback_data="prev")]
        ])
        await bot.send_photo(chat_id, photo, caption=caption, reply_markup=keyboard)

