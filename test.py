import stocks

stock_info = stocks.retrieve_stocks()

print(stock_info)

for key in stock_info:
    print(key)
    # stocks.current_trend(stock_info[key])
    for values in stock_info[key]:
        print(values)
        # print(type(values))
        print(stock_info[key][values])