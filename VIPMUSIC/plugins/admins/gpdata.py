from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from VIPMUSIC import app
from config import OWNER_ID
from VIPMUSIC.misc import SUDOERS
from pyrogram.types import Message
from VIPMUSIC.utils.vip_ban import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC.utils.database import add_served_chat, delete_served_chat

# ------------------------------------------------------------------------------- #


@app.on_message(filters.command(["تثبيت","ثبت","ث","ت"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & admin_filter & SUDOERS)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**🥤| يستخدم في المجموعات**")
    elif not replied:
        await message.reply_text("**🥤| قم بالرد على الرساله.**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**🥤| تم تثبيت الرساله بنجاح**\n\n**🥤| المجموعة :** {chat_title}\n**🥤| المشرف :** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" الـرساله ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("pinned"))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("**ɴᴏ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ ғᴏᴜɴᴅ**")
    try:        
        await message.reply_text("ʜᴇʀᴇ ɪs ᴛʜᴇ ʟᴀᴛᴇsᴛ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 ᴠɪᴇᴡ ᴍᴇssᴀɢᴇ",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["الغاء التثبيت","الغاء"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & admin_filter & SUDOERS)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**🥤| يستخدم في المجموعات.**")
    elif not replied:
        await message.reply_text("**🥤| قم بالرد على الرساله**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"**🥤| تم الغاء تثبيت الرساله بنجاح**\n\n**🥤| المجموعة :** {chat_title}\n**🥤| المشرف :** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" الـرساله  ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))



#------------------------------------------------------------------------------ #

@app.on_message(filters.command(["حذف صورة المجموعة","حذف صوره المجموعه","مسح الصوره","مسح الصورة","حذف الصوره","حذف الصورة","حذف بروفايل"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & admin_filter & SUDOERS)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**🥤| جاࢪي المعالجة....**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**🥤| يستخدم في المجموعات**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("**🥤| تم ازالة صورة المجموعة بنجاح\n\n🥤| بواسطة :** {}".format(message.from_user.mention))    
      except:
          await msg.edit("**🥤| امنحني جميع صلاحيات المشرف.**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["اضف بروفايل"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])& admin_filter & SUDOERS)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**🥤| جاࢪي المعالجة...**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**🥤| يستخدم في المجموعات.**") 
      elif not reply:
           await msg.edit("**🥤| قم بالرد على الصوره.**")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("**🥤| تم اضافة صورة المجموعة بنجاح\n\n🥤| بواسطة :** {}".format(message.from_user.mention))
             else:
                await msg.edit("**🥤| حدث حطأ حاول مرة اخرى.**")
     
          except:
              await msg.edit("**🥤| امنحني جميع صلاحيات المشرف.**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["اضف اسم","تغيير الاسم"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])& admin_filter & SUDOERS)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**🥤| جاࢪي المعالجة...**")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("**🥤| يستخدم في المجموعات.**")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**🥤| تم تغيير اسم المجموعة بنجاح\n\n🥤| بواسطة :** {}".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("**🥤| امنحني جميع صلاحيات المشرف.**")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**🥤| تم تغيير اسم المجموعة بنجاح\n\n🥤| بواسطة :** {}".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("**🥤| امنحني جميع صلاحيات المشرف.**")
          

    else:
       await msg.edit("**🥤| قم بالرد على الاسم او اكتبه مع الامر **")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command(["اضف وصف"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & admin_filter & SUDOERS)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**🥤| جاࢪي المعالجة...**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**🥤| يستخدم في المجموعات.**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**🥤| تم اضافة وصف المجموعة بنجاح**\n\n🥤| بواسطة : {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**🥤| امنحني جميع صلاحيات المشرف**")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**🥤| تم اضافة وصف المجموعة بنجاح**\n\n🥤| بواسطة : {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**🥤| امنحني جميع صلاحيات المشرف.**")
    else:
        await msg.edit("**🥤| قم بالرد على الوصف او اكتبه مع الامر.**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["بوت غادر"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & SUDOERS)
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**🥤| حاضر مطوري\n\n🥤| تم مغادرة البوت من المجموعة بنجاح.**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)
    await delete_served_chat(chat_id)


# --------------------------------------------------------------------------------- #

