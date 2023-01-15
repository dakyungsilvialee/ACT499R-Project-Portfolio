# %% [markdown]
# # Homework 8
# 
# ## Part I
# Read the the following pages from *Text Based Network Industries and Endogenous Product Differentiation* by Hoberg and Phillips; *Journal of Political Economy* 2016. 
# 
# - pg 1423- end of first paragraph on 1425
# - pg 1427- paragraph starting with 'Although it is convenient to use...' - 
# 
# This paper uses clustering (which we will learn about next week) to develop industry classifications. 
# 
# The paper is available on Canvas under 'Library Course Reserves'.
# 
# <font color = 'blue'> <font size = 4> 
# **Question 1:**  </font> What did you find most interesting in your reading?
#  
# 
#     
# <font color = 'blue'> <font size = 4>
# **Question 2:** </font> In your own words, what are the limitations of more traditional industry classification measures?

# %% [markdown]
# **Answers to Q1 and Q2 Above:**
# 
# Q1. In order to identify and classify firms, the paper suggested using a business description of the company's 10-k document as a historical dataset and group by products that are sold based on the customers' preferences by assigning a spatial location based on the product description.
# 
# Q2. 
# 
# 
# First, the original methods of classifying firms, SIC and NAICS, neither takes into consideration of reclassification as time is revolving and the market is changing. \
# Second, SIC and NAICS can't easily tailor towards innovations within the new product market. \
# Third, SIC and NAICS assumes a relation between three firms, where one of them holds between the two firms. This might not always be the case in a real life market, because the two firms that are rivals to a third firm might not be rivals. \
# Finally, the original method doesn't provide a metric of similarity both within and across industries. 
# 
# 
# ----------

# %% [markdown]
# ## Part II
# 
# In this part, you will forecast Home Depot's operating cash flows and estimate a confidence interval for your predictions. Follow the instructions below.

# %% [markdown]
# ### Clean the Data
# 
# Review the code I use below to practice your coding skills and to become familiar with the data.

# %%
# database tools
import pandas as pd 
import numpy as np

# import graphing tools
import seaborn as sns
import matplotlib.pyplot as plt

# import regression library 
import statsmodels.formula.api as smf

# import forecasting library-- new import today
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt

#import missing values
from numpy import NaN, nan, NAN

# format floats to have thousands separators and two decimals
pd.options.display.float_format = '{:,.2f}'.format

# %%
# import quarterly data from Compustat
quarterly = pd.read_csv('quarterlydata.csv')

quarterly.info()

# %%
# import annual data from compustat
annual = pd.read_csv('annualdata.csv')

annual.info()

# %%
# merge quarterly and annual data
data = quarterly.merge(annual, on = ['gvkey', 'datadate'], how = 'outer')

data.head()

# %% [markdown]
# <font color = 'blue'> <font size = 4>
#     
# **Question 3**
#     
# </font>
# 
# Using your understanding of the data and the assignment, why do you think I used an outer merge? What does an outer merge accomplish? 
#     
# - If we use "how = 'merge', that would default to an inner merge and make the data overlap. Thus, we need to specify outermerge. basically we need both quarterly and annual data
# - we used an outermerge to combine all the dataframes that have null values into one, in order to analyze effeciently.
#     

# %% [markdown]
# **Q3 Answer**

# %%
# US currency
data = data[data['curcdq'] == 'USD']

# %%
# some duplicate columns from merge
data = data[['gvkey', 'datadate', 'fyearq', 'fqtr', 'tic_x', 'conm_x', 'datacqtr',
       'datafqtr', 'niq', 'piq', 'oancfy', 'oiadpy',  'cik_x', 'gind', 'idbflag', 
             'naics', 'ipodate', 'fyear', 'oancf', 'oiadp', 'fic']]

# %%
# rename
data.columns = ['gvkey', 'datadate', 'fyearq', 'fqtr', 'tic', 'company',
'datacqtr', 'datafqtr', 'netincome_q', 'pretaxinc_q', 'opercf_fy', 'operinc_q',
'cik', 'industry', 'intl_dom', 'naics', 'ipodate', 'fyear',
 'opercf_annual', 'operinc_annual', 'country']

