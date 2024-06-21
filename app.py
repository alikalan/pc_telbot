import os
import telebot
from flask import Flask, request, jsonify
from utils import get_stocks, dict_to_text
import logging

app = Flask(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(level=logging.DEBUG)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Gib mir eine Postleitzahl und ich zeige dir welche DM-Filialen in der Nähe wie viele Pistazienschnitte auf Lager haben!")

@bot.message_handler(func=lambda msg: True)
def send_stocks(message):
    logging.debug(f"Received message: {message.text}")
    stocks = get_stocks(message.text.strip("/"))
    logging.debug(f"Stocks response: {stocks}")

    try:
        reply = dict_to_text(stocks.json())
        logging.debug(f"pretty reply: {reply}")
    except Exception as e:
        logging.error(f"Error processing stocks response: {e}")
        reply = f"There was a problem! The response from the server was {stocks}"

    bot.reply_to(message, reply)

@app.route('/')
def landing():
    return "Ok"

@app.route('/webhook', methods=['POST'])
def webhook():
    logging.debug("Received webhook request")
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        logging.debug(f"Webhook payload: {json_string}")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return jsonify(status='ok')
    else:
        logging.error("Invalid content-type")
        return jsonify(status='error', message='Invalid content-type')

if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=8000)
