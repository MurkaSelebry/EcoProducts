import telebot
from telebot import types

bot = telebot.TeleBot('5932020939:AAFC56lTYXkvbWdARlxKHlvP4fqlHn_-AoQ')

product_prices = {}
selected_stores = {}
selected_plans = {}
vegan_products = {
    'Морковь': 10,
    'Брокколи': 15,
    'Овсянка': 20,
    'Авокадо': 25,
    'Тофу': 30
}
regular_products = {
    'Курица': 50,
    'Рис': 40,
    'Гречка': 35,
    'Молоко': 30,
    'Яйца': 25
}

@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Рацион питания')
    button2 = types.KeyboardButton('Цена')
    button3 = types.KeyboardButton('Магазины')
    button4 = types.KeyboardButton('План')
    button5 = types.KeyboardButton('Хочу кушать')
    markup.add(button1, button2, button3, button4, button5)
    mess = f'Привет, <b>{message.from_user.first_name}</b>!\nЯ бот EcoProducts'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    bot.send_message(message.chat.id, 'Напиши <strong>/info</strong> чтобы узнать больше обо мне ', parse_mode='html')


@bot.message_handler(commands=['info', 'Info', 'INFO'])
def info(message):
    bot.send_message(message.chat.id, '''Я умею подбирать продукты под ваше финансовое состояние''', parse_mode='html')


# обработка выбранного продукта после того как чел нажимает кнопку Цена
def process_price_input(message):
    product_name = message.text
    chat_id = message.chat.id
    product_prices[chat_id] = product_name
    bot.reply_to(message, f"Вы выбрали продукт: {product_name}")


# обработка выбранного магазина после того как чел нажимает кнопку Магазины
def process_store_input(message):
    store_name = message.text
    chat_id = message.chat.id
    selected_stores[chat_id] = store_name
    bot.reply_to(message, f"Вы выбрали магазин: {store_name}")


# обработка выбранного плана после того как чел нажимает кнопку План
def process_plan_input(message):
    plan_duration = message.text
    chat_id = message.chat.id
    selected_plans[chat_id] = plan_duration
    bot.reply_to(message, f"Вы выбрали продолжительность плана: {plan_duration}")


@bot.message_handler(func=lambda message: message.text == 'Рацион питания')
def handle_ration(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Веганский')
    button2 = types.KeyboardButton('Обычный')
    back_button = types.KeyboardButton('Назад')
    markup.add(button1, button2, back_button)
    bot.reply_to(message, "Выберите рацион:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Цена')
def handle_price(message):
    bot.reply_to(message, "Введите название продукта цену которого вы хотите узнать:")
    bot.register_next_step_handler(message, process_price_input)


@bot.message_handler(func=lambda message: message.text == 'Магазины')
def handle_stores(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Евроспар')
    button2 = types.KeyboardButton('АШАН')
    button3 = types.KeyboardButton('Верный')
    button4 = types.KeyboardButton('METRO')
    button5 = types.KeyboardButton('Перекресток')
    button6 = types.KeyboardButton('Пятерочка')
    back_button = types.KeyboardButton('Назад')
    markup.add(button1, button2, button3, button4, button5, button6, back_button)
    bot.reply_to(message, "Выберите название ближайшего к вам магазина:", reply_markup=markup)
    bot.register_next_step_handler(message, process_store_input)


@bot.message_handler(func=lambda message: message.text == 'План')
def handle_plan(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('1 месяц')
    button2 = types.KeyboardButton('Полгода')
    button3 = types.KeyboardButton('Год')
    back_button = types.KeyboardButton('Назад')
    markup.add(button1,button2,button3,back_button)
    bot.reply_to(message, "Выберите продолжительность плана или введите свою:", reply_markup=markup)
    bot.register_next_step_handler(message, process_plan_input)



@bot.message_handler(func=lambda message: message.text == 'Хочу кушать')
def handle_hungry(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Веганский')
    button2 = types.KeyboardButton('Обычный')
    back_button = types.KeyboardButton('Назад')
    markup.add(button1, button2, back_button)
    bot.reply_to(message, "Выберите рацион:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Веганский')
def handle_vegan_ration(message):
    bot.reply_to(message, "Продукты веганского рациона:")
    for product, price in vegan_products.items():
        bot.send_message(message.chat.id, f"{product} - {price} рублей")


@bot.message_handler(func=lambda message: message.text == 'Обычный')
def handle_regular_ration(message):
    bot.reply_to(message, "Продукты обычного рациона:")
    for product, price in regular_products.items():
        bot.send_message(message.chat.id, f"{product} - {price} рублей")


@bot.message_handler(func=lambda message: message.text == 'Назад')
def handle_back(message):
    start(message)


bot.polling(none_stop=True)
