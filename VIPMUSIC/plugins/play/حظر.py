import asyncio, random, re
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ChatPermissions
from VIPMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from config import OWNER_ID
from VIPMUSIC.misc import SUDOERS as sudo
from VIPMUSIC.utils.database import (add_served_chat,
                                       is_served_chat,
                                       get_served_chats,
                                       add_served_user,
                                       get_served_users,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat,
                                       is_active_chat)


@app.on_message(filters.command(["الغاء حظرر"], "") & filters.group)
async def unbaneed(client, message):
    if not message.from_user.id in sudo:
     get = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not get.can_restrict_members: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if not message.reply_to_message: return await message.reply_text(f"**قم بالرد علي رساله**")
    user_id = message.reply_to_message.from_user.id
    try:
        await client.unban_chat_member(message.chat.id, user_id)
        await message.reply_text(f"**تم الغاء حظر هذه المستخدم**")
    except:
         return await message.reply_text(f"**فشل الغاء هذه المستخدم*")
@app.on_message(filters.command(["حظرر"], "") & filters.group)
async def baneed(client, message):
    if not message.from_user.id in sudo:
     get = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not get.can_restrict_members: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if not message.reply_to_message: return await message.reply_text(f"**قم بالرد علي رساله**")
    user_id = message.reply_to_message.from_user.id
    if user_id in sudo: return await message.reply_text(f"**لا يمكن حظر هذا المستخدم**")
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply_text(f"**تم حظر هذه المستخدم**")
    except:
         return await message.reply_text(f"**فشل حظر هذه المستخدم**")

@app.on_message(filters.command(["تقيدد"], "") & filters.group)
async def restrice(client, message):
    if not message.from_user.id in sudo:
     get = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not get.can_restrict_members: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if not message.reply_to_message: return await message.reply_text(f"**قم بالرد علي رساله**")
    user_id = message.reply_to_message.from_user.id
    if user_id in sudo: return await message.reply_text(f"**لا يمكن تقيد هذا المستخدم**")
    try:
        await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions())
        await message.reply_text(f"**تم تقيد هذه المستخدم**")
    except:
         return await message.reply_text(f"**فشل تقيد هذه المستخدم**")

@app.on_message(filters.command(["الغاء تقيدد"], "") & filters.group)
async def unrestrice(client, message):
    if not message.from_user.id in sudo:
     get = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not get.can_restrict_members: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if not message.reply_to_message: return await message.reply_text(f"**قم بالرد علي رساله**")
    user_id = message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions(can_send_messages=True))
        await message.reply_text(f"**تم الغاء تقيد هذه المستخدم**")
    except:
         return await message.reply_text(f"**فشل الغاء تقيد هذه المستخدم**")
mute = []

@app.on_message(filters.command(["كتمم"], "") & filters.group)
async def muted(client, message):
    if not message.from_user.id in sudo:
     get = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not get.can_restrict_members: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if not message.reply_to_message: return await message.reply_text(f"**قم بالرد علي رساله**")
    user_id = message.reply_to_message.from_user.id
    if user_id in sudo: return await message.reply_text(f"**لا يمكن كتم هذا المستخدم**")
    if not user_id in mute: mute.append(user_id)
    await message.reply_text(f"**تم كتم المستخدم**")


@app.on_message(filters.command(["الغاء كتمم"], "") & filters.group)
async def muted(client, message):
    if not message.from_user.id in sudo:
     get = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not get.can_restrict_members: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if not message.reply_to_message: return await message.reply_text(f"**قم بالرد علي رساله**")
    user_id = message.reply_to_message.from_user.id
    if user_id in mute: mute.remove(user_id)
    await message.reply_text(f"**تم الغاء كتم المستخدم**")



words = []
links = []
@app.on_message(filters.command(["قفلل الاسائه", "منع الاسائه"]) & ~filters.private)
async def loclkword(client: app, message):
    if not message.from_user.id in sudo:
     chek = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not chek.status in ["administrator", "creator"] : return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if not message.chat.id in words: words.append(message.chat.id)
    return await message.reply_text(f"**تم قفل الاسائه*")
