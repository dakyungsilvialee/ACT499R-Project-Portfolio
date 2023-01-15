# %% [markdown]
# # Regression Homework
# 
# For your homework this week you will study real estate prices in New York City. Specifically, our goal is to understand what factors determine the price of residential real estate in NYC over the last 4 years- 2018-2021. 
# 
# The data is collected from NYC's finance departments website (https://www1.nyc.gov/site/finance/taxes/property-annualized-sales-update.page). I pulled data from three boroughs (Manhattan, Brooklyn and Queens) over four years 2018-2021.
# 
# The variables are:
# 
# |Variable|Definition|
# |:---------|:-----------|
# |Borough|Number representing the borough in which the sale took place <br>
# ||1 = Manhattan <br>
# ||3 = Brooklyn <br>
# ||4 = Queens |
# |Neighborhood| Name of neighborhood in which the sale took place|
# |Building Class Category| Broad category of building class (eg. one family, multi family)|
# |BLOCK| A tax block is a subdivision of the borough|
# |Lot| A tax lot is a subdivision of a tax block. Distinguishes condos in the same building|
# |ADDRESS| Street address of the property|
# |APARTMENTNUMBER| Apartment number of the property if applicable|
# |ZIPCODE| Property's postal code|
# |RESIDENTIALUNITS| Number of residential units at the listed property|
# |COMMERCIALUNITS| The number of commercial units at the listed property|
# |TOTALUNITS| The total number of units at the listed property|
# |LANDSQUAREFEET| The land area of the property list in square feet|
# |GROSSSQUAREFEET| The total area of all the floors of a building as measured from the exterior surfaces of the outside walls of the building, including the land area and space within any building or structure on the property. |
# |YEARBUILT| Year the structure on the property was built|
# |TAXCLASSATTIMEOFSALE| - Class 1: Includes most residential property of up to three units, vacant land that is zoned for residential use, and most condominiums that are not more than three stories. <br>
# ||- Class 2: Includes all other property that is primarily residential, such as cooperatives and condominiums. <br>
# ||- Class 3: Includes property with equipment owned by a gas, telephone or electric company. <br>
# ||- Class 4: Includes all other properties not included in class 1,2, and 3, such as offices, factories, warehouses, garage buildings, etc.  |
# |BUILDINGCLASSATTIMEOFSALE|The Building Classification is used to describe a property’s constructive use.<br>
# ||The Letter describes a general class of properties (for example “A” signifies one-family homes, “O” signifies office buildings. “R” signifies condominiums).<br>
# ||The Number adds more specific information about the property’s use or construction style (using our previous examples “A0” is a Cape Cod style one family home, “O4” is a tower type office building and “R5” is a commercial condominium unit). <br>
# ||https://www1.nyc.gov/assets/finance/jump/hlpbldgcode.html|
# |SALEPRICE| Price paid for the property|
# |SALEDATE| Date the property sold|

# %% [markdown]
# <font color='blue' size = '5'> Task 1 </font>
# 
# Review my cleaning code below. Make sure you understand what I have done. Fill in the #'s throughout to notate what I did.
# 
# If you would like extra credit- rewrite the code as a loop. Specifically you should write one loop that clean all of the excel files before they are combined into one dataframe.

# %%
# Import database tools
import pandas as pd 
import numpy as np

# Import graphing tools
import seaborn as sns
import matplotlib.pyplot as plt

# Import regression library
import statsmodels.formula.api as smf

pd.options.display.float_format = '{:,.2f}'.format

# %%
# The data in our xlsx file starts at row 5, which is row "header" 4 in pandas.
# Thus, read the manhattan2018 and manhattan2019 xlsx dataset into pandas from header 4 

manhattan2018 = pd.read_excel('2018_manhattan.xlsx', header =4)

manhattan2019 = pd.read_excel('2019_manhattan.xlsx', header =4)

# %%
# The data in our xlsx file starts at row 7, which is row "header" 6 in pandas.
# Thus, read the manhattan2020 and manhattan2021 xlsx dataset into pandas from header 6 

manhattan2020 = pd.read_excel('2020_manhattan.xlsx', header =6)

manhattan2021 = pd.read_excel('2021_manhattan.xlsx', header =6)

