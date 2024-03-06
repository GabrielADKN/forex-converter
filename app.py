from flask import Flask, request, redirect, url_for, render_template, session, flash
from function import give_symbol, configure, get_data_api_convert, get_data_api_list, message_invalid, message_error_response
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = '123456'

# toolbar = DebugToolbarExtension(app)
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def index():  
    """
    This function serves as the main route for the Forex Converter application.
    It retrieves data from an API, handles error messages, and renders the index.html template.

    Returns:
        The rendered index.html template with the retrieved currencies.
    """
    response = get_data_api_list()
    message = message_error_response(response)
    if message == 'error':
        return redirect(url_for('index'))
    
    currencies = response["currencies"]
    session['currencies'] = currencies
    return render_template('index.html', currencies=currencies)
    
@app.route('/convert', methods=['POST'])
def convert():    
    """
    Converts the specified amount from one currency to another.

    Returns:
        The rendered template with the conversion result.
    """
    from_currency = request.form['from']
    to_currency = request.form['to']
    amount = request.form['amount']
     
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    
    message = message_invalid(from_cur=from_currency, to_cur=to_currency, amnt=amount)
    if message == 'error':
        return redirect(url_for('index'))

    if float(amount)<0 :
        flash('Please enter a valid amount in the form below','error')
        return redirect(url_for('index'))
    
    response = get_data_api_convert(from_currency, to_currency, amount)
    message = message_error_response(response)
    if message == 'error':
        return redirect(url_for('index'))
        
    price = response["result"]
    symbole_to = give_symbol(to_currency)
    symbole_from = give_symbol(from_currency)
    result = {'from': from_currency, 'to': to_currency, 'amount': amount, 'price': price,'symbole_to': symbole_to,'symbole_from': symbole_from}
    
    return render_template('convert.html', response=result)

if __name__ == '__main__':
    configure()
    app.run()