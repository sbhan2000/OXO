import asyncio
from config import OWNER_ID
import redis, re
from pyrogram import *
from dotenv import load_dotenv
from os import getenv
from VIPMUSIC import app
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid


bot_id = app.bot_token.split(":")[0]

# create a Redis client
r = redis.Redis(
  host='redis-13524.c84.us-east-1-2.ec2.cloud.redislabs.com',
  port=13524,
  password='J2tSRdAbiuSaFU3ROH2UqWWTahWR00b9')


Keyard = ReplyKeyboardMarkup(
  [
    [("《صنع بوت》"),("《حذف بوت》")],
    [("《صنع جلسه》")],
    [("《السورس》"),("《مطور السورس》")],
    [("الغاء")]
  ],
  resize_keyboard=True
)


Keyboard = ReplyKeyboardMarkup(
  [
    [("《قسم الاذاعه》")],
    [("《قسم الحساب المساعد》")],
    [("《قسم الادمنيه》"), ("《قسم الكولات》")],
    [("《معلومات السيرفر》"), ("《فحص سرعه البوت》")],
    [("المحظورين عام🚨"), ("المحظورين ميوزك❌")],
    [("《الاحصائيات والتواصل》")],
    [("《قسم الاشتراك الاجباري》")],
    [("نقل ملكية البوت")],
    [("《قسم النسخه الاحتياطيه》")],
    [("《قسم السورس》")],
    [("《تنظيف》"), ("《الغاء》")],
    [("《قفل الكيبورد🔒》")],
  ],
  resize_keyboard=True
)