# %% [markdown]
# <font color = 'red'> <font size = 4>
# **Task 1**
# 
# Annotate the cleaning loop below.

# %%
# assign list called 'fix' with columns: 'fyearq', 'fqtr','cik', 'industry', 'naics', 'ipodate', 'fyear'
fix = ['fyearq', 'fqtr','cik', 'industry', 'naics', 'ipodate', 'fyear']

# %%
# when a value from the 'fix' list goes inside the loop, convert to string and then drop the two digits then print
for i in fix:
    data[i] = data[i].astype('str')

    data[i] = data[i].str[:-2]

    print(data[i].head())

# %%
# convert 'datadate' column's format into %Y%m%d
data['datadate'] = pd.to_datetime(data['datadate'], format = '%Y%m%d')
# convert gvkey as string
data['gvkey'] = data['gvkey'].astype('str')
# check result
data.head()

# %% [markdown]
# <font color = 'red'> <font size = 4>  
# **Task 2**
#     
# </font> </font>
#     
# Quarterly operating cash flows are cumulative from the beginning of the year. Meaning the operating cash flows reported for Q2 are the operating cash flows from the beginning of the year through the end of Q2 and the operating cash flows reported for Q3 are the total operating cash flows from the beginning of the year through the end of Q3. 
#     
# Write a code below to create a new column that reports quarterly operating cash flows as a noncumulative number- i.e. the value for Q2 is the operating cash flows from the end of Q1 to the end of Q2 and the operating cash flows reported for Q3 is the operating cash flows from the end of Q2 to the end of Q3. 

# %%
# we want to group by the company identifier 'gvkey' and the reported year 'fyearq'  
data['non_cumulative'] = np.where(data['fqtr']=='1', data['operinc_q'], data.groupby(['gvkey','fyearq' ])['operinc_q'].diff())

# %%
data

# %% [markdown]
# <font color = 'red'> <font size = 4> 
# **Task 3**
#     
# </font> </font>
# 
# Use exponential smoothing to predict Home Depot's (HOME DEPOT INC) quarterly operating cash flows. **Use all but the last 4 quarters to build your model.**
# 
# Note- you will need to remove the first observation that has a missing value for quarterly operating cash flows for your model to work.

# %%
# subset home depot
data2 = data[data['company'] == 'HOME DEPOT INC']
data2.head()

# %%
# drop first row (observation) that has a missing value for quarterly operating cash flows
data2_resetindex = data2.reset_index(drop=True)
data3 = data2_resetindex.iloc[1: , :]
data3.head()

# %%
data3.tail()

# %%
# Use all but the last 4 quarters to build your model 

data4 = data3.iloc[0:-4]
data4.tail()

# %%
data4.head()

# %%
# use the shortened df that you dropped the last 4 and save it to new df -> ses model
# run model on the last 4 dropped observations we observe

model4 = ExponentialSmoothing(data4['non_cumulative'], seasonal_periods = 4, trend = 'add', seasonal = 'mul').fit()
model4.summary()

# %% [markdown]
# <font color = 'blue'> <font size = 4>
#     
# **Question 4**
#     
# </font> </font>
#     
# Interpret and explain the values provided for the four 'initial_seasons'.

# %% [markdown]
# **Question 4 Answer**
# 
# Depending on the seasonality (the different quarters) of the data, season 0 (quarter 1) has 0.43, season 1 (quarter 2) has 0.67, season 2 (quarter 3) has 0.48, season 3 (quarter 4) has 0.35 of permanent shifts.
# 

# %% [markdown]
# <font color = 'red'> <font size = 4>
# **Task 4**
#     
# </font> </font>
# 
# Predict quarterly operating cash flows through Home Depot's second quarter of fiscal year 2022. Use your model to predict both in sample and out of sample quarterly operating cash flows. 

# %%
# use shortened df 'data4' and predict quarterly operating cash flows
# in sample forecast
data4['tes_forecast'] = model4.fittedvalues
data4.head()

# %%
# out of sample forecast
model4.forecast(4)

# %% [markdown]
# <font color = 'red'> <font size = 4>
# **Task 5**
#     
# </font> </font>
# 
# Plot your predicted and actual values on the same graph. Use a lineplot that has dots at each point, like a combination line and scatterplot.

