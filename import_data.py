import yfinance as yf

data = yf.download("SPY", start="2017-01-01", end="2021-07-30")
data.to_csv("spy.csv")
