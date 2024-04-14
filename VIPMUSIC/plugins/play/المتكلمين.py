from pyrogram import filters, Client
from VIPMUSIC import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from VIPMUSIC.core.call import VIP 
from VIPMUSIC.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)

@app.on_message(filters.regex(["المتكلمين"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def strcall(client, message):
    assistant = await group_assistant(VIP,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./strings/call.mp3"), stream_type=StreamType().pulse_stream)
        text="**🥤| الاعضاء المتواجدين في المكالمة المرئية :**\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="**يتكلم*""
            else:
                mut="**لا يتكلم**"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}:{user.mention}↬{mut}\n"
        text += f"\n**🥤| عدد الاشخاص في المكالمة المرئية {len(participants)} **"    
        await message.reply(f"{text}")
        await asyncio.sleep(5)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"**🥤| لا يوجد اتصال.**")
    except TelegramServerError:
        await message.reply(f"**🥤| ارسل مرة اخرى يوجد خطأ في احد سيرفرات التليكرام**")