# %%
# plot forecasts
plt.figure(figsize=(30, 10))
plt.plot(data4['non_cumulative'], marker='o', color='black', label= 'Actual Quarterly Operating Cash Flow')
plt.plot(data4['tes_forecast'], marker='o', color='red', label= 'TES Forecast')

plt.legend(prop={'size':20})
plt.ylabel('Home Depot Uncumulative Quarterly Operating Cash Flow', size = 20)
plt.xlabel('Quarters Passed', size = 20)

# %% [markdown]
# <font color = 'red'> <font size = 4>
# **Task 6**
#     
# </font> </font>
# 
# Calculate your insample forecast errors and describe them numerically.

# %%
data4['tes_error'] = data4['non_cumulative'] - data4['tes_forecast']
data4.head()

# %%
# keep the columns we need and see how many insampe and outsample error there is
data4 = data4[['non_cumulative', 'tes_forecast', 'tes_error']]
data4

# %%
data4[['non_cumulative', 'tes_forecast', 'tes_error']].describe()

# %% [markdown]
# <font color = 'red'> <font size = 4>
# **Task 7**
#     
# </font> </font>
# 
# Simulate 1000 forecast errors for each quarter that we forecasted (both in and out of sample). Use this simulation to create a 95% confidence interval around your forecast.

# %%
# Simulate 1000 forecast errors 
# total of 50 periods (46 from insample, 4 from outsample)
simulated_errors = np.random.normal(loc= data4['tes_error'].mean(), scale = np.std(data4['tes_error']) , size = (1000, 50))
# turn the results into a pandas dataframe
simulated_errors = pd.DataFrame(simulated_errors)

#view the results
simulated_errors

# %%
# turn a 95% confidence interval around your forecast 
upper = .975

lower = .025

# %%
# calculate the 97.5 quantile of forecast errors for each period

simulated_errors.quantile(upper, axis = 0)

# %%
# the above values are the upper end of our forecast error confidence interval

data4['upper_level'] = simulated_errors.quantile(upper, axis = 0)

data4.head()

# %%
# Calculate lower end of our forecast error confidence interval

data4['lower_level'] = simulated_errors.quantile(lower, axis = 0)

data4.tail()

# we are 95% confident that our actual error is 639 below and 659 above our forecast

# %%
# demand - forecast = error
# error + forecast = demand

data4['simulation_upper'] = data4['tes_forecast'] + data4['upper_level']
# already a negative, so add
data4['simulation_lower'] = data4['tes_forecast'] + data4['upper_level']

data4.tail()

# %% [markdown]
# <font color = 'red'> <font size = 4>
# **Task 8**
#     
# </font> </font>
# 
# Recreate your plot from Task 4. Add a 95% confidence interval as a '-.' line.

# %%
plt.figure(figsize=(15, 8))
plt.plot(data4['non_cumulative'], marker='o', color='deeppink', label='Actual Quarterly Operating Cash Flow')
plt.plot(data4['tes_forecast'], marker='o', color='blue', label = 'TES Forecast')
plt.plot(data4['simulation_upper'], color='#B9D9EB', linestyle = '-.')
plt.plot(data4['simulation_lower'], color= '#B9D9EB', linestyle = '-.')
plt.legend()

# %% [markdown]
# <font color = 'blue'> <font size = 4>
# **Question 5**
#     
# </font> </font>
# 
# Explain your results. Use home Depot's 10-Ks to provide context.

# %% [markdown]
# Home Depot's actual quarterly operating cash flow in general seems have higher forecast probability, given the 95% confidence interval, than it's actual values. This indicates that Home Depot's 10-k reports that Home depot's products weren't meeting the demands and preferneces of the customers, except the quarterly operating cash flow forecast in 2021 quarter 2 being smaller than the actual values. Given the fact that this plot includes the 95% confidence interval while minimizing as much as forecast errors as possible, we predict that Home Depot's 10-k would report actual operating cash flows will be lower in the future. We can assume that this trend ties in with Home Depot being classified as less performing compared to similar industry boundaries and competition such as Ace Hardware.


