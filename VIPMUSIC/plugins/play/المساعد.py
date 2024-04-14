import asyncio
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from VIPMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.utils.decorators.userbotjoin import UserbotWrapper
from VIPMUSIC.utils.database import get_assistant, is_active_chat
links = {}


@app.on_message(filters.group & filters.command(["userbotjoin", f"userbotjoin@{app.username}","انضم"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~filters.private)
async def join_group(client, message):
    chat_id = message.chat.id
    userbot = await get_assistant(message.chat.id)
    userbot_id = userbot.id
    done = await message.reply("**🥤| انتظر قليلا من فضلك وسوف ينضم الحساب المساعد الى المجموعه...**")
    await asyncio.sleep(1)
    # Get chat member object
    chat_member = await app.get_chat_member(chat_id, app.id)
    
    # Condition 1: Group username is present, bot is not admin
    if message.chat.username and not chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        try:
            await userbot.join_chat(message.chat.username)
            await done.edit_text("**🥤| تم انضمام الحساب المساعد بنجاح⚡♥**")
        except Exception as e:
            await done.edit_text("**🥤| امنحني جميع الصلاحيات المشرف لكي اقوم باضافة الحساب المساعد...**")
            

    # Condition 2: Group username is present, bot is admin, and Userbot is not banned
    if message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        try:
            await userbot.join_chat(message.chat.username)
            await done.edit_text("**🥤| تم انضمام الحساب المساعد بنجاح⚡♥**")
        except Exception as e:
            await done.edit_text(str(e))

    
    
    # Condition 3: Group username is not present/group is private, bot is admin and Userbot is banned
    if message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        userbot_member = await app.get_chat_member(chat_id, userbot.id)
        if userbot_member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED]:
            try:
                await app.unban_chat_member(chat_id, userbot.id)
                await done.edit_text("**🥤| الحساب المساعد محظور...**")
                await userbot.join_chat(message.chat.username)
                await done.edit_text("**🥤| قم بارالة الحساب المساعد من قائمة المحظورين وحاول مره اخرى**")
            except Exception as e:
                await done.edit_text("**🥤| من فضلك قم بازالة الحساب المساعد من قائمة المحظورين وامنح البوت جميع الصلاحيات وحاول مرة اخرى.**")
        return
    
    # Condition 4: Group username is not present/group is private, bot is not admin
    if not message.chat.username and not chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        await done.edit_text("**🥤| ارفعني مشرف في المجموعه لاستطيع اضافة الحساب المساعد.**")
        


    # Condition 5: Group username is not present/group is private, bot is admin
    if not message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        try:
            try:
                userbot_member = await app.get_chat_member(chat_id, userbot.id)
                if userbot_member.status not in [ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED]:
                    await done.edit_text("**🥤| الحساب المساعد موجود بالفعل.**")
                    return
            except Exception as e:
                await done.edit_text("**🥤| انتظر قليلا لاضافة الحساب المساعد.**")
                await done.edit_text("**🥤| انتظر قليلا لاضافة الحساب المساعد.**")
                invite_link = await app.create_chat_invite_link(chat_id, expire_date=None)
                await asyncio.sleep(2)
                await userbot.join_chat(invite_link.invite_link)
                await done.edit_text("**🥤| تم انضمام الحساب المساعد بنجاح.**")
        except Exception as e:
            await done.edit_text(f"**🥤| الحساب المساعد غير موجود في المجموعه وغير قادر على اضافته\n امنحني جميع الصلاحيات وحاول مرة اخرى.**")

    
    
    # Condition 6: Group username is not present/group is private, bot is admin and Userbot is banned
    if not message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        userbot_member = await app.get_chat_member(chat_id, userbot.id)
        if userbot_member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED]:
            try:
                await app.unban_chat_member(chat_id, userbot.id)
                await done.edit_text("**🥤|; الحساب المساعد محظر ارفع الحظر عنه وحاول مره اخرى..**")
                invite_link = await app.create_chat_invite_link(chat_id, expire_date=None)
                await asyncio.sleep(2)
                await userbot.join_chat(invite_link.invite_link)
                await done.edit_text("**🥤| الحساب المسعد محظر ارفع الحظر وسوف ينضم للمجموعه**")
            except Exception as e:
                await done.edit_text(f"**🥤| الحساب المساعد غير موجود في المجموعه وغير قادر على اضافته\n امنحني جميع الصلاحيات وحاول مرة اخرى.**")
        return
    
    
    


        
@app.on_message(filters.command(["userbotleave","غادر"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group & admin_filter)
async def leave_one(client, message):
    try:
        userbot = await get_assistant(message.chat.id)
        await userbot.leave_chat(message.chat.id)
        await app.send_message(message.chat.id, "**🥤| غادر الحساب المساعد بنجاح.**")
    except Exception as e:
        print(e)


@app.on_message(filters.command(["leaveall", f"leaveall@{app.username}","مغادره"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("**🥤| تم المغادره بنجاح...**")
    try:
        userbot = await get_assistant(message.chat.id)
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001420714100:
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"**🥤| جاࢪي المغاده من كل المجموعات...**\n\n**🥤| النجاح:** {left} مجموعه.\n**🥤| الفشل:** {failed} مجموعه.**"
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"**🥤| جاࢪي المغادره من كل المجموعات...**\n\n**🥤| النجاح:** {left} مجموعه.\n**🥤| الفشل:** {failed} مجموعه.**"
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id, f"**🥤| تم المغادره من:* {left} chats.\n**🥤| تم فشل المغادره من:** {failed} مجموعه.**"
        )
