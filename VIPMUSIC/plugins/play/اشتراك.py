from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from VIPMUSIC import app
from config import channel 

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not channel:
        return
    try:
        try:
            await app.get_chat_member(channel, msg.from_user.id)
        except UserNotParticipant:
            if channel.isalpha():
                link = "https://t.me/" + channel
            else:
                chat_info = await app.get_chat(channel)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"**🥤| عزيزي {msg.from_user.mention} \n🥤| عليك الأشتراك في قناة البوت \n🥤| قناة البوت :** @{channel}.",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("‹ قـناة الـبوت ›", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"🥤| ارفع البوت مشرف في قناة {channel}!")
