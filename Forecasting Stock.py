# %% [markdown]
# # Homework 7- Forecasting Stock Data
# 
# In this homework, we will work with stock data. Python has a built in function that will pull stock data from Yahoo Finance, how cool!
# 
# First, you need to install yfinance:

# %%
# you may need to run this in the anaconda prompt
# in anaconda, open powershell prompt
# type in the following
# on a mac use pip3 instead of pip

!pip install yfinance

# %%
import yfinance as yf
import pandas as pd 
pd.options.display.float_format = '{:,.2f}'.format

# %% [markdown]
# ## Importing Stock Data Directly from the Internet
# 
# ```python
# 
# name = yf.Ticker("stock_code")
# ```
# 
# Where ``stock_code`` is a stock's stock exchange trading acronym. This code will return a reference to all of that Company's data stored on yahoo finance.
# 
# To access various data for that company we can use:
# 
# ```python
# 
# # general information
# name.info
# 
# # stock data as pandas dataframe
# name.history(period='1mo', interval='1d', start=None, end=None)
# ```
# 
# Where:
# - ``period`` is the length of time you want data for 
#     - Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# 
# - ``interval`` how often stock price data is calculated
#     - Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
#       
# - ``start`` instead of providing a period, you can provide start and end dates
#     - start date string YYYY-MM-DD
# - ``end`` Default is now. If do not enter this argument, you will receive 1 month of data ending today
# 
# Interestingly, you can also pull limited financial statement information from Yahoo Finance:
# 
# ```python
# # income statement items
# name.financials
# 
# # balance sheet
# name.balance_sheet
# 
# # cash flows
# name.cashflow
# 
# # sustainability data
# name.sustainability
# ```
# 
# You can read more here: https://github.com/ranaroussi/yfinance
# 
# <font color='blue' size = '5'> Task 1 </font>
# 
# For now, pull Coca Cola's Yahoo Finance data using ticker KO. Then:
# 
# 1. Look at Coke's info, peruse what information is given
# 2. Pull 5 years worth of daily stock values ending 11/1/2022. Name this dataframe so that you can access it in the future
# 4. Run the following code to remove timezone from the index ``df.index = df.index.tz_localize(None)``
# 3. Reset the index so that date is a column instead of the index
# 
# 
# **Note** Yahoo finance's stock price data adjusts backwards for stock splits. This keeps the data comparable over time. I don't think that Coke has done any stock splits in the recent past.

# %%
#1
CocaCola = yf.Ticker("KO")

# %%
#1 
CocaCola.info

# %%
#2
coke = CocaCola.history(period='5y', interval='1d', start='2017-10-26', end='2022-11-02')
coke

# %%
#3 
coke.index = coke.index.tz_localize(None)

# %%
#4 Reset the index so that date is a column instead of the index
coke.reset_index(inplace=True)
coke

# %% [markdown]
# <font color='blue' size = '5'> Task 2 </font>
# 
# Import your standard graphing libraries.
# 
# Use a seaborn relplot to plot Coke’s closing stock price over the last 5 years (the data you have). Set the size of the dots to equal the volume of trades divided by 1 million. Make sure the visualization is wide enough.

# %%
import seaborn as sns

size = coke['Volume']/1000000
sns.relplot(x= 'Date', y='Close', data= coke, kind = 'scatter', size= size)

# %%
sns.relplot(x= 'Date', y='Close', data= coke, kind = 'scatter', size= size, height = 5, aspect = 2)

# %% [markdown]
# <font color='blue' size = '5'> Task 3 </font>
# 
# Create a column that counts the number of days from your first observation of Coke's stock price to each observation. Note that we do not have data for stock price on weekends or holidays. Think through if that should affect your count or not. **Make a note of your decision.**
# 
# Then, run a regression of stock price on time.

# %%
coke['number_of_days'] = coke['Date'] - coke['Date'][0]

# %%
number_of_days = coke.index
coke['number_of_days'] = number_of_days
coke

# %%
import statsmodels.formula.api as smf

model = smf.ols('Close ~ number_of_days', data = coke).fit()

model.summary()

# %% [markdown]
# <font color='red' size = '5'> Question 1 </font>
# 
# How do you interpret your output? Specifically, how you interpret the coefficients? Do they make sense to you?

# %% [markdown]
# By looking at the regression model and the graph, for the past 5 years, Coke's stock price started from 36.47 and it is increasing 0.0188 per day.
# However, this doesn't explain the dips in the graph (e.g 2020, 2022). So, we would have to predict coke's actual stock price by using data we don't have yet in the next upcoming questions.

# %% [markdown]
# <font color='blue' size = '5'> Task 4 </font>
# 
# In a perfect stock market, stock price changes over a long period of time will reflect investor's expected return. However, on a day to day basis, stock price should not be predictable. This is because stock price should fully incorporate all information as soon as the information is publicly available. Future stock price changes will only reflect new information and thus should not be predictable. However for the sake of practice, lets try to forecast Coke's future stock price. 
# 
# First, build a forecast model that assumes there is no seasonality in the data but that there is a trend. Fit the model and display its results.

# %%
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

# %%
variable = 'Close'

# %%
# simple exponential smoothning needed to optimize alpha

# fit an SES model and view results
sesmodel = SimpleExpSmoothing(coke_original[variable]).fit()


sesmodel.summary()
# In between 0 and 1, 97% is a permanent shift up or down and 3% is random fluctuation
# The SES model predicts that if we have all of the observations available, there would be a demand of 39.3

