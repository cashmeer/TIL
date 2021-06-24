import yfinance as yf
import pandas as pd
from causalimpact import CausalImpact


# training_start = "2018-01-02"
# training_end = "2018-09-05"
#
# treatment_start = "2018-09-06"
# treatment_end = "2018-09-07"
#
# end_stock = "2018-09-08"


training_start = "2021-03-11"
training_end = "2021-06-16"

treatment_start = '2021-06-17'
treatment_end = '2021-06-18'

end_stock = "2021-06-21"
# get the date
coupang = 'CPNG'
stocks = ['CPNG', 'AMZN', "SHOP"]
dataset = yf.download(stocks, start= training_start, end= end_stock, interval="1d")


#getting data we want
dataset = dataset.iloc[:, :6]

dataset.columns = dataset.columns.droplevel()
dataset = dataset.dropna()

#getting dataset of only the training period

dataset_correlation = dataset[dataset.index <= training_end]
pd.set_option('display.max_column', None)
print(dataset_correlation.corr())

final_stocks = dataset[['CPNG', 'AMZN', "SHOP"]]

breakpoint()


#pre end post period

pre_period = [training_start, training_end]
post_period = [treatment_start, treatment_end]

# doind causal impact
breakpoint()


impact = CausalImpact(data=final_stocks, pre_period=pre_period,post_period=post_period)


#check result

#plot()

#print(impact.summary())
breakpoint()





