import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from typing import Union
from VIPMUSIC import app
import re
import sys
import config
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from VIPMUSIC.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID




GAME_MESSAGE = "**🥤| مرحبا بك عزيزي\n🥤| في قسم العاب اختر ما تريد **"
GAME_BUTTONS = [
    [ 
        InlineKeyboardButton ('اللعاب المتطورة', callback_data= 'GAME1'),
        InlineKeyboardButton ('العاب البوت', callback_data= 'GAME2')
        ],[
        InlineKeyboardButton ('العاب التسلية', callback_data= 'GAME3')           
        ],[
        InlineKeyboardButton ('‹ قـناة الـبوت ›', url=config.SUPPORT_CHANNEL)              
                 ],[
                InlineKeyboardButton(
                        "◍ اغلاق 🌐", callback_data="close"),
               ],
          ]
    

nmla = []

@app.on_message(filters.command(["رفع نمله"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def rf3nmla(client, message):
  if not message.reply_to_message.from_user.mention in nmla:
    nmla.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**🥤| تم رفع العضو نملهn\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل نمله"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in nmla:
    nmla.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["المرفوعين نمل"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def nml(client, message):
  nq = ""
  for n in nmla:
      nq += n + "\n"
  await message.reply_text(nq)





@app.on_message(filters.command(["رفع صرصار"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def rf3srsar(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو صرصار\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل صرصار"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def tnzelsrar(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["رفع رقاصه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def yasooo(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو رقاصه\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل رقاصه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def yaso(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
  
@app.on_message(filters.command(["رفع نجس"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def fdsa(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو نجس\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل نجس"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def kophvc(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع حبيبي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def roky(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو حبيبي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل حبيبي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def zerso(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع بقره"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def vvvtyy(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو بقره\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل بقره"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def tttryuh(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع قرد"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def uiipppl(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو قرد\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل قرد"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def bjhupq(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع قلبي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def pooiejh(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو قلبي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل قلبي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def ttrqew(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع خادم"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def qyui(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو خادم\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل خادم"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def klhj(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع كذاب"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def wqew(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو كذاب\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل كذاب"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def ohho(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع ارمله"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def drsss(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو ارمله\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل ارمله"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def gkvdr(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع صاكه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def cgfyu6f(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو صاكه\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل صاكه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def hhhhug(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع ابني"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def cbky(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو ابني\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل ابني"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def ccgy(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention} ")
  
  
@app.on_message(filters.command(["رفع خاينه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def mkloo(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو خاينه\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل خاينه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def fkijbh(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command(["رفع بنتي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def yuhhss(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو بنتي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل بنتي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def hloih(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command(["رفع خاين"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def kloss(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو خاين\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل خاين"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def fiihug(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع صاك"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def dadr(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو صاك\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل صاك"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def hjj7gv(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع حمار"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def cgfyu6f(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو حمار\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل حمار"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def cxxv(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  



@app.on_message(filters.command(["رفع غبي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def polkij(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو غبي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل غبي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def nbvcc(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  
  
@app.on_message(filters.command(["رفع مرتي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def ttttuhyp(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو مرتي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل مرتي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def xxxxt(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command(["رفع زبال"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def oooph(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو زبال\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل زبال"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def zzzas(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command(["رفع خدامه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def ggggop(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو خدامه\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل خدامه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def vvvuu(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command(["رفع حبيبتي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def mmmuy(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو حبيبتي\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل حبيبتي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def dfrewq(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")  
  
  
@app.on_message(filters.command(["رفع حرامي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def llok(client, message):
  await message.reply_text(f"**🥤| تم رفع العضو حرامي\n\n🥤| بواسطة : {message.reply_to_message.from_user.mention}")


@app.on_message(filters.command(["تنزيل حرامي"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])) 
async def kaompj(client, message):
  await message.reply_text(f"**🥤| تم تنزيل العضو\n\n🥤| بواسطة** : {message.reply_to_message.from_user.mention}")
  

@app.on_message(
    filters.command(["الالعاب","العاب"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) 
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
            
             GAME1_MESSAGE = "**<u>🏮 اللعاب المتطورة</u>\n🥤| مرحبا بك في قسم اللعاب المتطورة**"

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
                    ]
               ]
             await CallbackQuery.edit_message_text( 
                 GAME2_MESSAGE ,
                 reply_markup = InlineKeyboardMarkup(GAME2_BUTTONS) 
              )
          elif CallbackQuery.data == "GAME":
               
               RETURN_GAME = "**🥤| مرحبا بك عزيزي\n🥤| في قسم اللعاب اختر ما تريد**" 

               RETURN_BUTTON = [
                    [ 
                      InlineKeyboardButton ('اللعاب المتطورة', callback_data= 'GAME1'),
                      InlineKeyboardButton ('العاب البوت', callback_data= 'GAME2')
        ],[
        InlineKeyboardButton ('العاب التسلية', callback_data= 'GAME3')
                      ],[
        InlineKeyboardButton ('‹ قـناة الـبوت ›', url=config.SUPPORT_CHANNEL)              
                 ],[
                InlineKeyboardButton(
                        "◍ اغلاق 🌐", callback_data="close"),
               ],
          ]
               
               await CallbackQuery.edit_message_text( 
                 GAME1_MESSAGE ,
                 reply_markup = InlineKeyboardMarkup(GAME1_BUTTONS) 
              )
          elif CallbackQuery.data == "GAME":
               
               RETURN_GAME = "**🥤| مرحبا بك عزيزي\n🥤| في قسم اللعاب اختر ما تريد**" 

               RETURN_BUTTON = [
                    [ 
                      InlineKeyboardButton ('اللعاب المتطورة', callback_data= 'GAME1'),
                      InlineKeyboardButton ('العاب البوت', callback_data= 'GAME2')
        ],[
        InlineKeyboardButton ('العاب التسلية', callback_data= 'GAME3')
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
          elif CallbackQuery.data == "GAME3":
               
               GAME2_MESSAGE = "**<u>🏮 العاب التسلية</u>\n🥤| رفع/تنزيل\n- نمله\n- حرامي\n- حبيبي\n- حبيبتي\n- ابني\n- بنتي\n- زوجي\n- زوجتي\n- مرتي\n- خاين\n- خاينه\n- قلبي\n- صاك\n- صاكه\n- حرامي\n- خادم\n- خدامه\n- قرد\n- حمار\n- بقره\n- نجس\n- صرصار\n- رقاصه\n-ارمله\n- زبال\n- غبي**" 

               GAME2_BUTTONS = [
                    [ 
                      InlineKeyboardButton ('‹ قـناة الـبوت ›', url=config.SUPPORT_CHANNEL)
                      ],[
                         InlineKeyboardButton ('◍ رجوع 🔙', callback_data= 'GAME')
                    ]
               ]
               
               await CallbackQuery.edit_message_text( 
                 RETURN_GAME ,
                 reply_markup = InlineKeyboardMarkup(RETURN_BUTTON) 
                    )
          elif CallbackQuery.data == "GAME2":
               
               SOURCE_GAME = "**<u>🏮 العاب البوت</u>\n- افتارات شباب\n- افتارات بنات\n- افتارات عيال\n- افتارات كرتون\n- افتارات سينمائية\n- افتارات اطفال\n- افتارات رسم\n- افتارات فكتوري\n- افتارات دينية\n- افتارات رمضان\n- غنيلي\n- شعر\n- مزاج\n- ميمز\n- راب\n- افتاري\n- افتاره\n- كت\n- كتص\n- اذكار\n- دعاء\n- اقتباس\n- اقتبس\n- قران\n- حديث\n- رواية\n- اية\n- خطبة\n- كتاب اسلامي\n- لو خيروك\n- نصيحه\n- نكته\n- متحركه\n- ستوري\n- هيدرات\n- جداريات\n- بايو\n- صوره\n- انمي\n- صراحه\n- حروف**" 

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
    

    



