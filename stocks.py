import yfinance
import json



def retrieve_stocks():
    stocks = json.load(open('settings.json'))

    output = {}

    for stock in stocks['stocks']:
        print('getting info')
        output[stock] = get_stock_info(stock)

    return output

def get_stock_info(ticker):
    stock = yfinance.Ticker(ticker)
    print(stock)
    output = {}

    stock = stock.info

    keys = ['previousClose', 'open', 'dayLow', 'dayHigh', 'dividendRate', 'dividendYield', 'volume', 'averageVolume', 'averageVolume10days',
            'bid', 'ask', 'marketCap', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'allTimeHigh', 'profitMargins', 'floatShares', 'sharesOutstanding',
            'sharesShort', 'shortRatio', 'currentPrice', 'targetHighPrice', 'targetLowPrice', 'targetMedianPrice', 'totalCash', 'ebitda',
            'totalDebt', 'quickRatio', 'currentRatio', 'totalRevenue', 'grossProfits', 'freeCashflow']

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