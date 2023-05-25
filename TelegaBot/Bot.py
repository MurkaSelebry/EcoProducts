import telebot
from telebot import types

bot = telebot.TeleBot('5932020939:AAFC56lTYXkvbWdARlxKHlvP4fqlHn_-AoQ')

@bot.message_handler(commands=['start','help'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>!\nЯ бот EcoProducts'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id,'Напиши <strong>/info</strong> чтобы узнать больше обо мне ', parse_mode='html')

@bot.message_handler(commands=['info', 'Info', 'INFO'])
def info(message):
    bot.send_message(message.chat.id, '''Я умею подбирать продукты под ваше финансовое состояние''', parse_mode='html')

bot.polling(none_stop=True)
