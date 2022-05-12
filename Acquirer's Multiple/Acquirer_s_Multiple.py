import pandas as pd
import yfinance as yf

def s():
    x = input("Enter Your Company Ticker: ")

    str1 = "https://www.marketwatch.com/investing/stock/{}/company-profile?mod=mw_quote_tab"
    url = str1.format(x)

    df = pd.read_html(url, header=0)
    df1 = df[4]

    stock = yf.Ticker(x)
    currentprice = stock.history()
    last_quote = (currentprice.tail(1)['Close'].iloc[0])

    acqmult = df1.iloc[5, 1]
    deepvalue = 3*acqmult
    cheapvalue = 5*acqmult

    print("{} has an Acquirer's Multiple of {}".format(x.upper(), acqmult))
    print("{} last traded price is {}".format(x.upper(), round(last_quote, 2)))
    print("{} has a Deep Value of\n>".format(x.upper()), "$"+str(deepvalue))
    print("{} has a Cheap Value of\n>".format(x.upper()), "$"+str(cheapvalue))
    y_n()
def y_n ():
    j = input("Check Another Stock(Y/n)?:")
    if j.upper() == 'Y':
        print("------------------------------------")
        s()
    elif j.upper() == 'N':
        exit()
    else:
        print("Invalid Input, Try Again!")
        y_n()

s()