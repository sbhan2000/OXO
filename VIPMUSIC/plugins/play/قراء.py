import asyncio, redis, requests, datetime, random
from pyrogram import filters, Client
from pyrogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, ReplyKeyboardRemove, Message
from VIPMUSIC import app
from helper import available_reciters, available_urls, data_souar, dict_souar


redis_url = "redis://default:ETw7er7MYHFCWvHIdi8c0BvfKtJKyqSD@redis-16065.c278.us-east-1-4.ec2.cloud.redislabs.com:16065"
r = redis.from_url(redis_url, encoding="utf-8",decode_responses=True)

# ------------------------------------------------

@app.on_message(filters.command(commands='سورة عشوائية', prefixes=['!','/',''], case_sensitive=False) & filters.private)
async def random_reader(client, message):

    num_reciter = random.randint(0, 200)
    url_reciter = available_urls[num_reciter]
    rand_surah = random.choice(dict_souar)
    num_surah = data_souar[rand_surah]
    msg = await message.reply_text(f"`لقد اخترنا لك {rand_surah} من القارئ {available_reciters[num_reciter]} برواية حفص عن عاصم - مرتل , ستصل لك في لحظات ..`")
    link = "{}{}.mp3".format(url_reciter, num_surah)
    try: 
        await client.send_audio(message.chat.id, audio=link)
    except:
        await msg.edit_text(text="عذراً ، حدث خطأ")

# ------------------------------------------------

