from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils.database import is_muted, mute_off
from VIPMUSIC.utils.decorators import AdminRightsCheck



@app.on_message(filters.command(["unmute","تكلم"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if not await is_muted(chat_id):
        return await message.reply_text(_["admin_47"], disable_web_page_preview=True)
    await mute_off(chat_id)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await VIP.unmute_stream(chat_id)
    await message.reply_text(
        _["admin_48"].format(user_mention), disable_web_page_preview=True
    )
