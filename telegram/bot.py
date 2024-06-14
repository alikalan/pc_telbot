import os
import telebot
from utils import get_stocks, dict_to_text

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Gib mir eine Postleitzahl und ich zeige dir welche DM-Filialen in der Nähe wie viele Pistazienschnitte auf Lager haben!")

@bot.message_handler(func=lambda msg: True)
def send_stocks(message):
    stocks = get_stocks(message)
    reply = dict_to_text(stocks.json())
    bot.reply_to(message, reply)
    # for store, stock in stocks.items():
    #     bot.reply_to(message, f"{store}, {stock}")

bot.infinity_polling()
