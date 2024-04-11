from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from unidecode import unidecode

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


async def generate_join_link(chat_id: int):
    invite_link = await app.export_chat_invite_link(chat_id)
    return invite_link


def ordinal(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix


@app.on_message(filters.command(["المكالمات الصوتية", "المكالمات الصوتيه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("**🥤| جاري البحث عن مكالمات صوتيه نشطة...**")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    buttons = []
    for x in served_chats:
        try:
            chat_info = await app.get_chat(x)
            title = chat_info.title
            invite_link = await generate_join_link(x)
        except:
            await remove_active_chat(x)
            continue
        try:
            if chat_info.username:
                user = chat_info.username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
            button_text = f"اشترك{ordinal(j + 1)} "
            buttons.append([InlineKeyboardButton(button_text, url=invite_link)])
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"**🥤| لا توجد مكالمات صوتيه نشطة ** {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>🥤| المكالمات الصوتية النشطة :</b>\n\n{text}",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["المكالمات المرئيه", "المكالمات المرئية"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("**🥤| جاري البحث عن مكالمات مرئية نشطة...**")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    buttons = []
    for x in served_chats:
        try:
            chat_info = await app.get_chat(x)
            title = chat_info.title
            invite_link = await generate_join_link(x)
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if chat_info.username:
                user = chat_info.username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
            button_text = f"اشترك {ordinal(j + 1)}"
            buttons.append([InlineKeyboardButton(button_text, url=invite_link)])
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"**🥤| لا توجد مكالمات مرئيه نشطة** {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>🥤| المكالمات المرئيه النشطة :</b>\n\n{text}",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )
@app.on_message(filters.command(["المكالمات النشطة", "المكالمات النشطه"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])  & SUDOERS)
async def start(client: Client, message: Message):
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    await message.reply_text(f"🥤| <b><u>المكالمات النشطة الان</u></b> :\n\n🥤| الصوتيه : {ac_audio}\n🥤| المرئيه  : {ac_video}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('✯ ᴄʟᴏsᴇ ✯', callback_data=f"close")]]))