@app.on_message(filters.command(["فتحح الاسائه"]) & ~filters.private)
async def openword(client: app, message):
    if not message.from_user.id in sudo:
     chek = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not chek.status in ["administrator", "creator"]: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if message.chat.id in words: words.remove(message.chat.id)
    return await message.reply_text(f"**تم فتح الاسائه*")

@app.on_message(filters.command(["قفلل الروابط", "منع الروابط"]) & ~filters.private)
async def loclklinks(client: app, message):
    if not message.from_user.id in sudo:
     chek = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not chek.status in ["administrator", "creator"]: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if not message.chat.id in links: links.append(message.chat.id)
    return await message.reply_text(f"**تم قفل الروابط*")
@app.on_message(filters.command(["فتحح الروابط"]) & ~filters.private)
async def openlinks(client: app, message):
    if not message.from_user.id in sudo:
     chek = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not chek.status in ["administrator", "creator"]: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if message.chat.id in links: links.remove(message.chat.id)
    return await message.reply_text(f"**تم فتح الروابط*")

@app.on_message(filters.command(["مسحح"]) & ~filters.private)
async def delmessage(client: app, message):
    if not message.from_user.id in sudo:
     chek = await client.get_chat_member(message.chat.id, message.from_user.id)
     if not chek.status in ["administrator", "creator"]: return await message.reply_text(f"**ليس لديك صلاحيات كافيه**")
    if message.reply_to_message:
       await message.delete()
       await message.reply_to_message.delete()
    else:
        return await message.reply_text(f"**قم بالرد علي رساله**")


@app.on_message(filters.command(["إذاعه"]) & ~filters.private)
async def openlinks(client: app, message):
    if not message.from_user.id in OWNER_ID: return
    if not message.reply_to_message: return await message.reply_text(f"**قم بالرد علي رساله**")
    chats = await get_served_chats()
    c = 0
    u = 0
    for chat in chats:
        try:
            await client.send_message(int(chat["chat_id"]), message.reply_to_message.text)
            c += 1
        except Exception as a:
             print(a)
    users = await get_served_users()
    for user in users:
        try:
            await client.send_message(int(user["user_id"]), message.reply_to_message.text)
            u += 1
        except Exception as a:
            print(a)
    await message.reply_text(f"تم الاذاعه الي {c} و {u} مستخدم")
@app.on_message(filters.command(["المطور", "ممطور"], ""))
async def dev(client: Client, message: Message):
     dev = OWNER_ID[0]
     user = await client.get_chat(chat_id=dev)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = await client.export_chat_invite_link(message.chat.id)
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور الأساسي**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))



array = []
@app.on_message(filters.command(["@all", "تاك","تاك للكل"]) & ~filters.private)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text("التاك قيد التشغيل حالياً ،")
  if not message.from_user.id in sudo:
   chek = await client.get_chat_member(message.chat.id, message.from_user.id)
   if not chek.status in ["administrator", "creator"]:
    await message.reply("يجب انت تكون مشرف لاستخدام الامر 🖱️")
    return
  await message.reply_text("جاري بدأ المنشن ، لايقاف الامر اضغط \n /cancel او اكتب بس منشن")
  i = 0
  txt = ""
  zz = message.text
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("نادي الكل","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.iter_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ،"
       if i == 5:
        try:
              await client.send_message(message.chat.id, f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except:
          pass
  array.remove(message.chat.id)


@app.on_message(filters.command(["بس المنشن", "/cancel","بس منشن"]))
async def stop(client, message):
  if not message.from_user.id in sudo:
   chek = await client.get_chat_member(message.chat.id, message.from_user.id)
   if not chek.status in ["administrator", "creator"]:
    await message.reply("**يجب انت تكون مشرف لاستخدام الامر 🖱️")
    return
  if message.chat.id not in array:
     await message.reply("المنشن متوقف بالفعل")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("تم ايقاف المنشن بنجاح✅")
    return


