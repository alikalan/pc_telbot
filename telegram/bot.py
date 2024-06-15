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
    stocks = get_stocks(message.text.strip("/"))

    try:
        reply = dict_to_text(stocks.json())
    except:
        reply = f"There was a problem! The response from the server was {stocks}"

    bot.reply_to(message, reply)

bot.infinity_polling()
