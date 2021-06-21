from pandas_datareader import data as pdr
import yfinance as yf
from datetime import date, datetime, timedelta

def get_sample_data(code ='005930.KS' , yr=3, adjust_price=False):
  yf.pdr_override()
  today = datetime.now().date()
  y_ago = (datetime.now() - timedelta(days=yr * 365)).date()

  return pdr.get_data_yahoo(code, start=y_ago, end=today , adjust_price=False)


sample_data = get_sample_data()

breakpoint()