@app.on_message(filters.command(commands='سأختار 🤍', prefixes=['!','/',''], case_sensitive=False) & filters.private)
async def shoice_reader(client, message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("القائمة الرئيسية")],
            [KeyboardButton('إبراهيم الأخضر'), KeyboardButton('إبراهيم الجبرين'), KeyboardButton('إبراهيم العسيري'), KeyboardButton('شيخ أبو بكر الشاطري')],
            [KeyboardButton('أحمد بن علي العجمي'), KeyboardButton('أحمد الحواشي'), KeyboardButton('أحمد سعود'), KeyboardButton('أحمد صابر')],
            [KeyboardButton('أحمد نعينع'), KeyboardButton('أكرم العلاقمي'), KeyboardButton('إدريس أبكر'), KeyboardButton('الزين محمد أحمد')],
            [KeyboardButton('العشري عمران'), KeyboardButton('توفيق الصايغ'), KeyboardButton('جمال شاكر عبدالله'), KeyboardButton('حمد الدغريري')],
            [KeyboardButton('خالد الجليل'), KeyboardButton('خالد القحطاني'), KeyboardButton('خالد عبدالكافي'), KeyboardButton('خالد الوهيبي')],
            [KeyboardButton('خليفة الطنيجي'), KeyboardButton('داود حمزة'), KeyboardButton('رشيد بلعالية'), KeyboardButton('زكريا حمامة')],
            [KeyboardButton('سعد الغامدي'), KeyboardButton('سعود الشريم'), KeyboardButton('سهل ياسين'), KeyboardButton('زكي داغستاني')],
            [KeyboardButton('سامي الحسن'), KeyboardButton('سامي الدوسري'), KeyboardButton('سيد رمضان'), KeyboardButton('شعبان الصياد')],
            [KeyboardButton('شيرزاد عبدالرحمن طاهر'), KeyboardButton('صابر عبدالحكم'), KeyboardButton('صالح الصاهود'), KeyboardButton('صالح آل طالب')],
            [KeyboardButton('صالح الهبدان'), KeyboardButton('صلاح البدير'), KeyboardButton('صلاح الهاشم'), KeyboardButton('صلاح بو خاطر')],
            [KeyboardButton('عادل ريان'), KeyboardButton('عبدالبارئ الثبيتي'), KeyboardButton('عبدالبارئ محمد'), KeyboardButton('عبدالباسط عبدالصمد')],
            [KeyboardButton('عبدالرحمن السديس'), KeyboardButton('عبدالعزيز الأحمد'), KeyboardButton('عبدالعزيز الزهراني'), KeyboardButton('عبدالله البريمي')],
            [KeyboardButton('عبدالله البعيجان'), KeyboardButton('عبدالله المطرود'), KeyboardButton('عبدالله بصفر'), KeyboardButton('عبدالله خياط')],
            [KeyboardButton('عبدالله عواد الجهني'), KeyboardButton('عبدالله غيلان'), KeyboardButton('عبدالرشيد صوفي'), KeyboardButton('عبدالمحسن الحارثي')],
            [KeyboardButton('عبدالمحسن القاسم'), KeyboardButton('عبدالمحسن العسكر'), KeyboardButton('عبدالمحسن العبيكان'), KeyboardButton('عبدالهادي أحمد كناكري')],
            [KeyboardButton('عبدالودود حنيف'), KeyboardButton('عبدالولي الأركاني'), KeyboardButton('علي أبو هاشم'), KeyboardButton('علي بن عبدالرحمن الحذيفي')],
            [KeyboardButton('علي جابر'), KeyboardButton('علي حجاج السويسي'), KeyboardButton('عماد زهير حافظ'), KeyboardButton('فارس عباد')],
            [KeyboardButton('فهد العتيبي'), KeyboardButton('فهد الكندري'), KeyboardButton('فواز الكعبي'), KeyboardButton('لافي العوني')],
            [KeyboardButton('ناصر القطامي'), KeyboardButton('نبيل الرفاعي'), KeyboardButton('نعمة الحسان'), KeyboardButton('هاني الرفاعي')],
            [KeyboardButton('وليد الدليمي'), KeyboardButton('ياسر الدوسري'), KeyboardButton('ياسر القرشي'), KeyboardButton('ياسر الفيلكاوي')],
            [KeyboardButton('يحيى حوا'), KeyboardButton('يوسف الشويعي'), KeyboardButton('ماجد العنزي'), KeyboardButton('مالك شيبة الحمد')],
            [KeyboardButton('ماهر المعيقلي'), KeyboardButton('محمد البراك'), KeyboardButton('محمد الطبلاوي'), KeyboardButton('محمد اللحيدان')],
            [KeyboardButton('محمد المحيسني'), KeyboardButton('محمد أيوب'), KeyboardButton('محمد صالح عالم شاه'), KeyboardButton('محمد جبريل')],
            [KeyboardButton('محمد صديق المنشاوي'), KeyboardButton('محمد عبدالكريم'), KeyboardButton('محمود خليل الحصري'), KeyboardButton('محمود علي البنا')],
            [KeyboardButton('مشاري العفاسي'), KeyboardButton('مصطفى إسماعيل'), KeyboardButton('مصطفى اللاهوني'), KeyboardButton('مصطفى رعد العزاوي')],
            [KeyboardButton('معمر الأندونيسي'), KeyboardButton('ماجد الزامل'), KeyboardButton('ماهر شخاشيرو'), KeyboardButton('محمد المنشد')],
            [KeyboardButton('ياسر سلامة'), KeyboardButton('أخيل عبدالحي روا'), KeyboardButton('أستاذ زامري'), KeyboardButton('خالد المهنا')],
            [KeyboardButton('عادل الكلباني'), KeyboardButton('موسى بلال'), KeyboardButton('حسين آل الشيخ'), KeyboardButton('حاتم فريد الواعر')],
            [KeyboardButton('إبراهيم الجرمي'), KeyboardButton('محمود الرفاعي'), KeyboardButton('ناصر العبيد'), KeyboardButton('واصل المذن')],
            [KeyboardButton('إبراهيم الدوسري'), KeyboardButton('جمعان العصيمي'), KeyboardButton('رضية عبدالرحمن'), KeyboardButton('رقية سولونق')],
            [KeyboardButton('سابينة مامات'), KeyboardButton('سيدين عبدالرحمن'), KeyboardButton('عبدالغني عبدالله'), KeyboardButton('عبدالله فهمي')],
            [KeyboardButton('محمد الحافظ'), KeyboardButton('محمد حفص علي'), KeyboardButton('محمد خير النور'), KeyboardButton('يوسف بن نوح أحمد')],
            [KeyboardButton('جمال الدين الزيلعي'), KeyboardButton('معيض الحارثي'), KeyboardButton('محمد رشاد الشريف'), KeyboardButton('أحمد الطرابلسي')],
            [KeyboardButton('عبدالله الكندري'), KeyboardButton('أحمد عامر'), KeyboardButton('إبراهيم السعدان'), KeyboardButton('أحمد الحذيفي')],
            [KeyboardButton('محمد عثمان خان'), KeyboardButton('يوسف الدغوش'), KeyboardButton('وشيار حيدر اربيلي'), KeyboardButton('عثمان الأنصاري')],
            [KeyboardButton('بندر بليله'), KeyboardButton('خالد الشريمي'), KeyboardButton('وديع اليمني'), KeyboardButton('رعد محمد الكردي')],
            [KeyboardButton('عبدالرحمن العوسي'), KeyboardButton('خالد الغامدي'), KeyboardButton('رمضان شكور'), KeyboardButton('عبدالمجيد الأركاني')],
            [KeyboardButton('محمد خليل القارئ'), KeyboardButton('رامي الدعيس'), KeyboardButton('هزاع البلوشي'), KeyboardButton('عبدالرحمن الماجد')],
            [KeyboardButton('سلمان العتيبي'), KeyboardButton('محمد رفعت'), KeyboardButton('عبدالله الموسى'), KeyboardButton('عبدالله الخلف')],
            [KeyboardButton('منصور السالمي'), KeyboardButton('صلاح مصلي'), KeyboardButton('خالد الشارخ'), KeyboardButton('ناصر العصفور')],
            [KeyboardButton('أحمد السويلم'), KeyboardButton('إسلام صبحي'), KeyboardButton('بدر التركي'), KeyboardButton('هيثم الجدعاني')],
            [KeyboardButton('ناصر الماجد'), KeyboardButton('أحمد خليل شاهين'), KeyboardButton('محمد البخيت'), KeyboardButton('سعد المقرن')],
            [KeyboardButton('أحمد النفيس'), KeyboardButton('عمر الدريويز'), KeyboardButton('عبدالعزيز العسيري'), KeyboardButton('أحمد ديبان')],
            [KeyboardButton('عبدالله كامل'), KeyboardButton('بيشه وا قادر الكردي'), KeyboardButton('نذير المالكي'), KeyboardButton('محمود عبدالحكم')],
            [KeyboardButton('عبدالرحمن السويّد'), KeyboardButton('عبدالإله بن عون'), KeyboardButton('أحمد طالب بن حميد'), KeyboardButton('عبدالله بخاري')],
            [KeyboardButton('عبدالعزيز التركي'), KeyboardButton('مختار الحاج'), KeyboardButton('عبدالله عبدل'), KeyboardButton('أحمد عيسى المعصراوي')],
            [KeyboardButton('هاشم أبو دلال'), KeyboardButton('فؤاد الخامري'), KeyboardButton('سيد أحمد هاشمي'), KeyboardButton('خالد كريم محمدي')],
            [KeyboardButton('صالح الشمراني'), KeyboardButton('مال الله عبدالرحمن الجابر'), KeyboardButton('سلمان الصديق'), KeyboardButton('حسن صالح')],
            [KeyboardButton('عبدالرحمن الشحات'), KeyboardButton('عيسى عمر سناكو'), KeyboardButton('هارون بقائي'), KeyboardButton('فيصل الهاجري')],
            [KeyboardButton('أنس العمادي'), KeyboardButton('عبدالملك العسكر'), KeyboardButton('عبدالكريم الحازمي'), KeyboardButton('عبدالله المشعل')],
        ],
        resize_keyboard=True, one_time_keyboard=False
    )
    await message.reply_text("فضلا اختر القارئ المراد الاستماع له ...", quote=True, reply_markup=keyboard)

