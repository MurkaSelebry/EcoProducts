import telebot
from telebot import types

bot = telebot.TeleBot('5932020939:AAFC56lTYXkvbWdARlxKHlvP4fqlHn_-AoQ')


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


bot.polling(none_stop=True)
