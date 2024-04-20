import json
import urllib.request

if text == "الختمه" or text == "الختمة":
    reply_markup = {
        "type": "inline",
        "data": [
            [
                {"text": "البدء من جديد", "data": f"{msg.sender_id.user_id}/restas"},
                {"text": "استئناف الختمه", "data": f"{msg.sender_id.user_id}/estisaf"}
            ]
        ]
    }
    return buttons

# callback

if Text and Text.startswith(r'(\d+)/restas'):  # البدء من جديد / أول صفحه
    Redis.delete(f"{TheMero}:readables:{IdUser}")
    photo = "https://quran.ksu.edu.sa/png_big/1.png"
    caption = "الصفحه 1"
    readable = 0
    ratpep = readable + 1
    Redis.set(f"{TheMero}:readables:{IdUser}", int(ratpep))
    keyboard = {
        "inline_keyboard": [
            [{"text": " التالي ", "callback_data": "/nextts"}],
            [{"text": " السابق ", "callback_data": "/priors"}]
        ]
    }
    msg_rep = msg.id / 2097152 / 0.5
    urllib.request.urlopen(f"https://api.telegram.org/bot{Token}/sendphoto?chat_id={msg.chat_id}&reply_to_message_id={msg_rep}&photo={photo}&caption={urllib.parse.quote(caption)}&parse_mode=markdown&disable_web_page_preview=true&reply_markup={json.dumps(keyboard)}")

if Text == "/nextts":  # التالي
    readablet = int(Redis.get(f"{TheMero}:readables:{IdUser}") or 0)
    if readablet == 604:  # اخر صفحه
        return False
    ratpep = readablet + 1
    Redis.set(f"{TheMero}:readables:{IdUser}", int(ratpep))
    media = {
        "type": "photo",
        "media": f"https://quran.ksu.edu.sa/png_big/{int(ratpep)}.png",
        "caption": f'الصفحه {int(ratpep)} ',
        "parse_mode": "Markdown"
    }
    keyboard = {
        "inline_keyboard": [
            [{"text": " التالي ", "callback_data": "/nextts"}],
            [{"text": " السابق ", "callback_data": "/priors"}]
        ]
    }
    msg_rep = Msg_id / 2097152 / 0.5
    urllib.request.urlopen(f"http://api.telegram.org/bot{Token}/editmessagemedia?chat_id={ChatId}&message_id={msg_rep}&media={json.dumps(media)}&reply_markup={json.dumps(keyboard)}")

if Text == "/priors":  # السابق
    readablet = int(Redis.get(f"{TheMero}:readables:{IdUser}") or 2)
    if readablet == 1:
        return False
    ratpep = readablet - 1
    Redis.set(f"{TheMero}:readables:{IdUser}", int(ratpep))
    media = {
        "type": "photo",
        "media": f"https://quran.ksu.edu.sa/png_big/{int(ratpep)}.png",
        "caption": f'الصفحه {int(ratpep)} ',
        "parse_mode": "Markdown"
    }
    keyboard = {
        "inline_keyboard": [
            [{"text": " التالي ", "callback_data": "/nextts"}],
            [{"text": " السابق ", "callback_data": "/priors"}]
        ]
    }
    msg_rep = Msg_id / 2097152 / 0.5
    urllib.request.urlopen(f"http://api.telegram.org/bot{Token}/editmessagemedia?chat_id={ChatId}&message_id={msg_rep}&media={json.dumps(media)}&reply_markup={json.dumps(keyboard)}")

if Text and Text.startswith(r'(\d+)/estisaf'):  # استئناف
    readablet = int(Redis.get(f"{TheMero}:readables:{IdUser}") or 1)
    photo = f"https://quran.ksu.edu.sa/png_big/{readablet}.png"
    caption = f"الصفحه {readablet}"
    readable = 1
    ratpep = readable + 1
    Redis.set(f"{TheMero}:readables:{IdUser}", int(ratpep))
    keyboard = {
        "inline_keyboard": [
            [{"text": " التالي ", "callback_data": "/nextts"}],
            [{"text": " السابق ", "callback_data": "/priors"}]
        ]
    }
    msg_rep = msg.id / 2097152 / 0.5
    urllib.request.urlopen(f"https://api.telegram.org/bot{Token}/sendphoto?chat_id={msg.chat_id}&reply_to_message_id={msg_rep}&photo={photo}&caption={urllib.parse.quote(caption)}&parse_mode=markdown&disable_web_page_preview=true&reply_markup={json.dumps(keyboard)}")