# ------------------------------------------------

@app.on_message(filters.command(commands=available_reciters, prefixes=['!','/',''],case_sensitive=False) & filters.private)
async def shoice_surah(client, message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("القائمة الرئيسية")],
        [KeyboardButton("النساء"), KeyboardButton("آل عمران"), KeyboardButton("البقرة"), KeyboardButton("الفاتحة")],
        [KeyboardButton("التوبة"), KeyboardButton("الأنفال"), KeyboardButton("الأعراف"), KeyboardButton("الأنعام")],
        [KeyboardButton("إبراهيم"), KeyboardButton("الرعد"), KeyboardButton("يوسف"), KeyboardButton("هود")],
        [KeyboardButton("مريم"), KeyboardButton("الكهف"), KeyboardButton("الإسراء"), KeyboardButton("النحل")],
        [KeyboardButton("النور"), KeyboardButton("المؤمنون"), KeyboardButton("الحج"), KeyboardButton("الأنبياء")],
        [KeyboardButton("العنكبوت"), KeyboardButton("القصص"), KeyboardButton("النمل"), KeyboardButton("الشعراء")],
        [KeyboardButton("سبأ"), KeyboardButton("الأحزاب"), KeyboardButton("السجدة"), KeyboardButton("لقمان")],
        [KeyboardButton("الزمر"), KeyboardButton("ص"), KeyboardButton("الصافات"), KeyboardButton("يس")],
        [KeyboardButton("الدّخان"), KeyboardButton("الزخرف"), KeyboardButton("الشورى"), KeyboardButton("فصلت")],
        [KeyboardButton("الحجرات"), KeyboardButton("الفتح"), KeyboardButton("محمد"), KeyboardButton("الأحقاف")],
        [KeyboardButton("القمر"), KeyboardButton("النجم"), KeyboardButton("الطور"), KeyboardButton("الذاريات")],
        [KeyboardButton("الحشر"), KeyboardButton("المجادلة"), KeyboardButton("الحديد"), KeyboardButton("الواقعة")],
        [KeyboardButton("التغابن"), KeyboardButton("المنافقون"), KeyboardButton("الجمعة"), KeyboardButton("الصف")],
        [KeyboardButton("الحاقة"), KeyboardButton("القلم"), KeyboardButton("الملك"), KeyboardButton("التحريم")],
        [KeyboardButton("المدثر"), KeyboardButton("المزمل"), KeyboardButton("الجن"), KeyboardButton("نوح")],
        [KeyboardButton("النازعات"), KeyboardButton("النبأ"), KeyboardButton("المرسلات"), KeyboardButton("الإنسان")],
        [KeyboardButton("الإنشقاق"), KeyboardButton("المطففين"), KeyboardButton("الإنفطار"), KeyboardButton("التكوير")],
        [KeyboardButton("الفجر"), KeyboardButton("الغاشية"), KeyboardButton("الأعلى"), KeyboardButton("الطارق")],
        [KeyboardButton("الشرح"), KeyboardButton("الضحى"), KeyboardButton("الليل"), KeyboardButton("الشمس")],
        [KeyboardButton("الزلزلة"), KeyboardButton("البينة"), KeyboardButton("القدر"), KeyboardButton("العلق")],
        [KeyboardButton("الهمزة"), KeyboardButton("العصر"), KeyboardButton("التكاثر"), KeyboardButton("القارعة")],
        [KeyboardButton("الكافرون"), KeyboardButton("الكوثر"), KeyboardButton("الماعون"), KeyboardButton("قريش")],
        [KeyboardButton("الناس"), KeyboardButton("الفلق"), KeyboardButton("الإخلاص"), KeyboardButton("المسد")],
    ],
        resize_keyboard=True, one_time_keyboard=False
    )
    r.hset("QURAN-Reader", message.from_user.id, message.text)
    await message.reply_text("فضلا اختر السورة المراد الاستماع لها ...", quote=True, reply_markup=keyboard)

