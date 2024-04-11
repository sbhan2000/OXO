from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils.database import is_music_playing, music_on
from VIPMUSIC.utils.decorators import AdminRightsCheck
from VIPMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["resume", "استئناف","كمل"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await VIP.resume_stream(chat_id)
    buttons_resume = [
        [
            
            InlineKeyboardButton(
                text="تخطي", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ايقاف", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ايقاف مؤقت",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
        ]
    ]
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons_resume)
    )
