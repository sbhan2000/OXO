from pyrogram.enums import ParseMode

from VIPMUSIC import app
from VIPMUSIC.utils.database import is_on_off
from config import LOGGER_ID 

async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
ٴ<b>•────‌‌‏──‌‌‏─‌‌‏─‌‌‏─‌‌‏─‌‌‏─‌‌‏─•</b>
<b>إشعـارات  الميـوزك 𝄞</b>
ٴ<b>•────‌‌‏─‌‌‏─‌‌‏─‌‌‏─‌‌‏──‌‌‏─‌‌‏─•</b>
<b>🥤| سيـدي الـمطـور</b>
<b>🥤| هـنـاك شـخص يـستخـدم {app.mention} حاليـاً</b>

<b>🥤| الاسـم :</b> {message.from_user.mention}
<b>🥤| الـيوزر :</b> @{message.from_user.username}
<b>🥤| ايـدي الـمستخدم :</b> <code>{message.from_user.id}</code>

<b>🥤| اسـم الـمجموعة :</b> {message.chat.title}
<b>🥤| يـوزر الـمجموعة :</b> @{message.chat.username}
<b>🥤| ايـدي الـمجموعة :</b> <code>{message.chat.id}</code>

<b>🥤| الـطلب :</b> {message.text.split(None, 1)[1]}
<b>🥤| نـوع الـتشغيل :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
