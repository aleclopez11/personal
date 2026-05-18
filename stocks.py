import yfinance
import json
import datetime



def retrieve_stocks(user):
    print(user)
    config = json.load(open('settings.json'))
    stocks = config['stocks']
    keys = config['keys']

    output = {}

    for stock in stocks:
        print('getting info')
        output[stock] = get_stock_info(stock, keys)

    return output

async def refresh_data():
    # while True:
    print('running refresh of stock data')
    stock_info = {}
    now = datetime.datetime.now()
    weekday = now.weekday()
    time = now.time()
    start_time = datetime.time(9, 30)  # 9:30 AM
    end_time = datetime.time(16, 0)    # 4:00 PM
    if weekday < 5 and (start_time <= time <= end_time):
        print('refreshing data')
        stock_info = retrieve_stocks()
    # await asyncio.sleep(300)  # Refresh every 5 minutes (300 seconds)
    return stock_info

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