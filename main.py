import telebot

from config import *
from extensions import Convertor, APIException


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Приветствую, {message.chat.username} \n\nЭтот бот конвертирует валюту\nСписок доступных валют /values\n\nЧто, во что и сколько будем переводить?")

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Ввидите команду для бота в формате:\n<валюта> \ <валюта в которую хотим перевести> \ <количество>\n\nСписок доступных команд:\n/start\n/help\n/values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        sym, base, amount = message.text.split()
    except ValueError as e:
        bot.reply_to(message, 'Невернок количество  параметров!')

    try:
        new_price = Convertor.get_price(sym, base, amount)
        bot.reply_to(message, f"Цена {amount} {sym} в {base} : {new_price}")
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")


bot.polling()
