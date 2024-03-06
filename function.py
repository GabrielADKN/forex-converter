import json
from dotenv import load_dotenv
import requests
import os
from flask import flash, session, redirect, url_for

def give_symbol(currency_code):
    """
    Retrieves the symbol associated with the given currency code.

    Parameters:
    currency_code (str): The currency code for which to retrieve the symbol.

    Returns:
    str: The symbol associated with the currency code, or 'Unknown Currency Code' if not found.

    Raises:
    FileNotFoundError: If the symbol file is not found.
    JSONDecodeError: If the symbol file has an invalid JSON format.
    Exception: If any other error occurs during the symbol retrieval process.
    """
    try:
        file_path = 'symboles.json'

        with open(file_path, 'r', encoding='utf-8') as file:
            currency_data = json.load(file)

        currencies = currency_data.get('currencies', {})
        
    except FileNotFoundError:
        return f'Error: File {file_path} not found.'
    
    except json.JSONDecodeError:
        return f'Error: Invalid JSON format in {file_path}.'

    except Exception as e:
        return f'Error: {str(e)}'

    return currencies.get(currency_code, 'Unknown Currency Code')

def configure():
    """
    Configure the application by loading environment variables from a .env file.
    """
    load_dotenv()
    
def get_data_api_list():
    """
    Retrieves a list of available currencies from the API.

    Returns:
        dict or str: A dictionary containing the list of currencies if successful, 
                     otherwise a string indicating an error occurred.
    """
    req = requests.get(f'http://api.exchangerate.host/list?access_key={os.getenv("api_key")}')
    
    try:
        return req.json()
    except Exception:
        return 'error'
        
def get_data_api_convert(from_currency, to_currency, amount):
    """
    Retrieves the conversion rate and converted amount from the API.

    Parameters:
    from_currency (str): The currency code of the currency to convert from.
    to_currency (str): The currency code of the currency to convert to.
    amount (str): The amount to convert.

    Returns:
    dict: A dictionary containing the conversion rate and converted amount.
    str: 'error' if an exception occurs during the API request.
    """
    req = requests.get(f'http://api.exchangerate.host/convert?access_key={os.getenv("api_key")}&from={from_currency}&to={to_currency}&amount={amount}&format=1')
        
    try:
        return req.json()
    except Exception:
        return 'error'
    
def message_error_response(resp):
    """
    Displays an error message and returns 'error' if the API response is 'error'.

    Parameters:
    resp (str): The API response.

    Returns:
    str: The string 'error'.
    """
    if resp == 'error':
        flash('API error, please try again!', 'error')
        return 'error'
      
def message_invalid(from_cur=None, to_cur=None, amnt=None):
    """
    Check if the input values for currency conversion are valid.

    Args:
        from_cur (str): The currency to convert from.
        to_cur (str): The currency to convert to.
        amnt (str): The amount to convert.

    Returns:
        str: 'error' if any of the input values are invalid, otherwise None.
    """
    if (from_cur == '' or to_cur == '' or amnt == ''):
        flash('Please fill all the fields', 'error')
        return 'error'
     
    if (from_cur not in session['currencies']):
        flash('Please enter valid value in field : Converting from', 'error')
        return 'error'
        
    if (to_cur not in session['currencies']):
        flash('Please enter valid value in field : Converting to', 'error')
        return 'error'
        
    
    