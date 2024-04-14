from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import autoend_off, autoend_on


@app.on_message(filters.command(["autoend","المغادره التلقائيه","المغادرة التلقائية"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>🥤| مثــال :</b>\n\n🥤| المغادره التلقائيه [تفعيل | تعطيل]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "تفعيل":
        await autoend_on()
        await message.reply_text(
            "**🥤| تم تفعيل المغادرة التلقائية للمساعد .. بنجاح\n\nالحساب المساعد سوف يقوم بمغادرة الدردشة تلقائياً .. عند عدم وجود اشخاص في المكالمة**"
        )
    elif state == "تعطيل":
        await autoend_off()
        await message.reply_text("**🥤| تم تعطيل وضع المغادرة التلقائية للمساعد .. بنجاح.**")
    else:
        await message.reply_text(usage)
