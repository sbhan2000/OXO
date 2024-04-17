from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils.database import set_loop
from VIPMUSIC.utils.decorators import AdminRightsCheck
from VIPMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "stop", "انهاء", "ايقاف"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await VIP.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await message.reply_text(
        _["admin_5"].format(user_mention), reply_markup=close_markup(_)
    )
