import yfinance
import json



def retrieve_stocks():
    config = json.load(open('settings.json'))
    stocks = config['stocks']
    keys = config['keys']

    output = {}

    for stock in stocks:
        print('getting info')
        output[stock] = get_stock_info(stock, keys)

    return output

def get_stock_info(ticker, keys):
    stock = yfinance.Ticker(ticker)
    print(stock)
    output = {}

    stock = stock.info

    for key in keys:
        try:
            output[key] = stock[key]
            # output.append(f'{key}: {stock[key]}')
        except:
            pass
    output['trend'] = current_trend(output)
    return output

def current_trend(ticker):
    
    previous_close = ticker['previousClose']
    current = ticker['currentPrice']

    diff = current - previous_close

    trend = diff / previous_close * 100

    return f'{trend:.2f}'