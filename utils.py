import os
import requests

def get_stocks(plz):
    url = os.environ.get('URL')

    stocks = requests.get(url, params = {"plz": plz})

    return stocks

def dict_to_text(input_dict):
    result = ""
    for key, value in input_dict.items():
        result += f"{key}: {value}\n"
    return result.strip()