# ------------------------------------------------

surahs = ["الفاتحة", "البقرة", "آل عمران", "النساء", "المائدة", "الأنعام", "الأعراف", "الأنفال", "التوبة", "يونس", "هود", "يوسف", "الرعد", "إبراهيم", "الحجر", "النحل", "الإسراء", "الكهف", "مريم", "طه", "الأنبياء", "الحج", "المؤمنون", "النور", "الفرقان", "الشعراء", "النمل", "القصص", "العنكبوت", "الروم", "لقمان", "السجدة", "الأحزاب", "سبأ", "فاطر", "يس", "الصافات", "ص", "الزمر", "غافر", "فصلت", "الشورى", "الزخرف", "الدخان", "الجاثية", "الأحقاف", "محمد", "الفتح", "الحجرات", "ق", "الذاريات", "الطور", "النجم", "القمر", "الرحمن", "الواقعة", "الحديد", "المجادلة", "الحشر", "الممتحنة", "الصف", "الجمعة", "المنافقون", "التغابن", "الطلاق", "التحريم", "الملك", "القلم", "الحاقة", "المعارج", "نوح", "الجن", "المزمل", "المدثر", "القيامة", "الإنسان", "المرسلات", "النبأ", "النازعات", "عبس", "التكوير", "الانفطار", "المطففين", "الانشقاق", "البروج", "الطارق", "الأعلى", "الغاشية", "الفجر", "البلد", "الشمس", "الليل", "الضحى", "الشرح", "التين", "العلق", "القدر", "البينة", "الزلزلة", "العاديات", "القارعة", "التكاثر", "العصر", "الهمزة", "الفيل", "قريش", "الماعون", "الكوثر", "الكافرون", "النصر", "المسد", "الإخلاص", "الفلق", "الناس"]
surahss = ["سورة الفاتحة", "سورة البقرة", "سورة آل عمران", "سورة النساء", "سورة المائدة", "سورة الأنعام", "سورة الأعراف", "سورة الأنفال", "سورة التوبة", "سورة يونس", "سورة هود", "سورة يوسف", "سورة الرعد", "سورة إبراهيم", "سورة الحجر", "سورة النحل", "سورة الإسراء", "سورة الكهف", "سورة مريم", "سورة طه", "سورة الأنبياء", "سورة الحج", "سورة المؤمنون", "سورة النور", "سورة الفرقان", "سورة الشعراء", "سورة النمل", "سورة القصص", "سورة العنكبوت", "سورة الروم", "سورة لقمان", "سورة السجدة", "سورة الأحزاب", "سورة سبأ", "سورة فاطر", "سورة يس", "سورة الصافات", "سورة ص", "سورة الزمر", "سورة غافر", "سورة فصلت", "سورة الشورى", "سورة الزخرف", "سورة الدخان", "سورة الجاثية", "سورة الأحقاف", "سورة محمد", "سورة الفتح", "سورة الحجرات", "سورة ق", "سورة الذاريات", "سورة الطور", "سورة النجم", "سورة القمر", "سورة الرحمن", "سورة الواقعة", "سورة الحديد", "سورة المجادلة", "سورة الحشر", "سورة الممتحنة", "سورة الصف", "سورة الجمعة", "سورة المنافقون", "سورة التغابن", "سورة الطلاق", "سورة التحريم", "سورة الملك", "سورة القلم", "سورة الحاقة", "سورة المعارج", "سورة نوح", "سورة الجن", "سورة المزمل", "سورة المدثر", "سورة القيامة", "سورة الإنسان", "سورة المرسلات", "سورة النبأ", "سورة النازعات", "سورة عبس", "سورة التكوير", "سورة الانفطار", "سورة المطففين", "سورة الانشقاق", "سورة البروج", "سورة الطارق", "سورة الأعلى", "سورة الغاشية", "سورة الفجر", "سورة البلد", "سورة الشمس", "سورة الليل", "سورة الضحى", "سورة الشرح", "سورة التين", "سورة العلق", "سورة القدر", "سورة البينة", "سورة الزلزلة", "سورة العاديات", "سورة القارعة", "سورة التكاثر", "سورة العصر", "سورة الهمزة", "سورة الفيل", "سورة قريش", "سورة الماعون", "سورة الكوثر", "سورة الكافرون", "سورة النصر", "سورة المسد", "سورة الإخلاص", "سورة الفلق", "سورة الناس"]
@app.on_message(filters.command(commands=surahs, prefixes=['!','/',''],case_sensitive=False))
@app.on_message(filters.command(commands=surahss, prefixes=['!','/',''],case_sensitive=False))
async def send_audio(client, message):
    reader = r.hget("QURAN-Reader", message.from_user.id)
    if reader:
        await message.reply_text(f"`لقد اخترت سورة {message.text.replace('سورة ', '')} من القارئ {reader} برواية حفص عن عاصم - مرتل , ستصل لك في لحظات ..`")
        num_reader = available_reciters.index(reader)
        url = available_urls[num_reader]
        number = data_souar[message.text.replace('سورة ', '')]
        print(f"{url}{number}")
        await message.reply_audio(audio=f"{url}{number}.mp3")

# ------------------------------------------------
print("$ The bot is working now")
asyncio.get_event_loop()