@app.on_message(filters.command(["/hmd"], ""))
async def for_users (app,m):
   if check(m.from_user.id):
     kep = ReplyKeyboardMarkup([["《صنع بوت》", "《حذف بوت》"], ["البوتات المصنوعه"], ["تعطيل المجاني", "تفعيل المجاني"], ["تعطيل التواصل", "تفعيل التواصل"], ["السورس"], ["الغاء"]], resize_keyboard=True)
     return await m.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""[ ●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━● •](https://t.me/UIU_II)\n\n**اهـلا يـنـجـم.؟ **\n**مـرحبآ بـك انــا بــوت اقـوم بــتـشـغـيـل الاغــانــي فـي الـمـڪـالـمـه الـصـوتـية .🤔❤**\n**يمكنني التشغيل بصوت رائع وبدون اي مشاكل او تقطيع في الاغنيه**\n**اضفني الى مجموعتك وارفعني رول بشڪل مع ڪامل الصلاحيات صحيح**\n**لمعرفة استخدامي بشڪل صحيح اضغط علي زر الاوامر. 🤔💕**\n
اضغط(/sezar)لاظهار كيب المطور ✨
[ ●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━● •](https://t.me/UIU_II)""", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطور السورس. ⚡", url=f"https://t.me/c_a_s_e_r_h"),
            ],[
                    InlineKeyboardButton(
                        "قناة السورس⚡", url=f"https://t.me/UIU_II"),
            ],[
                    InlineKeyboardButton(
                        " اضغط هنا لاضافتي الي مجموعتك🤖", url=f"https://t.me/SILA_11bot?startgroup=true"),
            ], 
            ]
        ),
    )
    
   kep = ReplyKeyboardMarkup([["《مطور البوت》", "《مطور السورس》"], ["《اضافه البوت لمجموعتك》"], ["《السورس》", "《جروب السورس》"], ["✨بنك قيصر", "⋖━❲𖣂❳━⋗", "✨ابراج"], ["✨ازكار", "⋖━❲𖣂❳━⋗", "✨اسال"], ["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"], ["زخرفه", "⋖━❲𖣂❳━⋗", "✨زخارف"], ["✨حكمه", "⋖━❲𖣂❳━⋗", "✨معلومات"], ["✨العاب", "⋖━❲𖣂❳━⋗", "✨اغاني"], ["✨مهنتي", "⋖━❲𖣂❳━⋗", "✨افلام"], ["✨كت", "⋖━❲𖣂❳━⋗", "✨تويت"], ["✨رايك بصورتي", "⋖━❲𖣂❳━⋗", "✨حساب العمر"], ["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"], ["✨حذف حسابي", "⋖━❲𖣂❳━⋗", "✨انصحني"], ["✨مميزات", "⋖━❲𖣂❳━⋗", "✨بوت"], ["✨نكته", "⋖━❲𖣂❳━⋗", "✨حروف"], ["✨صوره", "⋖━❲𖣂❳━⋗", "✨غنيلي"], ["✨انمي", "⋖━❲𖣂❳━⋗", "✨متحركه"], ["✨اقتباسات", "⋖━❲𖣂❳━⋗", "✨هيدرات"], ["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"], ["✨صور بنات", "⋖━❲𖣂❳━⋗", "✨صور شباب"], ["✨قران", "⋖━❲𖣂❳━⋗", "✨الشيخ نقشبندي"], ["✨استوريهات", "⋖━❲𖣂❳━⋗", "✨فيلم"], ["✨ايدي", "⋖━❲𖣂❳━⋗", "✨خيرني"], ["🥺 ¦ حذف الكيبورد"]], resize_keyboard=True)
   await m.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""[ ●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━● •](https://t.me/UIU_II)\n\n**اهـلا يـنـجـم.؟ **\n**مـرحبآ بـك انــا بــوت اقـوم بــتـشـغـيـل الاغــانــي فـي الـمـڪـالـمـه الـصـوتـية .🤔❤**\n**يمكنني التشغيل بصوت رائع وبدون اي مشاكل او تقطيع في الاغنيه**\n**اضفني الى مجموعتك وارفعني رول بشڪل مع ڪامل الصلاحيات صحيح**\n**لمعرفة استخدامي بشڪل صحيح اضغط علي زر الاوامر. 🤔💕**\n
اضغط(/sezar)لاظهار كيب المطور والاعضاء✨
[ ●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━● •](https://t.me/UIU_II)""", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطور السورس. ⚡", url=f"https://t.me/c_a_s_e_r_h"),
            ],[
                    InlineKeyboardButton(
                        "قناة السورس⚡", url=f"https://t.me/UIU_II"),
            ],[
                    InlineKeyboardButton(
                        " اضغط هنا لاضافتي الي مجموعتك🤖", url=f"https://t.me/SILA_11bot?startgroup=true"),
            ], 
            ]
        ),
    )
   await m.reply_text(f"صلي علي النبي وتبسم✨🌺", reply_markup=kep)
   if not check(m.from_user.id):
     await check_sub(app, m)
   if not is_user(m.from_user.id):
     add_user(m.from_user.id)
     text = '🙍 شخص جديد دخل الى البوت !\n\n'
     text += f'🎯 الأسم: {m.from_user.first_name}\n'
     text += f'♻️ الايدي: {m.from_user.id}\n\n'
     text += f'🌐 اصبح عدد المستخدمين: {len(get_users())}'
     reply_markup=InlineKeyboardMarkup (
      [[
        InlineKeyboardButton (m.from_user.first_name, user_id=m.from_user.id)
      ]]
     )
     if len(get_admins()) > 0:
        list = get_admins()
        for admin in list:
          await app.send_message(int(admin), text, reply_markup=reply_markup)
        await app.send_message(int(r.get(f"bot_owner{bot_id}")), text, reply_markup=reply_markup)
     else:
        await app.send_message(int(r.get(f"bot_owner{bot_id}")), text, reply_markup=reply_markup)
     
     
