import asyncio
import os
import time
import requests
import json
import urllib.parse
import urllib.request
import config
from pyrogram import filters
from pyrogram import Client
from VIPMUSIC import app
from pyrogram.types import Message, InlineKeyboardMarkup



bot = Client(
    "QuranPlaybot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

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

@bot.on_callback_query()
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

bot.run()
