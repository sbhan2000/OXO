import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from typing import Union
from VIPMUSIC import app
import re
import sys
import config



GAME_MESSAGE = "**🥤| مرحبا بك عزيزي:\n🥤| في قسم العاب اختر ما تريد:: **"
GAME_BUTTONS = [
    [ 
        InlineKeyboardButton ('اللعاب المتطورة', callback_data= 'GAME1'),
        InlineKeyboardButton ('اللعاب البوت', callback_data= 'GAME2'),
        ],[
        InlineKeyboardButton ('‹ قـناة الـبوت ›', url=config.SUPPORT_CHANNEL)              
                 ],[
                InlineKeyboardButton(
                        "◍ اغلاق 🌐", callback_data="close"),
               ],
          ]
    

nmla = []

@app.on_message(filters.command("رفع نمله"))
async def rf3nmla(client, message):
  if not message.reply_to_message.from_user.mention in nmla:
    nmla.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**🥤| تم رفع العضو نملهn\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل نمله"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in nmla:
    nmla.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("المرفوعين نمل"))
async def nml(client, message):
  nq = ""
  for n in nmla:
      nq += n + "\n"
  await message.reply_text(nq)





@app.on_message(filters.command("رفع صرصار"))
async def rf3srsar(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو صرصار\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل صرصار"))
async def tnzelsrar(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("رفع رقاصه"))
async def yasooo(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو رقاصه\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل رقاصه"))
async def yaso(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
  
@app.on_message(filters.command("رفع نجس"))
async def fdsa(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو نجس\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل نجس"))
async def kophvc(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع كلب"))
async def roky(client, message):
  await message.reply_text(f"**🥤|تم رفع العضو كلب\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل كلب"))
async def zerso(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع بقره"))
async def vvvtyy(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو بقره\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل بقره"))
async def tttryuh(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع قرد"))
async def uiipppl(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو قرد\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل قرد"))
async def bjhupq(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع قلبي"))
async def pooiejh(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو قلبي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل قلبي"))
async def ttrqew(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع خادم"))
async def qyui(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو خادم\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل خادم"))
async def klhj(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع كذاب"))
async def wqew(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو كذاب\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل كذاب"))
async def ohho(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع ارمله"))
async def drsss(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو ارمله\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل ارمله"))
async def gkvdr(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع صاكه"))
async def cgfyu6f(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو صاكه\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل صاكه"))
async def hhhhug(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع ابني"))
async def cbky(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو ابني\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل ابني"))
async def ccgy(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention} ")
  
  
@app.on_message(filters.command("رفع خاينه"))
async def mkloo(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو خاينه\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل خاينه"))
async def fkijbh(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command("رفع بنتي"))
async def yuhhss(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو بنتي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل بنتي"))
async def hloih(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command("رفع خاين"))
async def kloss(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو خاين\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل خاين"))
async def fiihug(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع صاك"))
async def dadr(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو صاك\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل صاك"))
async def hjj7gv(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع حمار"))
async def cgfyu6f(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو حمار\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل حمار"))
async def cxxv(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  



@app.on_message(filters.command("رفع غبي"))
async def polkij(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو غبي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل غبي"))
async def nbvcc(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command("رفع مرتي"))
async def ttttuhyp(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو مرتي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل مرتي"))
async def xxxxt(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command("رفع زبال"))
async def oooph(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو زبال\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل زبال"))
async def zzzas(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command("رفع خدامه"))
async def ggggop(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو خدامه\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل خدامه"))
async def vvvuu(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command("رفع كلبه"))
async def mmmuy(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو كلبه\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل كلبه"))
async def dfrewq(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command("رفع حرامي"))
async def llok(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو حرامي\n\n🥤| بواسطة : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command("تنزيل حرامي"))
async def kaompj(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  

@app.on_message(
    filters.command(["الالعاب","العاب"])
)
async def zohary(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/1a01f35e8049dc11c8779.png",
        caption= GAME_MESSAGE,
        reply_markup=InlineKeyboardMarkup(GAME_BUTTONS)
    )  
@app.on_callback_query()
async def callback_query(client, CallbackQuery):
          if CallbackQuery.data == "GAME1":
            
             GAME1_MESSAGE = "**🥤| مرحبا بك في قسم اللعاب المتطورة**"

             GAME1_BUTTONS = [
                 [
                    InlineKeyboardButton(
                        "°فلابي بيرد°", url=f"http://t.me/awesomebot?game=FlappyBird"), 
                    InlineKeyboardButton (
                        "°تبديل النجوم°", url=f"http://t.me/gamee?game=Switchy"),
                ],[
                    InlineKeyboardButton (
                        "°موتسيكلات°" , url=f"http://t.me/gamee?game=motofx"),
                    InlineKeyboardButton (
                        "°اطلاق النار°" , url=f"http://t.me/gamee?game=NeonBlaster"),
                ],[
                    InlineKeyboardButton (
                        "°كرة القدم°" , url=f"http://t.me/gamee?game=Footballstar"),
                    InlineKeyboardButton (
                        "°تجميع الالوان°" , url=f"http://t.me/awesomebot?game=Hextris"),
                ],[        
                    InlineKeyboardButton (
                        "°المجوهرات°" , url=f"http://t.me/gamee?game=DiamondRows"),
                    InlineKeyboardButton (
                        "°ركل الكرة°" , url=f"http://t.me/gamee?game=KeepitUP"),
                ],[        
                    InlineKeyboardButton (
                        "°بطولة السحق°" , url=f"http://t.me/gamee?game=SmashRoyale"),
                    InlineKeyboardButton (
                        "°2048°" , url=f"http://t.me/awesomebot?game=g2048"),
                ],[        
                    InlineKeyboardButton (
                        "°كرة السلة°" , url=f"http://t.me/gamee?game=BasketBoy"),
                    InlineKeyboardButton (
                        "°القط المجنون°" , url=f"http://t.me/gamee?game=CrazyCat"),
                ],[
                    InlineKeyboardButton (
                        "◍ رجوع 🔙" , callback_data= 'GAME')
                  ],
             ]
             await CallbackQuery.edit_message_text( 
                 GAME1_MESSAGE ,
                 reply_markup = InlineKeyboardMarkup(GAME1_BUTTONS) 
              )
          elif CallbackQuery.data == "GAME":
               
               RETURN_GAME = "**🥤| مرخبا بك عزيزي\n🥤| في قسم اللعاب اختر ما تريد:**" 

               RETURN_BUTTON = [
                    [ 
                      InlineKeyboardButton ('اللعاب المتطورة', callback_data= 'GAME1'),
                      InlineKeyboardButton ('اللعاب البوت', callback_data= 'GAME2')
                      ],[
        InlineKeyboardButton ('‹ قـناة الـبوت ›', url=config.SUPPORT_CHANNEL)              
                 ],[
                InlineKeyboardButton(
                        "◍ اغلاق 🌐", callback_data="close"),
               ],
          ]
     
               await CallbackQuery.edit_message_text( 
                 RETURN_GAME ,
                 reply_markup = InlineKeyboardMarkup(RETURN_BUTTON) 
                    )
          elif CallbackQuery.data == "GAME2":
               
               SOURCE_GAME = "**- افتارات شباب
- افتارات بنات 
- افتارات عيال 
- افتارات كرتون
- افتارات سينمائية
- افتارات اطفال 
- افتارات رسم 
- افتارات فكتوري 
- افتارات دينية
- افتارات رمضان 
- غنيلي
- شعر
- مزاج
- ميمز
- راب
- افتاري
- افتاره
- كت
- كتص
- اذكار
- دعاء
- اقتباس
- اقتبس
- قران
- حديث
- رواية
- اية
- خطبة
- كتاب اسلامي
- لو خيروك
- نصيحه
- نكته
- متحركه
- ستوري
- هيدرات
- جداريات
- بايو 
- صوره
- انمي 
- صراحه
- حروف**" 

               SORGAM_BUTTON = [
                    [ 
                      InlineKeyboardButton ('‹ قـناة الـبوت ›', url=config.SUPPORT_CHANNEL)
                      ],[
                         InlineKeyboardButton ('◍ رجوع 🔙', callback_data= 'GAME')
                    ]
               ]    
               await CallbackQuery.edit_message_text( 
                 SOURCE_GAME ,
                 reply_markup = InlineKeyboardMarkup(SORGAM_BUTTON) 
                    )
    
