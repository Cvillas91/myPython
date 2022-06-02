import os
import time
from matplotlib import ticker
import pandas_datareader as web
from winotify import Notification, audio

tickers = ["AAPL"]

#for ticker in tickers:
#    print(web.DataReader(ticker, "yahoo").iloc[-1]['Close'])

upper_limits = [148.70]
lower_limits = [148.60]

while True:
    print('Hi')
    last_prices = [web.DataReader(ticker, "yahoo")["Adj Close"][-1] for ticker in tickers]
    print(last_prices)
    time.sleep(2)
    for i in range(len(tickers)):
        if last_prices[i] > upper_limits[i]:
            toast = Notification(app_id = "Carlos Alarm bot", 
                                title = "Price Alert for " + tickers[i],
                                msg = f"{tickers[i]} has reached a price of {last_prices[i]}. Sell!",
                                icon = os.path.join(os.getcwd(), "sell.png"),
                                duration = "long")
            toast.add_actions(label = "Go To Stockbroker", launch= "https://www.google.com")
            toast.set_audio(audio.LoopingAlarm6,  loop= True)
            toast.show()
        elif last_prices[i] < lower_limits[i]:
            toast = Notification(app_id = "Carlos Alarm bot", 
                                title = "Price Alert for " + tickers[i],
                                msg = f"{tickers[i]} has reached a price of {last_prices[i]}. Buy!",
                                icon = os.path.join(os.getcwd(), "buy.png"),
                                duration = "long")
            toast.add_actions(label = "Go To Stockbroker", launch= "https://www.google.com")
            toast.set_audio(audio.LoopingAlarm8, loop= True)
            toast.show()
        time.sleep(1)