# %%
# save result for graphing later

alpha = sesmodel.params['smoothing_level']
alpha

# %%
# another way to quickly calculate forecasted values
# from an optimized SES model

coke['forecast_ses'] = sesmodel.fittedvalues

# we didn't used outersample yet, so no need to forecast out of sample in the next question

# %% [markdown]
# <font color='red' size = '5'> Question 2 </font>
# 
# Use coding to predict Coke's stock price over the upcoming week. 
# 
# Is price expected to go up or down? Interpret in the context of what stock price has been doing lately.

# %%
coke.tail()

# %%
# add 5 number_of_days (it ended at 'number_of_days': 1262) to calculate forecast out of sample
extra = pd.DataFrame({'number_of_days' : [1258, 1259, 1260, 1261, 1262]})

extra

# %%
# append it to our existing 'coke' dataframe
coke = coke.append(extra, ignore_index=True)

coke.tail()

# %%
# create and run model
# holt needed to optimize beta
desmodel = Holt(coke[variable]).fit()

desmodel.summary()

# %%
# calculate 
coke['des_forecast'] = desmodel.fittedvalues

# out of sample forecast
coke['des_forecast'].fillna(desmodel.forecast(5), inplace=True)
coke.head(10)

# %%
b = desmodel.params['smoothing_level']

c = desmodel.params['smoothing_trend']

# %% [markdown]
# coke's stock price is expected to go up over the upcoming week due to closing prices increasing overweighing closing prices decreasing. 
# we can also graph our outsampled holt model and see that the trend is increasing.

# %% [markdown]
# <font color='red' size = '5'> Question 3 </font>
# 
# a. How do you interpret the 'smoothing_level' or $\alpha$ in your forecast?
# - 
# 
# b. How do you interpret the 'smoothing_trend' or $\beta$ in your forecast?
# - 

# %% [markdown]
# ## a. 
# For the insample, in between 0 and 1, 97% is a permanent shift up or down and 3% is random fluctuation. 
# For the outsample, in between 0 and 1, 0.005 is a permanent shift up or down and 0.995 is a random fluctuation. 
# The change in a lower alpha value suggests less emphasis on newer demand and more emphasis on older demand.
# ## b. 
# beta of 0.001 from our holt model is almost close to 0, this shows us that the holt model is close to our ses model and how we are close to fit the actual data. It also shows the trend of the forecast between the predictor variable and the dependent variable, as in, for every one unit increase in days, coke's stock price increases by 0.001.

# %% [markdown]
# #### <font color='blue' size = '5'> Task 5 </font>
# 
# Graph the fitted values of your forecast (in sample) as well as your estimated forecast for the next week (out of sample) against Coke's actual stock price over the last two years. Make sure your graph is nice and wide and that the X-axis is date.

# %%
import matplotlib.pyplot as plt

# %%
# Insample forecast graph

fig, ax = plt.subplots(figsize = (18, 8), nrows=1, ncols=1)

ax.plot(coke[variable], marker='o', color='black', label = 'Actual Stock Price')
ax.plot(coke['forecast_ses'], marker='o', color='blue', label = fr'Forecast $\alpha =$ {alpha: .2f}')

ax.legend()
plt.ylabel(variable)
plt.xlabel('Date')

# %%
# Outsample forecast graph

fig, ax = plt.subplots(figsize = (18, 8), nrows=1, ncols=1)

ax.plot(coke['Date'], coke[variable], marker='o', color='black', label = 'Actual Stock Price')
ax.plot(coke['Date'], coke['forecast_ses'], marker='o', color='blue', label = fr'Forecast $\alpha =$ {alpha: .2f}')
ax.plot(coke['Date'], coke['des_forecast'], marker='o', color='red', label = fr'Forecast $\alpha =$ {b: .2f} $\gamma =$ {c: .2f}')

ax.legend()
plt.ylabel(variable)
plt.xlabel('Date')

# %% [markdown]
# <font color='red' size = '5'> Question 4 </font>
# 
# Is there seasonality in the data? If so, how many seasons? How do you know? Do the statistics make any sense theoretically? (if you are uncomfortable interpretting stock data do your best, I will not test you on your asset pricing acumen).
# 
# Hint: Writing a loop to test different autocorrelations may be helpful here. 
# 
# 

# %% [markdown]
# *Your Answer Here*

# %%
coke['error'] = coke[variable] - coke['des_forecast']
coke[['error']].describe()

# %%
coke['error'].autocorr(6)

# purpose of seasonality is to get rid of autocorrelation (make my errors better). 
# there are 6 periods of seasonality in the data because the autocreelation of 6 is the maximum depth of seasonality that returns the value below the cutoff of 0.056
# if we have 7 periods of seasonaliy in the data, it returns a value beyond the cutoff and indicates that my autocorrelation is too high  

# %%
import math
2/math.sqrt(coke['error'].count())

# my cutoff is 0.056

# %%
coke['error'].autocorr(lag=1)
# when lag is 1, we are below the cut off
# lag is looking at every 5 days do stocks tend to move in the same day
# lag is between 1 and 6 in order to stay below the cutoff --> every 1 period to 6 periods, there's a correlation of errors

# %%
# create loop to check lag result is higer than the cutoff
for i in range (1, 730):
    test = coke['error'].autocorr(i)
    if (test >= 0.05627666078833527):
        print(i, test)


