import yfinance
import json


test = yfinance.Ticker('GOOGL')

print(test)
# print(test.info)
keys = ['calendar', 'info', 'financials', 'earnings', 'earnings_dates']
print(test.calendar)
print(test.financials)
print(test.earnings_dates)

out = test.info
for key in out:
    print(key)


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
        except:
            pass

    print(f'heres the output {output}')
    return output