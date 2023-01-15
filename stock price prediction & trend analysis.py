# %%
!pip install pandas-datareader 
import pandas as pd
import pandas_datareader
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.float_format = '{:,.2f}'.format


start = datetime.datetime(2018,1,1)
end = datetime.datetime(2022,1,1)

# %%
Tesla = web.DataReader('TSLA','yahoo',start,end)
Tesla.head()

# %%
BMW = web.DataReader('BMWYY','yahoo',start,end)
BMW.head()

# %%
Tesla['Close'].plot(label='Tesla Closing Price', fig=(50, 5))
Tesla['Open'].plot(label='Tesla Open Price', fig=(50, 5))
BMW['Close'].plot(label='BMW Closing Price', fig=(50, 5))
BMW['Open'].plot(label='BMW Open Price', fig=(50, 5))
plt.legend()
plt.title('Teslas Stocks')
plt.ylabel('Stock Prices')
plt.show


# Tesla and BMW's opening price are pretty similar for the past 4 years
# Looking closely, from mid 2020, Tesla has been dominating over BMW with higher opening price
# We would have to look at volume (number of stocks traded) of the 2 stocks to compare in depth

# %%
Tesla['Volume'].plot(label = 'Tesla Volume', figsize=(16, 5))
BMW['Volume'].plot(label = 'BMW Volume', figsize=(16, 5))
plt.title('Comparison output of Tesla and BMWs volume performance')
plt.ylabel('Stock Prices')
plt.show

# It seems as if I should be better off investing Tesla because it had a huge spike reaching a high volume trade somewhere in late 2018, early 2020, and early 2021

# %%
# If I were to invest on Tesla and am risk averse, I want to know its highest traded volume and to make sure that I can also jump on the investing trend
highest = Tesla['Volume'].max()
Tesla.loc[Tesla['Volume']==highest]
# It would be optimal to invest around the early 2020

# %%
# I want to seek Tesla's top 3 highest stock price to see when I should sell my tesla share and get a good ROI 
Tesla3high = Tesla.nlargest(3, ['High'])
Tesla3high

# %%
# I want to seek Tesla's top 3 lowest stock price to see when I can purchase some Tesla shares and hope to make a good ROI in the future
Tesla3low = Tesla.nlargest(3, ['Low'])
Tesla3low


# %%
# I also want to know the cumulative returns of each stocks to compare and chose the one that gives a bigger cumulative return
BMW['returns'] = (BMW['Close']/BMW['Close'].shift(1))-1
Tesla['returns'] = (Tesla['Close']/Tesla['Close'].shift(1))-1

BMW['cumulative return'] = (1 + BMW['returns']).cumprod()
Tesla['cumulative return'] = (1 + Tesla['returns']).cumprod()

# %%
BMW['cumulative return'].plot(label='BMW')
Tesla['cumulative return'].plot(label='Tesla')
plt.legend()

# Tesla has a bigger cumulative return whereas BMW had a small cumulative return. Thus, I should invest in Tesla.

# %% [markdown]
# ### writeup
# 
# 
# The automobile industry is in high demand during the recent years, including innovative and environment friendly brands like Tesla and hugh luxury brands like BMW. In order to make a wise investing decision, an investor should compare two companies' stock performance: open, close, high, low, volume, and cumulative returns.
# 
# So, let's make a simple line plot that compares Tesla and BMW's open and close price. By glossing over the graph, Tesla and BMW's opening price are pretty similar for the past 4 years (2018-2022). Looking at it more closely, from mid 2020, Tesla has had higher opening price compared to BMW.
# 
# This isn't enough to make a investing decision.
# 
# So, le'ts compare volume (number of stocks traded) of the 2 stocks to compare in depth. We can see that I am better off investing in Tesla because of the huge spike somewhere in late 2018, early 2020, and early 2021. 
# 
# Let's add more meat into the analysis. If I am a risk averse investor and I want to confirm that I should invest in Tesla, I should check its highest traded volume. I would also appreciate looking at Tesla's top 3 highest stock price to see when I should sell my tesla share and get a good ROI. I also want to seek the top 3 lowest stock price to see when I can purchase some shares in a cheaper price.
# 
# I lastly want a confirmation that investing on a Tesla stock would give me a higher return. I used our pre-existing variables to calculate return and cumulative return. Then, compare the two companies' cumulative return by plotting another line chart to confirm that investing on a Tesla is good because it has a bigger cumulative return than BMW.


