import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader as web
import pandas as pd
import datetime as dt


start = dt.datetime(2021,1,1)
end = dt.datetime.now()

tickers = ["FB","GS","NVDA","TSLA","MSFT","AAPL","CCL","BA"]
colnames = []

for ticker in tickers :
    data = web.DataReader(ticker, "yahoo", start, end)
    if len(colnames) == 0:
        combined = data [['Adj Close']].copy()
        colnames.append(ticker)
        combined.columns = colnames
    else :
        combined = combined.join(data['Adj Close'])
        colnames.append(ticker)
        combined.columns = colnames

'''
plt.yscale("log")

for ticker in tickers :
    plt.plot(combined[ticker], label = ticker)

plt.legend(loc = "upper right")
plt.show() '''

corr_data = combined.pct_change().corr(method = "pearson")
sns.heatmap(corr_data, annot = True, cmap = "coolwarm")

plt.show()
