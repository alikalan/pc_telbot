import os
import requests

"""
Sets the webhook for the Telegram bot.

This script retrieves the bot token and webhook URL from environment variables
and sets the webhook for the Telegram bot using the Telegram Bot API.

Environment Variables:
    BOT_TOKEN (str): The token for the Telegram bot.
    WEBHOOK_URL (str): The URL to set as the webhook for the bot.

Returns:
    None

Prints:
    dict: The JSON response from the Telegram API indicating the success or failure
    of setting the webhook.
"""

# Fetch the bot token and webhook URL from environment variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')

# Set the webhook for the Telegram bot
response = requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}')

# Print the response from the Telegram API
print(response.json())
