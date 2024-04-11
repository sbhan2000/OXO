from asyncio import sleep
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageDeleteForbidden, RPCError
from pyrogram.types import Message
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC import app

@app.on_message(filters.command(["مسح","حذف"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def del_msg(app: app, msg: Message):
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**🥤| امنحني إذن حذف الرسائل.**")
        return        
    if msg.reply_to_message:
        await msg.delete()
        await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.reply_to_message.id)
    else:
        await msg.reply_text(text="**🥤| قم بالرد ع الرسالة.**")
        return

