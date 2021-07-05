"""
middle band = Simple Moving Average 20 days SMA(20)
upper band = SMA + 2*std of close price
lower band = SMA - 2*std of close price
"""

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

item = '005930.KS'
WINDOW = 20

df = yf.download(item, start='2018-01-01')
breakpoint()
df['SMA'] = df.Close.rolling(window=WINDOW).mean()
df['stddev'] = df.Close.rolling(window=WINDOW).std()
df['Upper'] = df.SMA + 2 * df.stddev
df['Lower'] = df.SMA - 2 * df.stddev
breakpoint()

df['Buy_Signal'] = np.where(df.Lower > df.Close, True, False)
df['Sell_Signal'] = np.where(df.Upper < df.Close, True, False)

df = df.dropna()

breakpoint()


plt.figure(figsize=(12, 6))
plt.plot(df[['Close', 'SMA', 'Upper', 'Lower']])
plt.scatter(df.index[df.Buy_Signal], df[df.Buy_Signal].Close, marker='^', color='g')
plt.scatter(df.index[df.Sell_Signal], df[df.Sell_Signal].Close, marker='v', color='g')
plt.fill_between(df.index, df.Upper, df.Lower, color ='grey', alpha=0.3)
plt.legend(['Close', 'SMA', 'Upper', 'Lower'])
plt.show()

breakpoint()
"""
Crossing
"""

buys = []
sells = []
open_pos = False
for i in range(len(df)):
  if df.Lower[i] >df.Close[i]:
    if open_pos == False:
      buys.append(i)
      open_pos = True
  elif df.Upper[i] < df.Close[i]:
    if open_pos:
      sells.append(i)
      open_pos= False


plt.figure(figsize=(12, 6))
plt.plot(df[['Close', 'SMA', 'Upper', 'Lower']])
plt.scatter(df.iloc[buys].index, df.iloc[buys].Close, marker='^', color='g')
plt.scatter(df.iloc[sells].index, df.iloc[sells].Close, marker='v', color='g')
plt.fill_between(df.index, df.Upper, df.Lower, color ='grey', alpha=0.3)
plt.legend(['Close', 'SMA', 'Upper', 'Lower'])
plt.show()

breakpoint()
# backtest
merged = pd.concat([df.iloc[buys].Close, df.iloc[sells].Close], axis=1)

merged.columns = ['Buys', 'Sells']

breakpoint()

totalprofit = merged.shift(-1).Sells - merged.Buys

relprofits = (merged.shift(-1).Sells - merged.Buys)/merged.Buys

print(relprofits.mean())

breakpoint()
