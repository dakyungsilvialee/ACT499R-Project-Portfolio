# %% [markdown]
# # Homework 3
# 
# I have inserted blank code cells for you to work in but feel free to add or delete depending on your needs. **Do not read into the number of code cells as a sign of the number of cells you need to answer the questions.** Feel free to also add markdown cells if you want to make notes for yourself. These may be helpful in the future as you can review this workbook to see the code you learned.
# 
# Also note that I have inserted blank Markdown cells for you to insert your answers to my questions. These cells currently say "Type Markdown and LaTeX:  𝛼2". If you click on the cell, you can type in your response.

# %% [markdown]
# <font color='red' size = '5'> Exercise 1: Input your Data </font>
# 
# a. First, download hw3.csv from Canvas and save to the same folder that holds this Homework 3 notebook
# 
# b. Upload the data to this notebook as a DataFrame named ``df``. 
# 
# You should have the following variables:
# 
# |Variable Name| Description|
# |:-----|:------|
# |country| Country|
# |year| Year the data relates to|
# |pop| Population of that country in that year, displayed in millions, billions or thousands|
# |pop2| Population of that country in that year as a numeric value|
# |gdp_percapita| GDP per person in that country in that year|
# |billion_num| number of billionaires based on country of citizenship|
# |billion_age| average age of billionaires in that country, 0 if no billionaires|
# |billion_rate_perM| number of billionaires per 1 million citizens|
# |poor10| percentage share of total income that accrues to bottom 10% of population|
# |rich10| percentage share of total income that accrues to top 10% of population|
# |pov_320| \% of people below \$3.20/day|
# |pov_550| \% of people below \$5.50/day|

# %%
import pandas as pd

# %%
df = pd.read_csv('hw3.csv')

# %% [markdown]
# c. Is all of your data in the correct format? If not, update accordingly. Don't worry about formatting anything as a date, we're not quite there yet. But anything that we do want to perform mathematical calculations on should be a number and anything we do not want to perform calculations on should be a string.
# 
# d. Change the float formatting of this notebook to have thousands separators and 2 decimal places.

# %%
#c

df['year'] = df['year'].astype(str)
df['billion_num'] = df['billion_num'].astype(str)

df['billion_age'] = df['billion_age'].astype(str)
df['billion_rate_perM'] = df['billion_rate_perM'].astype(str)
df['gdp_percapita'] = df['gdp_percapita'].astype(str)
df['poor10'] = df['poor10'].astype(str)
df['rich10'] = df['rich10'].astype(str)
df['pov_320'] = df['pov_320'].astype(str)
df['pov_550'] = df['pov_550'].astype(str)
df['pop2'] = df['pop2'].astype(str)

# %%
#d

pd.options.display.float_format = '{:,.2f}'.format

# %%
df.describe()

# %%
df.info()

# %% [markdown]
# <font color='red' size = '5'> Exercise 2: Understand your Data </font>
# 
# a. Describe your data (using code, not words).
# 
# b. Use what you learn from the summary statistics and your data subsetting skills to answer the following questions. You may answer by simply having code that outputs the answer. No need to add markdown cells. Each question should be answered with **one** line of code.
#     
# 1. People in which country in which year are the poorest of the poor? (accrue the smallest amount of their country's total income)
#     
# 2. Has the plight of these countries' poorest citizens improved over the time period captured by our data sample?
# 3. What percentage of total income does the richest 10% of the population accrue in the country with the most billionaires? Answer this question twice- once for the country with the absolute most billionaires and once for the country with the most billionaires per million people

# %%
#1
#we filter out the minimum amount of gdp_percapita with its respective country.

df['country'][df['gdp_percapita'] == df['gdp_percapita'].min()]

# %%
#we filter out the minimum amount of gdp_percapita and it's country with its respective year
df['year'][df['gdp_percapita'] == df['gdp_percapita'].min()]

# %%
#2

df.groupby('country')['gdp_percapita'].sum()

# %%
#3

df['rich10'][df['billion_num'] == df['billion_num'].max()]

# %%
df['rich10'][df['billion_num'] == df['billion_rate_perM'].max()]

# %% [markdown]
# <font color='red' size = '5'> Exercise 3: Analyze your Data </font>
#     
# a. Calculate the total GDP in each country in each year. You do not need to display anything for this step.
# 
# b. Calculate the worldwide GDP in each year.
# 
# c. Calculate the worldwide population in each year.
# 
# d. What is the worldwide gdp per capita in each year? Answer with code output.
# 
# e. What is the total number of billionaires in each year of our sample? Answer with code output.
# 
# f. What is the average age of billionaires worldwide? Be sure that your calculation does not include countries without billionaires.
# 
# g. Challenge Question: What percentage of worldwide billionaires live in the US in each year? Note: because this question is so hard it is not worth very many points but I would still love for you to attempt to answer it. Think about what you need in what format to calculate the answer. And of course, I am looking for code, not hard coding.

# %%
#a

df.groupby('country')['gdp_percapita'].sum()

# %%
#b

df.groupby('year')['gdp_percapita'].sum()

# %%
#c

df['worldwide_pop'] = df.groupby('year')['gdp_percapita'].sum() * df['gdp_percapita']
df['worldwide_pop']

# %%
#d 
df.groupby('year')['gdp_percapita']

# %%
#e
df.groupby('year')['billion_num'].sum()

# %%
#f
df['billion_age'].sum()

# %% [markdown]
# <font color='red' size = '5'> Question 1 </font>
# 
# In the following code, classify each item in the code as a variable, function, method or attribute: 
# ```python
# print(df.columns)
# ```

# %% [markdown]
# df = (country, year, billion_age, billion_num, billion_rate_perM, gdp_percapita, poor10, rich10, pop, pov_320, pov_550, pop2) 

# %% [markdown]
# ## Prep for Next Week's Class
# 
# Read the first three pages of EY ARC_360 Performance Evaluations.


