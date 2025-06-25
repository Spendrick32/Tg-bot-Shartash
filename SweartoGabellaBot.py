import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("7927430165:AAEkAGSTQrVX2weyfLTkjwbPEvx1llzIkSg")

# Клавиатура с одной кнопкой "Начать"
def start_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Начать")
    markup.add(btn)
    return markup

# Основная клавиатура после нажатия "Начать"
def main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Информация")
    btn2 = types.KeyboardButton("Карта")
    btn3 = types.KeyboardButton("Места")
    markup.add(btn1, btn2, btn3)
    return markup

#Клавиатура с интересными местами
def places_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Церковь Саввы Сербского")
    btn2 = types.KeyboardButton("Водонапорная башня")
    btn3 = types.KeyboardButton("Стоянка древнего человека")
    btn4 = types.KeyboardButton("Низинное болото")
    btn5 = types.KeyboardButton("Озеро малый Шарташ")
    btn6 = types.KeyboardButton("Вернуться назад")
    markup.add(btn1,btn2,btn3,btn4,btn5, btn6)
    return markup

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_start_button(message):
    bot.send_message(message.chat.id, 'Нажмите "Начать", чтобы продолжить', reply_markup=start_keyboard())

# Обработчик кнопки "Начать" (Приветствие + Появление кнопок)
@bot.message_handler(func=lambda message: message.text == "Начать")
def on_click(message):
    bot.send_message(
        message.chat.id,
        'Привет! \n<b>Мы - клуб друзей Шарташа.</b>\nЭтот бот посвящён тропе Шарташа под названием "Тропа к низинному болоту".\n'
        '<u>Доступные кнопки:</u>\n'
        '- <b>Карта</b>: сайт с картой маршрута.\n'
        '- <b>Информация</b>: наш телеграм-канал и группа ВК.\n'
        '-  <b>Места</b>: интересные места на тропе.',
        parse_mode='html',
        reply_markup=main_keyboard()
    )

# Обработчик кнопки "Карта"
@bot.message_handler(func=lambda message: message.text == "Карта")
def site(message):
    bot.send_message(
        message.chat.id,
        "Вот карта маршрута: [Открыть карту](https://yandex.ru/maps/?um=constructor%3A105945cdd1626f3cd498cd066765a3428ade76758af1a18695a225fbdf7ebe31&source=constructorLink)",
        parse_mode="Markdown"
    )

# Обработчик кнопки "Информация"
@bot.message_handler(func=lambda message: message.text == "Информация")
def info(message):
    bot.send_message(message.chat.id, "Наш Telegram-канал: https://t.me/shartash_frends_club \nНаша группа ВК: https://vk.com/shartash_frends_club")

# Обработчик команды "Места"
@bot.message_handler(func=lambda message: message.text == "Места")
def places(message):
    bot.send_message(message.chat.id,"Выбери интересующее тебя место на тропе", reply_markup=places_keyboard())

# Обработчик команды "Вернуться назад (места)"

@bot.message_handler(func=lambda message: message.text == "Вернуться назад")
def back(message):
    bot.send_message(message.chat.id, "Возвращаюсь назад...", reply_markup=main_keyboard())

# Обработчик команды "Церковь Саввы Сербского (места)"

@bot.message_handler(func=lambda message: message.text == "Церковь Саввы Сербского")
def church(message):
        bot.send_photo(message.chat.id, photo="https://sobory.ru/pic/32300/32306_20141106_220429.jpg", caption= "<b>Церковь Саввы Сербского</b> в Екатеринбурге была построена в 2003 году и является ярким примером сербского православного архитектурного стиля. Это храм в честь святого Саввы Сербского, одного из основателей Сербской православной церкви и значимой фигуры в истории православия. \n Церковь выполнена в традиционном византийском стиле с элементами русской и сербской архитектуры. Среди её особенностей — купола в форме луковиц, мозаики на фасаде и яркие фрески внутри, изображающие сцены из жизни святого Саввы и другие святых.", parse_mode='html', reply_markup=places_keyboard())

@bot.message_handler(func=lambda message: message.text == "Водонапорная башня")
def tower(message):
        bot.send_photo(message.chat.id, photo="https://avatars.mds.yandex.net/get-altay/11522875/2a0000018e1e2fc5c0570e8f5a7ab6254c31/XXXL", caption= "<b>Водонапорная башня</b> — это исторический памятник, построенный в 1927 году для обеспечения водоснабжения района. Башня выполнена в стиле <i>конструктивизма</i> и имеет высоту около 30 метров.\nСегодня водонапорная башня утратила свою первоначальную функцию, но остаётся важным элементом городской истории и символом индустриального прошлого Екатеринбурга", parse_mode='html', reply_markup=places_keyboard())

@bot.message_handler(func=lambda message: message.text == "Стоянка древнего человека")
def old(message):
        bot.send_photo(message.chat.id, photo="https://avatars.mds.yandex.net/get-altay/14092818/2a00000192ec1008b89651b6fa672ae9bc72/XXXL", caption= "<b>Стоянка древнего человека</b> — это археологический памятник, расположенный рядом с озером Шарташ. Первобытные люди жили здесь в III тысячелетии до нашей эры, эта стоянка является одной из самых известных на Урале.Гряда камней была условным центром поселения и жертвенным местом.", parse_mode='html', reply_markup=places_keyboard())

@bot.message_handler(func=lambda message: message.text == "Низинное болото")
def shrek(message):
        bot.send_photo(message.chat.id, photo="https://avatars.dzeninfra.ru/get-zen_doc/1917783/pub_5ff96a43f906b1687290aea0_5ff96ff5f906b1687299d564/scale_2400", caption= "<b>Низинное болото</b> рядом с озером Малый Шарташ связано с большими водоемами в этом районе. Вода с обоих озер стекает в низину к северо-западу от озера.Эта территория характерна болотной растительностью и каменными останцами, оставшимися от старых строительных материалов. Болото трудно доступно летом, но зимой можно лучше исследовать его окрестности.", parse_mode='html', reply_markup=places_keyboard())

@bot.message_handler(func=lambda message: message.text == "Озеро малый Шарташ")
def shrek(message):
        bot.send_photo(message.chat.id, photo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Maly_Shartash_%28August_2022%29_-_2.jpg/1920px-Maly_Shartash_%28August_2022%29_-_2.jpg", caption= "<b>Озеро Малый Шарташ</b> — небольшой водоём, расположенный рядом с Шарташским гранитным карьером. Его площадь около <b>3,4 га</b>, а берега сильно заболочены и покрыты тростником, осокой и кустарниками.Озеро связано с Малошарташским торфяным болотом, куда стекает вода с обоих Шарташских озёр. Место труднодоступно и редко посещается, но интересно для исследователей и любителей дикой природы.", parse_mode='html', reply_markup=places_keyboard())


bot.infinity_polling()