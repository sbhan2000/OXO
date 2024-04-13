from VIPMUSIC import app
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from VIPMUSIC.utils.vip_ban import admin_filter
import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from VIPMUSIC.utils.database import get_assistant
from time import time
import asyncio
from VIPMUSIC.utils.extraction import extract_user
import config

from ..logging import LOGGER

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5



@app.on_chat_member_updated(filters.group, group=-2)
async def greet_new_members(_, member: ChatMemberUpdated):
    try:
        
        chat_id = member.chat.id
        userbot = await get_assistant(chat_id)
        count = await app.get_chat_members_count(chat_id)
        A = await wlcm.find_one(chat_id)
        if A:
            return

        user = member.new_chat_member.user if member.new_chat_member else member.from_user
        
        # Add the modified condition here
        if member.new_chat_member and not member.old_chat_member:
            welcome_text = f"""**Wᴇʟᴄᴏᴍᴇ** {user.mention}\n**@{user.username}**"""
            await asyncio.sleep(3) 
            await userbot.send_message(chat_id, text=welcome_text)
    except Exception as e:
       LOGGER.error(e)
    
