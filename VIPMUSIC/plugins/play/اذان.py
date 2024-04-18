from pyrogram import Client, filters
import requests
from VIPMUSIC import app 

@app.on_message(filters.command(["الاذان"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
def meme_command(client, message):
    api_url = "https://api.aladhan.com"

    try:
        response = requests.get(api_url)
        data = response.json()

        meme_url = data.get("url")
        title = data.get("title")

        caption = f"{title}\n\nRequest by {message.from_user.mention}\nBot username: @{app.get_me().username}"

        message.reply_photo(
            photo=meme_url,
            caption=caption
        )

    except Exception as e:
        print(f"Error fetching meme: {e}")
        message.reply_text("Sorry, I couldn't fetch a meme at the moment.")