@app.on_message(filters.command(["/hamd"], ""))
async def for_users (app,m):
   if check(m.from_user.id):
     kep = ReplyKeyboardMarkup([["《صنع بوت》", "《حذف بوت》"], ["البوتات المصنوعه"], ["تعطيل المجاني", "تفعيل المجاني"], ["تعطيل التواصل", "تفعيل التواصل"], ["السورس"], ["الغاء"]], resize_keyboard=True)
     return await m.reply_text(f"╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي  ⁽ {m.from_user.mention} ₎\n│⎋ اليك كيب التحكم بالبوت✨", reply_markup=Keyboard)
   kep = ReplyKeyboardMarkup([["✨بنك قيصر", "⋖━❲𖣂❳━⋗", "✨ابراج"], ["✨ازكار", "⋖━❲𖣂❳━⋗", "✨اسال"], ["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"], ["زخرفه", "⋖━❲𖣂❳━⋗", "✨زخارف"], ["✨حكمه", "⋖━❲𖣂❳━⋗", "✨معلومات"], ["✨العاب", "⋖━❲𖣂❳━⋗", "✨اغاني"], ["✨مهنتي", "⋖━❲𖣂❳━⋗", "✨افلام"], ["✨كت", "⋖━❲𖣂❳━⋗", "✨تويت"], ["✨رايك بصورتي", "⋖━❲𖣂❳━⋗", "✨حساب العمر"], ["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"], ["✨حذف حسابي", "⋖━❲𖣂❳━⋗", "✨انصحني"], ["✨مميزات", "⋖━❲𖣂❳━⋗", "✨بوت"], ["✨نكته", "⋖━❲𖣂❳━⋗", "✨حروف"], ["✨صوره", "⋖━❲𖣂❳━⋗", "✨غنيلي"], ["✨انمي", "⋖━❲𖣂❳━⋗", "✨متحركه"], ["✨اقتباسات", "⋖━❲𖣂❳━⋗", "✨هيدرات"], ["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"], ["✨صور بنات", "⋖━❲𖣂❳━⋗", "✨صور شباب"], ["✨قران", "⋖━❲𖣂❳━⋗", "✨الشيخ نقشبندي"], ["✨استوريهات", "⋖━❲𖣂❳━⋗", "✨فيلم"], ["✨ايدي", "⋖━❲𖣂❳━⋗", "✨خيرني"], ["🥺 ¦ حذف الكيبورد"]], resize_keyboard=True)
   await m.reply_text(f"╮⦿ اهـلا بڪ عزيـزي ⁽ {m.from_user.mention} ₎\n│⎋ ✦مرحبا بك عزيزي في كيبور اعضاء بوتات ميوزك سورس قيصر ✨", reply_markup=keep)
   

@app.on_message(filters.command("ahmed") & filters.private, group=1)
async def keyboard_show(app,m):
    if check(m.from_user.id):
       await m.reply(f"• أهلا بك {m.from_user.mention} .\n• اليك لوحة التحكم الخاصة", reply_markup=Keyboard, quote=True)

admins_commands = [
   '《الاحصائيات》', '《تفعيل التواصل》',
   '《تعطيل التواصل》', '《اذاعة بالتثبيت》', '《اذاعة》',
   '《اذاعة بالتوجيه》', '《تفعيل الاشتراك》', '《تعطيل الاشتراك》',
   '《ضع قناة الاشتراك》', '《حذف قناة الاشتراك》', '《قناة الاشتراك》','قائمه الأدمنيه',
   'المستخدمين', 'الأدمنية', 'الجروبات',
   '《اذاعة بالمجموعات》','《اذاعة بالتثبيت بالمجموعات》', 'اخفاء الكيبورد'
   ]
   
owner_commands = [
   'نقل ملكية البوت', 'رفع ادمن', 'تنزيل ادمن'
]

