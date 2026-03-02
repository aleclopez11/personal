from flask import Flask
import yfinance
import stocks

# test = yfinance.ticker.Ticker('GOOGL')
# print(test.fast_info)
# print(test.get_info())
# print(test.news)
# print(test)
app = Flask(__name__)


@app.route('/')
def home():
    print('hello world')
    stock_info = stocks.retrieve_stocks()
    print(stock_info)
    print(type(stock_info))
    output = ''
    for key in stock_info:
        output += f'<br>${key}:<br>' 
        for values in stock_info[key]:
            output += f'{values}: {stock_info[key][values]}<br>'
    return(f'app homepage <br>{output}')

if __name__ == '__main__':
    app.run()