# %%
# Return all columns from manhattan2018
manhattan2018.columns

# %%
# Replace ‘\n’ with ‘‘ space in the column names for manhattan2018, manhattan2019, manhattan2020, manhattan2021
manhattan2018.columns = manhattan2018.columns.str.replace(pat = '\n', repl = '')

manhattan2019.columns = manhattan2019.columns.str.replace(pat = '\n', repl = '')

manhattan2020.columns = manhattan2020.columns.str.replace(pat = '\n', repl = '')

manhattan2021.columns = manhattan2021.columns.str.replace(pat = '\n', repl = '')

# %%
# Replace ‘ ’ with ‘‘ space in the column names
manhattan2018.columns = manhattan2018.columns.str.replace(pat = ' ', repl = '')

manhattan2019.columns = manhattan2019.columns.str.replace(pat = ' ', repl = '')

manhattan2020.columns = manhattan2020.columns.str.replace(pat = ' ', repl = '')

manhattan2021.columns = manhattan2021.columns.str.replace(pat = ' ', repl = '')

# %%
# Print to see if the column names from manhattan2018 matches column names from manhattan2020, manhattan2019, manhattan2021

print(manhattan2018.columns == manhattan2020.columns)

print(manhattan2018.columns == manhattan2019.columns)

print(manhattan2018.columns == manhattan2021.columns)

# %%
# Check manhattan2018 column names
manhattan2018.columns

# %%
# Check manhattan2020 column names
manhattan2020.columns

# %%
# Pick certain column names and assign them as manhattan2018, manhattan2019, manhattan2020, manhattan2021

