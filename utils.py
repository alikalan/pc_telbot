import os
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def get_stocks(plz):
    """
    Fetches stock information based on the provided postal code (PLZ).

    This function sends a GET request to a predefined URL with the given postal code
    as a parameter to retrieve stock information.

    Args:
        plz (str): The postal code to check stock availability.

    Returns:
        requests.Response: The response object containing stock information if successful.
        None: If there was an error during the request.

    Logs:
        Debug information about the request URL and response.
        Error information if the request fails.
    """
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
    """
    Converts a dictionary to a formatted text string.

    This function takes a dictionary and converts it into a string where each key-value
    pair is on a new line, formatted as "key: value".

    Args:
        input_dict (dict): The dictionary to convert.

    Returns:
        str: A formatted string representation of the dictionary.
    """
    result = ""
    for key, value in input_dict.items():
        result += f"{key}: {value}\n"
    return result.strip()
