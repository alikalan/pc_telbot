import os
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def get_stocks(plz):
    url = os.environ.get('URL')
    logging.debug(f"Fetching stocks for PLZ: {plz} from URL: {url}")

    try:
        stocks = requests.get(url, params={"plz": plz})
        logging.debug(f"Stocks response: {stocks.json()}")
        return stocks
    except Exception as e:
        logging.error(f"Error fetching stocks: {e}")
        return None

def dict_to_text(input_dict):
    result = ""
    for key, value in input_dict.items():
        result += f"{key}: {value}\n"
    return result.strip()
