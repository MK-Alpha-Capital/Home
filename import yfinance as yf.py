import yfinance as yf
import pandas as pd

def find_growth_stocks():
    # Technologie-Aktienliste abrufen
    tech_tickers = yf.Tickers('XLK')
    tech_stocks = tech_tickers.tickers
    stock_list = pd.DataFrame()
    for stock in tech_stocks:
        stock_list = stock_list.append(yf.download(stock))

    # Finanzkennzahlen berechnen
    stock_list['P/E'] = stock_list['Close'] / stock_list['Earnings per Share']
    stock_list['EPS_growth'] = stock_list['Earnings per Share'].pct_change()

    # Aktien filtern
    growth_stocks = stock_list[(stock_list['EPS_growth'] > 0) & (stock_list['P/E'] < 20) & (stock_list['Market Cap'] < 5000000000)]

    # Ergebnisse anzeigen
    print(growth_stocks)

find_growth_stocks()
