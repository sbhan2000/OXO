import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from VIPMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from VIPMUSIC import app
from asyncio import gather
from pyrogram.errors import FloodWait
from config import OWNER_ID
from random import  choice, randint
import config 

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(
    filters.command(["المبرمج","حمد","مبرمج السورس","الـمبرمج"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
async def yas(client, message):
    usr = await client.get_chat("ah_2_v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"<b>⦗ الـمبرمج ⦘<b>\n<b>↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘<b>\n<b>↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘<b>\n<b>↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘<b>\n<b>↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘<b>",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )




@app.on_message(
    filters.command(["السورس","سورس","الـسورس"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
async def yas(client, message):
    usr = await client.get_chat("ah07v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"<b>𝘛𝘏𝘌 𝘉𝘌𝘚𝘛 𝘚𝘖𝘜𝘙𝘊𝘌 𝘖𝘕 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔<b>",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝚛𝚘𝚞𝚙", url=f"https://t.me/ah_1_v"
                    ),
                    InlineKeyboardButton(
                        "𝙲𝚑𝚊𝚗𝚗𝚎𝚕", url=f"https://t.me/ah07v"),
                ],
                [
                    InlineKeyboardButton(
                        "𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛", url=f"https://t.me/ah_2_v" )
                ],
            ]
        ),
    )