@app.on_message(filters.text & filters.private, group=2)
async def keyboardforadmins(app, m):
  if m.text in admins_commands:
    if not check(m.from_user.id):
      return await m.reply('🌀 هذا الأمر لا يخصك', quote=True)
    else:
    
      if m.text == '《الاحصائيات》':
        text = f'**👤 عدد المستخدمين: {len(get_users())}\n'
        text += f'📊 عدد المجموعات: {len(get_groups())}\n'
        text += f'🌀 عدد المشرفين: {len(get_admins())}**'
        await m.reply(text, quote=True)
        
      if m.text == '《تفعيل التواصل》':
        if r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تفعيل التواصل مسبقاً", quote=True)
          
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل التواصل بنجاح**', quote=True)
        r.set(f'enable_twasol{bot_id}', 1)
      
      if m.text == '《تعطيل التواصل》':
        if not r.get(f'enable_twasol{bot_id}'):
          return await m.reply("• تم تعطيل التواصل مسبقاً", quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل التواصل بنجاح**', quote=True)
        r.delete(f'enable_twasol{bot_id}')
      
      if m.text == 'المستخدمين':
        await m.reply_document(get_users_backup(), quote=True)
      
      if m.text == 'الأدمنية':
        await m.reply_document(get_admins_backup(), quote=True)
      
      if m.text == 'الجروبات':
        await m.reply_document(get_groups_backup(), quote=True)
      
      if m.text == '《تفعيل الاشتراك》':
        if r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تفعيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تفعيل الاشتراك بنجاح**', quote=True) 
        r.set(f"enable_force_subscribe{bot_id}", 1)
      
      if m.text == '《تعطيل الاشتراك》':
        if not r.get(f"enable_force_subscribe{bot_id}"):
          return await m.reply('• تم تعطيل الاشتراك الاجباري مسبقاً',quote=True)
        await m.reply(f'**• بواسطة ⟨ {m.from_user.mention} ⟩\n• تم تعطيل الاشتراك بنجاح**', quote=True) 
        r.delete(f"enable_force_subscribe{bot_id}")
      
      if m.text == '《ضع قناة الاشتراك》':
        await m.reply("• ارسل معرف القناة العام مثال @UIU_II", quote=True)
        r.set(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
      
      if m.text == '《حذف قناة الاشتراك》':
        if not r.get(f'force_channel{bot_id}'):
          return await m.reply("• لا توجد قناة اشتراك معينة", quote=True)
        await m.reply("• تم حذف قناة الاشتراك بنجاح", quote=True)
        r.delete(f'force_channel{bot_id}')
      
      if m.text == '《قناة الاشتراك》':
        if not r.get(f'force_channel{bot_id}'):
          await m.reply('• لاتوجد قناة مضافة', quote=True)
        else:
          channel = r.get(f'force_channel{bot_id}').decode('utf-8')
          await m.reply(f"https://t.me/{channel}", quote=True)
      
      if m.text == 'قائمه الأدمنيه':
        if len(get_admins()) == 0:
          await m.reply("• لايوجد آدمنية", quote=True)
        else:
          text = '• قائمة الأدمنية\n'
          for admin in get_admins():
            try:
              get = await app.get_chat(int(admin))
              text += f'• [{get.first_name}](tg://user?id={admin})\n'
            except:
              text += f'• [@UIU_II](tg://user?id={admin})\n'
          await m.reply(text, quote=True)
          
      if m.text == '《اذاعة》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == '《اذاعة بالتثبيت》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
        
      if m.text == '《اذاعة بالتوجيه》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == '《اذاعة بالمجموعات》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == '《اذاعة بالتثبيت بالمجموعات》':
        await m.reply("• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )",quote=True)
        r.set(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}",1)
        r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
        r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
      
      if m.text == 'اخفاء الكيبورد':
        await m.reply("• تم اخفاء لوحة التحكم لاظهارها مجدداً ارسل /start",
        quote=True, reply_markup=ReplyKeyboardRemove (selective=True))


@app.on_message(filters.text & filters.private, group=3)
async def for_owner(app,m):
  text = m.text
  if text in owner_commands:
   if not m.from_user.id == int(r.get(f"bot_owner{bot_id}")):
      return await m.reply("• هذا الأمر يخص المطور الأساسي فقط", quote=True)
   
   if text == 'نقل ملكية البوت':
     await m.reply("• ارسل ايدي المالك الجديد الآن", quote=True)
     r.set(f"{m.from_user.id}transfer{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
   if text == 'رفع ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}",1)
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
   
   if text == 'تنزيل ادمن':
     await m.reply("• ارسل ايدي الآدمن الآن", quote=True)
     r.set(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}", 1)
     r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
     r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")

@app.on_message(filters.text & filters.private, group=4)
async def response_for_commands(app,m):
   text = m.text
   
   if text in admins_commands:
     return

   if text in owner_commands:
     return 
     
   if check(m.from_user.id):
     if text == '《الغاء》':
       await m.reply("• تم الغاء كل شيء", quote=True)
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
       
     
     if r.get(f"{m.from_user.id}transfer{m.chat.id}{bot_id}"):
       try:
         get = await app.get_chat(int(text))
       except:
         return await m.reply("• الآيدي خطأ أرسل آيدي آخر او تأكد ان المستخدم مو حاظر البوت", quote=True)
       r.delete(f"{m.from_user.id}transfer{m.chat.id}{bot_id}")
       txt = '• تم نقل ملكية البوت بنجاح إلى :\n\n'
       txt += f'• الأسم : {get.first_name}\n'
       txt += f'• الآيدي : {get.id}\n'
       if get.username:
         txt += f'• اليوزر : @{get.username}\n'
       if get.bio:
         txt += f'• البايو : {get.bio}\n'
       r.set(f"bot_owner{bot_id}", get.id)
       await m.reply(txt, quote=True)
       return
     
     if r.get(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}"):
       try:
         get = await app.get_chat(int(text))
       except:
         return await m.reply("• الآيدي خطأ أرسل آيدي آخر او تأكد ان المستخدم مو حاظر البوت", quote=True)
         
       if is_admin(int(text)):
         r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
         return await m.reply(f"• المستخدم [{get.first_name}]({get.id}) ادمن من قبل")
       r.delete(f"{m.from_user.id}addadmin{m.chat.id}{bot_id}")
       txt = '• تم رفع المستخدم ادمن بنجاح :\n\n'
       txt += f'• الأسم : {get.first_name}\n'
       txt += f'• الآيدي : {get.id}\n'
       if get.username:
         txt += f'• اليوزر : @{get.username}\n'
       if get.bio:
         txt += f'• البايو : {get.bio}\n'
       add_admin(int(text))
       await m.reply(txt, quote=True)
       return 
     
     if r.get(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}"):
      try: 
       if not is_admin(int(text)):
         r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
         return await m.reply("• المستخدم مو ادمن من قبل")
       r.delete(f"{m.from_user.id}deladmin{m.chat.id}{bot_id}")
       del_admin(int(text))
       await m.reply("• تم تنزيل المستخدم ادمن بنجاح", quote=True)
       return 
      except:
       return await m.reply("• الآيدي خطأ")
     
     if r.get(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}"):
       channel = text.replace("@","")
       r.set(f"force_channel{bot_id}", channel)
       r.delete(f"{m.from_user.id}addchannel{m.chat.id}{bot_id}")
       await m.reply("• تم تعيين القناة بنجاح ", quote=True)
   
       
@app.on_message(filters.new_chat_members, group=6)
async def add_group(app,m):
  get = await app.get_me()
  for mm in m.new_chat_members:
    if mm.id == get.id:
      if not is_group(m.chat.id):
        add_group(m.chat.id)
        text = '• تم اضافة البوت الى مجموعة جديدة\n'
        text += f'• اسم المجموعه: {m.chat.title}\n'
        if m.chat.username:
          text += f'• رابط المجموعة: https://t.me/{m.chat.username}\n'
        text += '\n• معلومات الي ضافني :\n'
        text += f'• اسمه : {m.from_user.mention}\n'
        text += f'• الايدي : {m.from_user.id}\n'
        text += f'\n• عدد الجروبات الآن : {len(get_groups())}'
        if len(get_admins()) > 0:
          list = get_admins()
          for admin in list:
            await app.send_message(int(admin), text,
            disable_web_page_preview=True)
          await app.send_message(int(r.get(f"bot_owner{bot_id}")), text,
          disable_web_page_preview=True)
        else:
          await app.send_message(int(r.get(f"bot_owner{bot_id}")), text,
          disable_web_page_preview=True)

@app.on_raw_update(group=7)
async def kick_from_group(app: Client, m: Update, _, __):
   try:
     name = re.search(r"first_name='([^']+)'", str(_)).group(1)
     title = re.search(r"title='([^']+)'", str(__)).group(1)
     if m.new_participant:
      get = await app.get_me()
      if m.new_participant.peer.user_id == get.id:
        print("🌀")
      else:  return 
      if m.new_participant.kicked_by:
        print("🌀")
      del_group(int(f'-100{m.channel_id}'))
      text = '• تم طرد البوت من مجموعة:\n\n'
      text += f'• اسم الي طردني : [{name}](tg://user?id={m.new_participant.kicked_by})\n'
      text += f'• ايدي الي طردني : {m.new_participant.kicked_by}\n'
      text += f'\n• معلومات المجموعة: \n'
      text += f'\n• ايدي المجموعة: `-100{m.channel_id}`'
      text += f'\n• اسم المجموعه: {title}'
      text += '\n• تم مسح جميع بيانات الجروب'
      if len(get_admins()) > 0:
          list = get_admins()
          for admin in list:
            await app.send_message(int(admin), text,
            disable_web_page_preview=True)
          await app.send_message(int(r.get(f"bot_owner{bot_id}")), text,
          disable_web_page_preview=True)
      else:
          await app.send_message(int(r.get(f"bot_owner{bot_id}")), text,
          disable_web_page_preview=True)
   except:
     pass
      

@app.on_message(filters.private, group=8)
async def forbroacasts(app,m):
   if m.text:
      if m.text in admins_commands:  return
      if m.text in owner_commands:  return 
   if m.from_user:
     if r.get(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcast{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_users():
          try:
            await m.copy(int(user))
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_users():
          try:
            a = await m.copy(int(user))
            await a.pin(disable_notification=False,both_sides=True)
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception as e:
            print(e)
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}broadcastfor{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for user in get_users():
          try:
            await m.forward(int(user))
          except PeerIdInvalid:
            del_user(int(user))
            pass
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
     
     if r.get(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroad{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups():
          try:
            await m.copy(int(group))
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")
       
     
     if r.get(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}"):
       r.delete(f"{m.from_user.id}gbroadpin{m.chat.id}{bot_id}")
       rep = await m.reply("• جاري الإذاعة ..", quote=True)
       for group in get_groups():
          try:
            a = await m.copy(int(group))
            await a.pin(disable_notification=False)
          except Exception:
            pass
       await rep.edit("• تمت الاذاعة بنجاح")

@app.on_message(filters.private, group=9)
async def twasol__(app,m):
   if not check(m.from_user.id):
     if r.get(f'enable_twasol{bot_id}'):
       await m.forward(int(r.get(f"bot_owner{bot_id}")))
   
   if m.from_user.id == int(r.get(f"bot_owner{bot_id}")):
      if m.reply_to_message:
        if m.reply_to_message.forward_from:
          await m.reply(f"• تم إرسال رسالتك إلى {m.reply_to_message.forward_from.first_name} بنجاح", quote=True)
          try:
            await m.copy(m.reply_to_message.forward_from.id)
          except:
            pass
      

@app.on_message(filters.text & filters.group , group=10)
async def for_admins_in_group(app,m):
   if not m.reply_to_message:
      return
   if not m.reply_to_message.from_user:
      return
      
   if m.from_user.id == int(r.get(f"bot_owner{bot_id}")):
     text = m.text
     user_id = m.reply_to_message.from_user.id
     if text == 'رفع ادمن':
       if is_admin(user_id):
          return await m.reply("• المستخدم آدمن من قبل")
       else:
          add_admin(user_id)
          await m.reply("• تم رفعه ادمن بنجاح")
     
     if text == 'تنزيل ادمن':
      if not is_admin(user_id):
          return await m.reply("• المستخدم مو آدمن من قبل")
      else:
          del_admin(user_id)
          await m.reply("• تم تنزيله ادمن بنجاح")

def add_user(user_id: int):
	if is_user(user_id):
		return
	r.sadd(f"botusers{bot_id}", user_id)
	
def is_user(user_id: int):
  try:
    a= get_users()
    if user_id in a:
      return True
    return False
  except:
    return False

def del_user(user_id: int):
	if not is_user(user_id):
		return False
	r.srem(f"botusers{bot_id}", user_id)
	return True

def get_users():
   try:
     list = []
     for a in r.smembers(f"botusers{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_users_backup() -> str:
	text = ''
	for user in r.smembers(f"botusers{bot_id}"):
		text += user.decode('utf-8')+'\n'
	with open('users.txt', 'w+') as f:
		f.write(text)
	return 'users.txt'
	
def add_admin(user_id: int):
    if is_admin(user_id):  return 
    r.sadd(f"botadmins{bot_id}", user_id)

def is_admin(user_id: int):
  try:
    a = get_admins()
    if user_id in a:
      return True
    return False
  except:
    return False

def del_admin(user_id: int):
	if not is_admin(user_id):
		return False
	r.srem(f"botadmins{bot_id}", user_id)
	
def get_admins():
   try:
     list = []
     for a in r.smembers(f"botadmins{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_admins_backup() -> str:
	text = ''
	for admin in r.smembers(f"botadmins{bot_id}"):
		text += admin.decode('utf-8')+'\n'
	with open('admins.txt', 'w+') as f:
		f.write(text)
	return 'admins.txt'
	

def check(id):
    if is_admin(id):
      return True
    if id == int(r.get(f"bot_owner{bot_id}")):
      return True
    else:
      return False

async def check_sub(c,m):
    if not r.get(f"enable_force_subscribe{bot_id}"):
      return
    else:
      if not r.get(f"force_channel{bot_id}"):
        return 
      else:
        channel = r.get(f"force_channel{bot_id}").decode('utf-8')
        text = f'✖️ عذراً عليك الاشتراك بقناة البوت أولاً لتتمكن من استخدامه !\n\nhttps://t.me/{channel}\n- /start'
        try:
           get = await c.get_chat_member(r.get(f"force_channel{bot_id}").decode('utf-8'), m.from_user.id)
           if get.status in [enums.ChatMemberStatus.LEFT, enums.ChatMemberStatus.BANNED]:
             return await m.reply(text, quote=True, disable_web_page_preview=True)
        except:
           return await m.reply(text, quote=True, disable_web_page_preview=True)

def add_group(chat_id: int):
    if is_group(chat_id):  return 
    r.sadd(f"botgroups{bot_id}", chat_id)

def is_group(chat_id: int):
  try:
    a = get_groups()
    if chat_id in a:
      return True 
    return False 
  except:
    return False

def del_group(chat_id: int):
	if not is_group(chat_id):
		return False
	r.srem(f"botgroups{bot_id}", chat_id)

def get_groups():
   try:
     list = []
     for a in r.smembers(f"botgroups{bot_id}"):
        list.append(int(a.decode('utf-8')))
     return list
   except:
     return []

def get_groups_backup() -> str:
	text = ''
	for group in r.smembers(f"botgroups{bot_id}"):
		text += group.decode('utf-8')+'\n'
	with open('groups.txt', 'w+') as f:
		f.write(text)
	return 'groups.txt'

if not r.get(f"bot_owner{bot_id}"):
   owner = int(getenv("OWNER_ID", ""))
   r.set(f"bot_owner{bot_id}", owner)


@app.on_message(filters.command(["✨حذف حسابي"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/50228546bd85a32fecd6e.jpg",
        caption=f"""**اتفضل احذف او احذفي مع الف سلامه بس خد بالك او خدي بالك اتوحشني والله😂**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "رابط الحذف🗑", url=f"https://t.me/LC6BOT"),
            ],
            ]
        ),
    )
   
@app.on_message(filters.command(["✨ايدي"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ae23083044ace5c97ff9a.jpg",
        caption=f"""لروية الايدي الخاص بك اضغط علي الزر في الاسفل وانضم الي الجروب وثم اكتب في الجروب (ايدي) ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "رابط الجروب ✨", url=f"https://t.me/sorescaser"),
            ],
            ]
        ),
    )
    
@app.on_message(filters.command(["⋖━❲𖣂❳━⋗"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""صلي علي النبي وتبسم ✨💖""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗘𝗭𝗔𝗥", url=f"https://t.me/UIU_II"),
            ],
            ]
        ),
    )
    
@app.on_message(filters.command(["●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""صلي علي النبي وتبسم ✨💖""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗘𝗭𝗔𝗥", url=f"https://t.me/UIU_II"),
            ],
            ]
        ),
    )
    
@app.on_message(filters.command(["《اضافه البوت لمجموعتك》"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
        caption=f"""قم باضافتي لمجوموعتك لتشغيل الموسيقي والفديو في المحادثه الصوتيه انا من اسرع البوتات التي تستطيع تشغيل الاغاني تم تنصيبي في افضل سورس في التلجرام سورس القيصر قناه السورس @UIU_II""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " اضغط هنا لاضافتي الي مجموعتك", url=f"https://t.me/SILA_11bot?startgroup=true"),
            ],
            ]
        ),
    )
    
@app.on_message(filters.command(["🥺 ¦ حذف الكيبورد"], ""))
async def ahmed(_, message: Message): 
    await message.reply_text(
        text="""جتك قفله في دماغك 🥺""",            
  reply_markup=ReplyKeyboardRemove()
    )