manhattan2018 = manhattan2018[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

manhattan2019 = manhattan2019[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

manhattan2020 = manhattan2020[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

manhattan2021 = manhattan2021[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

# %%
# Merge manhattan2018, manhattan2019, manhattan2020, manhattan2021 dataframes into one dataframe called manhattan

manhattan = pd.concat([manhattan2018, manhattan2019, manhattan2020, manhattan2021])

# %%
# The data in our xlsx file starts at row 5, which is row "header" 4 in pandas.
# Thus, read brooklyn2018 and brooklyn2019 xlsx dataset into pandas from header 4. 

brooklyn2018 = pd.read_excel('2018_brooklyn.xlsx', header =4)

brooklyn2019 = pd.read_excel('2019_brooklyn.xlsx', header =4)

# The data in our xlsx file starts at row 7, which is row "header" 6 in pandas.
# Thus, read brooklyn2020 and brooklyn2021 xlsx dataset into pandas from header 6. 

brooklyn2020 = pd.read_excel('2020_brooklyn.xlsx', header =6)

brooklyn2021 = pd.read_excel('2021_brooklyn.xlsx', header =6)

# %%
# Check brooklyn2018 column names
brooklyn2018.columns

# %%
# Check brooklyn2020 column names
brooklyn2020.columns

# %%
# Replace ‘\n’ with ‘‘ space in the column names for brooklyn2018, brooklyn2019, brooklyn2020, broooklyn2021

brooklyn2018.columns = brooklyn2018.columns.str.replace(pat = '\n', repl = '')

brooklyn2019.columns = brooklyn2019.columns.str.replace(pat = '\n', repl = '')

brooklyn2020.columns = brooklyn2020.columns.str.replace(pat = '\n', repl = '')

brooklyn2021.columns = brooklyn2021.columns.str.replace(pat = '\n', repl = '')

# Replace ‘ ’ with ‘‘ space in the column names for brooklyn2018, brooklyn2019, brooklyn2020, broooklyn2021
brooklyn2018.columns = brooklyn2018.columns.str.replace(pat = ' ', repl = '')

brooklyn2019.columns = brooklyn2019.columns.str.replace(pat = ' ', repl = '')

brooklyn2020.columns = brooklyn2020.columns.str.replace(pat = ' ', repl = '')

brooklyn2021.columns = brooklyn2021.columns.str.replace(pat = ' ', repl = '')

# %%
# Print to see if the column names from brooklyn2018 matches column names from brooklyn2020, brooklyn2019, brooklyn2021
print(brooklyn2018.columns == brooklyn2020.columns)

print(brooklyn2018.columns == brooklyn2019.columns)

print(brooklyn2018.columns == brooklyn2021.columns)

# %%
# Pick certain column names and assign them as brooklyn2018, brooklyn2019, brooklyn2020, brooklyn2021
brooklyn2018 = brooklyn2018[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

brooklyn2019 = brooklyn2019[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

brooklyn2020 = brooklyn2020[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

brooklyn2021 = brooklyn2021[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]


# Merge brooklyn2018, brooklyn2019, brooklyn2020, brooklyn2021 dataframes into one dataframe called brooklyn
brooklyn = pd.concat([brooklyn2018, brooklyn2019, brooklyn2020, brooklyn2021])

# %%
# The data in our xlsx file starts at row 5, which is row "header" 4 in pandas.
# Thus, read queens2018 and queens2019 xlsx dataset into pandas from header 4. 

queens2018 = pd.read_excel('2018_queens.xlsx', header =4)

queens2019 = pd.read_excel('2019_queens.xlsx', header =4)

# The data in our xlsx file starts at row 7, which is row "header" 6 in pandas.
# Thus, read queens2018 and queens2019 xlsx dataset into pandas from header 6. 

queens2020 = pd.read_excel('2020_queens.xlsx', header =6)

queens2021 = pd.read_excel('2021_queens.xlsx', header =6)


# Replace ‘\n’ with ‘‘ space in the column names for queens2018, queens2019, queens2020, queens2021

queens2018.columns = queens2018.columns.str.replace(pat = '\n', repl = '')

queens2019.columns = queens2019.columns.str.replace(pat = '\n', repl = '')

queens2020.columns = queens2020.columns.str.replace(pat = '\n', repl = '')

queens2021.columns = queens2021.columns.str.replace(pat = '\n', repl = '')

# Replace ‘ ’ with ‘‘ space in the column names for queens2018, queens2019, queens2020, queens2021
queens2018.columns = queens2018.columns.str.replace(pat = ' ', repl = '')

queens2019.columns = queens2019.columns.str.replace(pat = ' ', repl = '')

queens2020.columns = queens2020.columns.str.replace(pat = ' ', repl = '')

queens2021.columns = queens2021.columns.str.replace(pat = ' ', repl = '')


# Pick certain column names and assign them as queens2018, queens2019, queens2020, queens2021
queens2018 = queens2018[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

queens2019 = queens2019[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

queens2020 = queens2020[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

queens2021 = queens2021[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT',
                               'ADDRESS', 'APARTMENTNUMBER',
       'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS',
       'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT',
       'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', 'SALEPRICE',
       'SALEDATE']]

# Merge queens2018, queens2019, queens2020, queens2021 dataframes into one dataframe called queens
queens = pd.concat([queens2018, queens2019, queens2020, queens2021])

# %%
# EXTRA CREDIT PT
# Loop to clean data (assuming that we haven't run the previous individual cells that cleaned data) before merging


# List of num files to clean
files = ['2018_manhattan.xlsx', '2019_manhattan.xlsx', '2020_manhattan.xlsx', '2021_manhattan.xlsx', \
         '2018_brooklyn.xlsx', '2019_brooklyn.xlsx', '2020_brooklyn.xlsx', '2021_brooklyn.xlsx' \
         '2018_queens.xlsx', '2019_queens.xlsx', '2020_queens.xlsx', '2021_queens.xlsx']


# Total Compilation Variable (create an empty list to append cleaned dataset)
nyc_subset = {}

for file in files:
  # DATA LOADING (Manhattan, Brooklyn, and Queens 2018 - 2019)
  if (file[0:4] == '2018' or file[0:7] == '2019'):
    year = file[0:7]

    # Load nyc from the excel sheet that starts with '2018' or '2019'
    nyc = pd.read_excel(file, header = 4)
    
    # Replace the column names '\n' and ' ' with '' in manbrookqueens_df
    nyc.columns = df.columns.str.replace(pat = '\n', repl = '')
    nyc.columns = df.columns.str.replace(pat = ' ', repl = '')
    
    # Pick certain columns to include in nyc_final
    nyc_final = nyc[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT', \
                               'ADDRESS', 'APARTMENTNUMBER', 'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS', \
                            'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT', 'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', \ 
                            'SALEPRICE', 'SALEDATE']]

  # DATA LOADING (Manhattan, Brooklyn, and Queens 2020 - 2021)                
  else:
    # Load nyc from the excel sheet that doesn't starts with '2018' or '2019' 
    nyc = pd.read_excel(file, header = 6)
    
     # Replace the column names '\n' and ' ' with '' in manbrookqueens_df
    nyc.columns = df.columns.str.replace(pat = '\n', repl = '')
    nyc.columns = df.columns.str.replace(pat = ' ', repl = '')
    
    # Pick certain columns to include in nyc_final
    nyc_final = nyc[['BOROUGH', 'NEIGHBORHOOD', 'BUILDINGCLASSCATEGORY', 'BLOCK', 'LOT', 'EASE-MENT', \
                               'ADDRESS', 'APARTMENTNUMBER', 'ZIPCODE', 'RESIDENTIALUNITS', 'COMMERCIALUNITS', 'TOTALUNITS', \
                            'LANDSQUAREFEET', 'GROSSSQUAREFEET', 'YEARBUILT', 'TAXCLASSATTIMEOFSALE', 'BUILDINGCLASSATTIMEOFSALE', \ 
                            'SALEPRICE', 'SALEDATE']] 


# %%
#BACK TO NO LOOP CLEANING
# Merge manhattan, brooklyn, queens dataframes into one dataframe called nyc
nyc = pd.concat([manhattan, brooklyn, queens])

# Print the information inside the nyc dataframe
nyc.info()

# %%
# Since we merged every dataframe horizontally previously, drop column 'EASE-MENT' all together in one dataframe called 'nyc'.
nyc = nyc.drop(['EASE-MENT'], axis = 1)

# %%
# Convert datatypes 'BOROUGH', 'BLOCK', 'LOT', 'ZIPCODE', 'TAXCLASSATTIMEOFSALE', 'YEARBUILT' as string 
nyc['BOROUGH'] = nyc['BOROUGH'].astype(str)

nyc['BLOCK'] = nyc['BLOCK'].astype(str)

nyc['LOT'] = nyc['LOT'].astype(str)

nyc['ZIPCODE'] = nyc['ZIPCODE'].astype(str)

nyc['TAXCLASSATTIMEOFSALE'] = nyc['TAXCLASSATTIMEOFSALE'].astype(str)

nyc['YEARBUILT'] = nyc['YEARBUILT'].astype(str)

# %%
# Return a series containing counts of unique values from column 'YEARBUILT' in nyc dataframe 
nyc['YEARBUILT'].value_counts()

# %%
# Return values that corresponds to index 0 to 4 inside 'YEARBUILT' column inside nyc dataframe
nyc['YEARBUILT'] = nyc['YEARBUILT'].str[0:4]

nyc['YEARBUILT'].head()

# %%
# Format year as a four digit number and override error by returning NaT (missing value) for any values that do not conform
nyc['YEARBUILT'] = pd.to_datetime(nyc['YEARBUILT'], format = '%Y', errors='coerce')

# %%
# Drop null values from column 'SALEPRICE' and 'GROSSSQUAREFEET' inside the nyc dataframe 
nyc.dropna(subset = ['SALEPRICE'], inplace = True)

nyc.dropna(subset = ['GROSSSQUAREFEET'], inplace = True)

# %%
# Return a tuple that contains the nyc dataframe's dimensionality
nyc.shape

# %%
# Return only the year of the values from column 'SALEDATE' and rename column name into 'saleyear'
nyc['saleyear'] = nyc['SALEDATE'].dt.year

# Return a series containing counts of unique values from column 'saleyear' in nyc dataframe 
nyc['saleyear'].value_counts()

# %%
# Return a series containing counts of unique values from column 'TAXCLASSATTIMEOFSALE' in nyc dataframe 
nyc['TAXCLASSATTIMEOFSALE'].value_counts()

# %%
# only keep residential sales
nyc_subset = nyc[(nyc['TAXCLASSATTIMEOFSALE'] =='1.0') | (nyc['TAXCLASSATTIMEOFSALE'] =='2.0')]

# %%
# Return a series containing counts of unique values from column 'TAXCLASSATTIMEOFSALE' in nyc dataframe 
nyc_subset['BUILDINGCLASSCATEGORY'].value_counts()

# %%
# remove vacant land sales
nyc_subset = nyc_subset[nyc_subset['BUILDINGCLASSCATEGORY'] != '05 TAX CLASS 1 VACANT LAND']

# %% [markdown]
# <font color='blue' size = '5'> Task 2 </font>
# 
# ## Understand our Y-Variable
# 
# 1. Your borough data is currently coded with numbers. Replace the numbers with the name of each borough. 

# %%
nyc_subset = nyc_subset.replace({'BOROUGH':{'1.0':'Manhattan', '3.0':'Brooklyn', '4.0':'Queens'}})
nyc_subset

# %% [markdown]
# 2. Describe the distribution of sales price data in each Borough (with data, no writing necessary).

# %%
nyc_subset.groupby('BOROUGH')['SALEPRICE'].describe()

# %% [markdown]
# 3. Remove any data in which the sales price is zero. NYC notes, "A \\$0 sale indicates that there was a transfer of ownership without a cash consideration. There can be a number of reasons for a \\$0 sale including transfers of ownership from parents to children." We are not interested in these transfers. Remove them from our dataframe.
# 
# 
# 4. Redescribe the sales price data in each Borough (with data, no writing necessary).

# %%
#3

nyc_subset = nyc_subset[nyc_subset.SALEPRICE != 0]
nyc_subset

# %%
#4
nyc_subset.groupby('BOROUGH')['SALEPRICE'].describe()

# %% [markdown]
# 5. Create a boxplot to visualize sales price data in each Borough.

# %%
# figsize is width, height
# rows, columns for set up of subplots
fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize = (15,8))

# plot each variable on a boxplot

ax1.boxplot(nyc_subset[nyc_subset['BOROUGH'] == 'Manhattan']['SALEPRICE'], whis = 1.5)
ax2.boxplot(nyc_subset[nyc_subset['BOROUGH'] == 'Brooklyn']['SALEPRICE'], whis = 1.5)
ax3.boxplot(nyc_subset[nyc_subset['BOROUGH'] == 'Queens']['SALEPRICE'], whis = 1.5)

# label each axes
ax1.set_ylabel('Manhattan')
ax2.set_ylabel('Brooklyn')
ax3.set_ylabel('Queens')

# to make y labels fit a bit better
plt.tight_layout()

# %% [markdown]
# 6. Create another boxplot to visualize the bottom 95% of the sales price data in each Borough (ignore the top 5%). ``df['column'].quantile()`` will be helpful. Do not remove the top 5% just create a graph without those values.

# %%
# figsize is width, height
# rows, columns for set up of subplots
fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize = (15,8))


# plot each variable on a boxplot

ax1.boxplot(nyc_subset[(nyc_subset['BOROUGH'] == 'Manhattan') & (nyc_subset['SALEPRICE'] < nyc_subset['SALEPRICE'].quantile(0.95))]['SALEPRICE'], whis = 1.5)
ax2.boxplot(nyc_subset[(nyc_subset['BOROUGH'] == 'Brooklyn') & (nyc_subset['SALEPRICE'] < nyc_subset['SALEPRICE'].quantile(0.95))]['SALEPRICE'], whis = 1.5)
ax3.boxplot(nyc_subset[(nyc_subset['BOROUGH'] == 'Queens') & (nyc_subset['SALEPRICE'] < nyc_subset['SALEPRICE'].quantile(0.95))]['SALEPRICE'], whis = 1.5)



# label each axes
ax1.set_ylabel('Manhattan')
ax2.set_ylabel('Brooklyn')
ax3.set_ylabel('Queens')

# to make y labels fit a bit better
plt.tight_layout()

# %% [markdown]
# 7. Describe the distribution of sales prices data in each of the last four years. (Just with code, no writing necessary).

# %%
nyc_subset.groupby('saleyear')['SALEPRICE'].describe()

# %% [markdown]
# <font color='red' size = '5'> Question 1 </font>
# 
# **Describe in words what you learned throughout Task 2.**
# 
# In order to frame business questions, we need to describe data in a concise manner. Thus, we learned that we should use the groupby function in order to  collapse a field into its distinct values. We also learned how to incorporate the describe method in order to see the description (distribution) of our numerically grouped dataframe with informations for each column such as count, mean, std, min, max, and percentiles. By analyzing the box plots, we hope to understand our y variable that help us determine the sales price of the borough from respective years: 2018, 2019, 2020, and 2021   
# - The distribution of sales price data from grouping by borough and sale year shows us that...
#     - Manhattan has the highest avg saleprice of 3,527,773, the highest median (50%) saleprice of 1,440,000, and the highest upperr quartile.
#     - 2020 has the highest avg saleprice of 1,715,414 and one of the highest median (50%) saleprice of 840,000. 
#     - This shows that there is a high demand for the housing market in Manhattan for the past 4 years, especially in 2020, where we can assume the pandemic and quarantining lifestyle caused a higher demand
# 
# ---

# %% [markdown]
# <font color='blue' size = '5'> Task 3 </font>
# 
# ## Understand our X-Variable
# 
# 1. Describe the distribution of gross square feet in each Borough (with data, no writing necessary). You may find some funky values. Troubleshoot and fix.

# %%
nyc_subset.groupby('BOROUGH')['GROSSSQUAREFEET'].describe()

# %% [markdown]
# 2. Use ``sns.lmplot()`` to create a scatterplot with a regression line that plots sales price as a function of gross square feet.

# %%
sns.lmplot(x = 'GROSSSQUAREFEET', y = 'SALEPRICE', data= nyc_subset)

# %% [markdown]
# 3. Describe what you notice in the above graph and you propose needs to be done to clean our variables.

# %% [markdown]
# There is an outlier: a house that has been sold with a small amount for a big gross square feet. This phenomenon can pull our regression line down due to bias. We should remove data that is 0 or over/below a certain threshold of the correlation between sale price and gross square feet.

# %%
nyc_subset = nyc_subset[nyc_subset.GROSSSQUAREFEET != 0]

# %% [markdown]
# 4. Assume that any sale with a price per square foot less than the average price per square foot in Oxford, Georgia (where Emory's Oxford campus is location) is a related party transfer and remove this data. The median price per square foot in Oxford, Georgia is \\$140.
# 
# 5. Rerun your lmplot on the filtered data.

# %%
#4

nyc_subset['SALEPRICE_PER_SQUAREFEET'] = nyc_subset['SALEPRICE']/(nyc_subset['GROSSSQUAREFEET'])

nyc_subset = nyc_subset[nyc_subset.SALEPRICE_PER_SQUAREFEET > 140]
nyc_subset

# %%
#5
sns.lmplot(x = 'GROSSSQUAREFEET', y = 'SALEPRICE', data= nyc_subset)

# %% [markdown]
# 6. Create boxplots to visualize the distribution of gross square feet of the properties sold in each Borough.
# 
# 7. Create another boxplot to visualize the bottom 95% of the gross square footage data in each Borough (ignore the top 5%). ``df['column'].quantile()`` will be helpful. Do not remove the top 5% just create a graph without those values.

# %%
# 7
# figsize is width, height
# rows, columns for set up of subplots
fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize = (15,8))


# plot each variable on a boxplot

ax1.boxplot(nyc_subset[(nyc_subset['BOROUGH'] == 'Manhattan') & (nyc_subset['GROSSSQUAREFEET'] < nyc_subset['GROSSSQUAREFEET'].quantile(0.95))]['GROSSSQUAREFEET'], whis = 1.5)
ax2.boxplot(nyc_subset[(nyc_subset['BOROUGH'] == 'Brooklyn') & (nyc_subset['GROSSSQUAREFEET'] < nyc_subset['GROSSSQUAREFEET'].quantile(0.95))]['GROSSSQUAREFEET'], whis = 1.5)
ax3.boxplot(nyc_subset[(nyc_subset['BOROUGH'] == 'Queens') & (nyc_subset['GROSSSQUAREFEET'] < nyc_subset['GROSSSQUAREFEET'].quantile(0.95))]['GROSSSQUAREFEET'], whis = 1.5)



# label each axes
ax1.set_ylabel('Manhattan')
ax2.set_ylabel('Brooklyn')
ax3.set_ylabel('Queens')

# to make y labels fit a bit better
plt.tight_layout()

# %% [markdown]
# <font color='red' size = '5'> Question 2 </font>
# 
# **Describe in words what you learned over throughout Task 3 and any thoughts you have on further cleaning this variable.**\
# 
# By analyzing the box plots and regression plots, we hope to understand our x variable that help us determine the sales price of the borough from respective years: 2018, 2019, 2020, and 2021
# 
# - The distribution and the regression plot of gross square feet data from grouping by borough shows us that...
#     - Brooklyn has the highest avg gross square feet of 4,741 and the highest median (50%) gross square feet of 1,728.
#     - Brooklyn has a higher (both lower and upper quartile) than Manhattan or Queens with a longer spread of variation (box length).
#     - There seems to be a positive correlation between gross square feet and the sale price from the regression . 
#     - There seems to be an error in the data that results the distribution of Manhattan because the minimum, 25% quartile, and 50% quartile of gross square feet resulting in 0. 
#     - We can also see errors in the regression plot such as outliers that pulls the regression line downwards.
#     - This shows that there is a need to remove erroneouos data such as 0 values or data over or below a certain threshold of the correlation between sale price and gross square feet.
# 
# 
# ---

# %% [markdown]
# <font color='blue' size = '5'> Task 4 </font>
# 
# Run a regression that predicts sales price based on gross square footage and borough.
# 
# Note: .summary2() will display the results in float format rather than scientific notation. Its probably best to look at both.

# %%
simple = smf.ols('SALEPRICE ~ GROSSSQUAREFEET + BOROUGH', data = nyc_subset).fit()
simple.summary()

# %% [markdown]
# <font color='red' size = '5'> Question 3 </font>
# 
# **a. How do you interpret the R squared in this model?**
# 
# The regression model shows us that 75% accounts for the variation of our sales price is described by our gross square feet per borough. \
# Thus, it is reasonable to associate most of my sales price with "how big is the home in a specific borough". The other (1-75) 25% shows us that it is reasonable to predict sales price from other independent variables (e.g neighborhood, total units, etc).   
# 
# 
# **b. How do you interpret each of the coefficients (including the intercept) in this model?** 
# - draw out y=mx+b equation and think about the changs in x and y \
# - there seems to be a positive correlation between sales price and gross square feet per borough
# 
# 
# **c. Your regression likely produced the following error "The condition number is large, 4.63e+04. This might indicate that there are strong multicollinearity or other numerical problems." What does this mean? What do you think may cause the problem?** 
# - Multicollinearity
#     - In this case, we threw in two x variables (gross square feet and borough) that captures the same thing by being highly correlated
#     - standard errors of at least one of the correlated x variables will increases the probability that our coefficient estimate is less accurate and underestimates the statistical significance
# - Missing a theoretical link
#     - we need to understand our x variables before putting them in regression in order to say that it's reaonsable to think that gross square feet and borough is a proxy for sales price.

# %% [markdown]
# <font color='blue' size = '5'> Task 5 </font>
# 
# Run the same regression that predicts sales price based on gross square footage and borough except multiply together square footage and borough. 

# %%
simple = smf.ols('SALEPRICE ~ GROSSSQUAREFEET * BOROUGH', data = nyc_subset).fit()
simple.summary()

# %% [markdown]
# <font color='red' size = '5'> Question 4 </font>
# 
# Explain how this regression's specification differs from your first regression and why it may be important to specify the regression in this manner. 

# %% [markdown]
# In order to avoid issues such as multicollinearity, it would be beneficial to have one independent variable that captures the best fit line for our dependent variable rather than having multiple "same" independent variables that can lead to biased high correlation. 
# 
# Thus, when independent variables are the same, multiplying them and the coefficients together and compresses them into a single independent variable would give a more accurate result. 
# 
# In this case, our borough and gross square feet being a proxy to estimate sales price was very similar and lead to multicollinearity issues. If we compress these coefficients and variables together into a single independent variable, our r squared rate is 10% higher.

# %%



