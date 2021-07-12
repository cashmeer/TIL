from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf
plt.style.use('fivethirtyeight')

assets = ['FB', "AMZN", "AAPL", "NFLX", "GOOG"]
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

stockStartDate = "2018-01-01"

today= datetime.today().strftime('%Y-%m-%d')

df = pd.DataFrame()

for stock in assets:
  df[stock] = yf.download(stock, start=stockStartDate, end=today)['Close']
  #breakpoint()
  #df[stock] = yf.download(stock,start=)['Close']


returns = df.pct_change()
# 252 거래일수
cov_matrix_annual = returns.cov() * 252
print(cov_matrix_annual)
port_variance = np.dot(weights.T, np.dot(cov_matrix_annual, weights))
print(port_variance)
port_volatility = np.sqrt(port_variance)
print(port_volatility)
port_simpleAnnualReturn = np.sum(returns.mean()*weights) * 252
print(port_simpleAnnualReturn)


breakpoint()

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

mu = expected_returns.mean_historical_return(df)
S = risk_models.sample_cov(df)

ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe()
cleaned_weight  = ef.clean_weights()
print(cleaned_weight)
print(ef.portfolio_performance(verbose=True))

breakpoint()
