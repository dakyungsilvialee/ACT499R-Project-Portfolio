# -*- coding: utf-8 -*-
"""Analyzing Australian Tax Return Data_Part I_ 2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/101tHtlhKJjeqUjfSXhYw_3GwyDsDXKFi

# Analyzing Australian Tax Return Data- Part 1

## Background Information

In this case study you will explore Australian corporations’ tax return data. Australia (unlike the United States) publicly discloses three line items from large corporations’ tax returns. The three line items disclosed are:

- **Total Income**- Total income is a measure of a company’s gross receipts or revenue. It does not include any deductions or expenses.


- **Taxable Income** - Taxable income is a measure of a company’s profitability based on Australian tax law. Taxable income is the basis from which a company’s income tax liability is calculated.
   - The difference between a company’s total income and it’s taxable income is the amount of tax deductions or expenses a company claims on its tax return.
   
<center> <font color = blue> <font size = 4> $Taxable Income$ <font color = black> $=$ <font color = red> $Total  Income$ <font color = black> $- Tax Deductions$ </center>

   - Taxable income is separate and distinct from a company’s financial accounting income. Although both financial accounting income and taxable income measure a firm’s profitability, they are calculated differently.
      - Financial accounting income is designed to measure a firm’s economic transactions and to be as informative as possible to investors and creditors.
      - Taxable income is defined by the government and is designed to raise money and to encourage or discourage certain behaviors. For example, in the United States, we are allowed to deduct interest incurred on a household mortgage because the government wants to encourage home ownership.


- **Tax Payable**- Tax payable is a company’s Australian income tax liability and measures the amount of income taxes that the company must pay to Australia’s federal government.
   - Tax payable is a function of a company’s taxable income. If the company does not claim any tax credits, tax payable will equal 30% of a company’s taxable income. 30% is the corporate income tax rate in Australia. 
   
<center> <font color = green> <font size = 4> $Tax Payable$ <font color = black> $=$ <font color = blue> $Taxable Income$ <font color = black> $*Tax Rate (30\%\ in Australia)$ </center>

   - Tax payable will be less than a company’s taxable income times the income tax rate if the company claims any tax credits.

<center> <font color = green> <font size = 4> $Tax Payable$ <font color = black> $=$ <font color = blue> $Taxable Income$ <font color = black> $*30\%-Tax Credits$ </center>
	
   - Tax credits are a way for the government to subsidize certain corporate activities. Tax credits allow the government to indirectly pay a corporation back for the amount of money a corporation spent on a certain activity. For instance, in the United States, some students qualify for tuition tax credits. By giving a student a tuition tax credit, the government allows a student to pay less taxes than the amount the student would normally owe based on the student’s taxable income. This way, the student can pay for the student’s tuition with the money the student saved by not paying taxes. These transactions are an indirect way for the government to pay for the student’s tuition. In corporations, the most common tax credit is for research and development (R&D). Many governments want to encourage R&D as innovation often leads to economic growth.

The following equation summarizes the relationship between the three variables:

<center> <font size = 4> <font color = red> $(Total Income$ </font> $-Tax Deductions)*30\%-Tax Credits=$ <font color = green> $Tax Payable$ </font> </center>

The Australian government started to publicly disclose large corporation’s tax return information in December 2015. Due to the long nature of the tax reporting cycle, information disclosed in December 2015 relates to tax returns for years ending December 1, 2013 – November 30th, 2014 (most Australian firms have a June 30th year end).

The Australian government’s tax transparency legislation has two stated objectives: 

> 1. Discourage large corporate entities from engaging in aggressive tax avoidance practices
> 2. Provide more information to inform public debate about tax policy
> *Australian Senate 2013* 
    
    
Australian legislators hoped that if large firms were forced to report their tax information, public shaming would cause low tax paying firms (firms that engage in a lot of tax planning) to pay more taxes. In this case study, you will explore that idea.

## Case Instructions

To break down the over arching question of this case into actionable steps, you will follow the FACT framework.

## F- Frame the Question: 

The overarching goal of this case is to provide evidence as to whether public disclosure of corporate tax return data affected firms’ tax planning choices. Remember that Australian legislators hoped that if large firms were forced to report their tax return information, the public would shame low tax paying firms (firms that engage in a lot of tax planning) and subsequently cause these firms to pay more taxes. We are specifically interested in measuring if this phenomenon occurred. 

Because you are studying income taxes, it is important to remember that taxes are a function of profitability. Rather than focusing on total taxes paid in isolation, you may want to focus on an effective tax rate:

<div align = "center"> <font size = 4> $Effective Tax Rate = \frac{Tax Payable}{Taxable Income}$ </font> </div>

If this number is lower than Australia’s 30% statutory rate, the firm is claiming tax credits.

Keep in mind that a firm that pays the 30% statutory rate may still engage in tax planning by lowering the firm’s taxable income. With this type of tax planning, a firm claims extra tax deductions. Some tax deductions are normal expenses, such as an employee's salary. Some tax deductions may push the boundaries of what lawmakers intended corporations to deduct. For instance, a firm may improperly deduct the cost of operating a corporate jet for an executive’s vacation.

As an example of tax planning that relies on claiming extra tax deductions, a recent article in *The New York Times* notes that,
>...without any explanation in his [President Donald Trump] returns, the general and administrative expenses at his Bedminster golf club in New Jersey increased fivefold from 2016 to 2017.
>
>*Buettner, Craig and McIntire 2020*

We have panel data- multiple firms over multiple years. The law was passed in June 2013. The first data was disclosed in December 2015 and related to tax years ending 12/1/2013 - 11/30/2014; most Australian corporations have a June 30th year end so most of the data related to the year ending June 30th, 2014. Companies could have updated their tax planning for this year in anticipation of a public backlash but the first two years, the year ending 6/30/2014 and 6/30/2015 ended before the first year of data was disclosed in December 2015. If companies changed their tax planning after an actual public backlash (if there was one) we would not see it in the data until year 3 ending 6/30/2016 (which was half way over when the first year of data was disclosed) or even year 4 ending 6/30/2017 (which occured completely after data had been disclosed).

**Keeping in mind the above points and your understanding of the data, <font color = 'blue'> write three concrete data questions </font> that are designed to help you understand (at least descriptively) if public tax return disclosure led firms to pay more taxes.**

A few notes:
- Your questions should be framed in terms of the data you have and be very specific. For instance, if you are interested in an average, specify whether you will measure the mean or median. Note that the same question augmented to ask about the mean instead of the median does **not** count as a second question.
- Your question should specify which year you are looking at: first year, last year, changes over specific years.
- You may want to study all firms, or you may want to study specific subgroups (i.e. public vs. private, really big vs. less big (define size criteria), etc.)
- Be sure that your questions can be answered with the data we have. If you have a question that cannot be answered with the data you have, describe what data you need and how you would use it to help answer your question.
- Your questions should help to answer the bigger question as to whether public tax return disclosure changed tax paying behavior.
- I am looking for thoughtful ideas and most importantly, **I should be able to understand exactly what you intend to measure.**

**Good and not as good examples based on a study of Lyft and Uber pricing strategies:**
- Example of an interesting question that does not clearly explain what will be measured
> We expect the surge multiplier to increase at certain times of day such as rush hour. Is this expectation true? What is the relationship between surge multiplier and time?

- Same question, more specifics with respect to what will be measured
> What is the highest surge multiplier (from both Lyft and Uber) observed in our dataset and what time of day does it occur? If I segment the data into 4 times of day (7am – 9am, 10am-4pm, 5pm- 7pm, 7pm-7am), what is the average (mean and median) surge multiplier during each time segment?

<div style="color:black;
           display:fill;
           border-radius:5px;
           background-color:#ABBAEA;>

            
<p style="padding: 10px;
              color:white;">

**Type your specific, measurable questions here**:


. If I separate public and private firms observed in our dataset and segment the years (2013-2014, 2014-2015, 2015-2016, 2016-2017, 2017-2018, 2018-2019, 2019-2020), **what is the mean and standard deviation of the effective tax rate for those periods?** Thus, what would you conclude from the clustering of firms (public vs private) such as if the policy is doing its job or if firms are following the same/different tendencies? 


. After determining the size of the firm- based if under or above the median of total income- **what is the average (median) difference between total income and taxable income in years 2013-2014 and 2014-2015** in order to see whether big/small companies take more/less advantage of tax credits and deductions.


. **What is the average change of the effective tax rate between years(2013-2014, 2014-2015)?** By separating public and private firms, how can we conclude that a company is ashamed/proud of disclosing their tax return data?


------

### A- Assemble the Data- Part 1

The Australian Tax Office (ATO) is the Australian version of the United States’ Internal Revenue Service (IRS). The ATO posts excel workbooks with large corporations' tax return information once a year on the following [website](https://data.gov.au/dataset/ds-dga-c2524c87-cea4-4636-acac-599a82048a26/details). 

Each workbook relates to a different year of data. You will analyze the first seven years of data which relate to tax years ending December 1st, 2013- November 30th, 2020. The data is a time series with seven years of observations for approximately 1,000 firms.


**1. Open the first excel workbook in excel. Read the information tab in the excel workbooks to better understand the data.**
   - In the first year of public tax return disclosure, public firms' data was disclosed in December, while private firms' data was disclosed in March. In all subsequent years, public and private firm data is disclosed at the same time (in December). Public and private firms are separated only in the first year of data: public firms on the tab labeled ‘December’ and private firms on the tab labeled ‘March’. In all subsequent years, the two sets of firms are intermingled in the data. 
   - You should also notice that in all years after the first year, there are additional tabs or rows disclosing prior year data. You will only focus on data that is filed on time so you can ignore those tabs (for instance the 2013-2014 data in the 2014-2015 workbook).

   
    
**2. Without doing any manipulation in excel, upload the data you need from each excel workbook into this Jupyter notebook and clean the data <font color = 'blue'> using a loop </font>. Be sure to document your work and to make it as replicable as possible.**
- I recommend uploading the first year of data outside of the loop for two reasons:
   - The first year of data is different because public and private data are listed on separate tabs. You do want to identify and distinguish public and private firms. Use the first year of data to do so. We will assume no public firms went private and vice versa during our time frame.
   - Uploading and cleaning this data separately will make writing a loop easier for all subsequent years
   - **Things to keep in mind when uploading and cleaning:**
      - When uploading the data, keep in mind that you are interested specifically in income tax data, not PRRT (Petroleum Resource Rent Tax). 
      - Do not keep any firms that are missing their Australian Business Number (ABN).
      - Make sure each year of data is distinguishable, i.e. create a column to indicate which year is which
      - All public firms with total income over \\$100M are subject to disclosure whereas private firms are only subject to disclosure if the firm's total income is over \\$200M. To make the two sets of firms fully comparable, filter each year of data to only include firms with \\$200M or more in total income. 


       
<font color= 'green'> *If you are really struggling with the loop. Upload each file separately and move on. You will lose some points for not having the loop but it is more important that you finish this notebook so that you can move on to part 2- the data analysis.*
"""

!pip install xlrd
!pip install psycopg2

import numpy as np
from google.colab import files
import io
import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format

#import midter dataset files
dataset = files.upload()

#first year public dataset
df_public = pd.read_excel('2013-14-corporate-report-of-entity-tax-information.xlsx', sheet_name = 'December')
df_public

#drop ABN null value

df_public = df_public.dropna(subset=['ABN'])
df_public

#filter each year of data to only include firms with $200M or more in total income

df_public = df_public[df_public['Total income $'] >= 200000000]
df_public.head(20)

#first year private dataset
df_private = pd.read_excel('2013-14-corporate-report-of-entity-tax-information.xlsx', sheet_name = 'March')
df_private

#filter each year of data to only include firms with $200M or more in total income
df_private = df_private[df_private['Total income $'] >= 200000000]
df_private.head(20)

# Do not keep any firms that are missing their Australian Business Number (ABN)
df_public.dropna(inplace = True)
df_public

frames = [df_public, df_private]

df_public_private = pd.concat(frames, keys = ['public', 'private']).reset_index().drop('level_1', axis=1).rename(columns={'level_0':'Public/Private'})

df_public_private.insert(5, "Income Year", "13-14", True)
df_public_private

"""### A- Continue to Assemble- Part 2

**Ultimately, you need to combine the seven datasets into one DataFrame. Before you start, think through what type of merge you want to do based on which observations you’d like to keep. Explain your reasoning.**

<div style="color:black;
           display:fill;
           border-radius:5px;
           background-color:#ABBAEA;>

            
<p style="padding: 10px;
              color:white;">

**Answer:**
We should merge these different dataframes by applying an inner join because all the dataframes have attributes that are in common such as "total income", "taxable "and "tax payable" as well as the names of the public and private companies correspond.  

----

**Transform the data. The steps below walk you through the data merging and cleaning process. There are different ways to get to the same end point. <font color = 'blue'> Follow the process below to demonstrate your skillset.**

**1.** Rename the columns in each dataset to distinguish which year each Total Income, Taxable Income and Taxes Payable come from.
- It is also important to make sure that the base of the column names are the same. For instance, if you make Total Income in year 1 `Total Income_14` make the second year’s Total Income column `Total Income_15`.
- This is most efficient if you write a loop but a loop is not required here. (Nor will you receive bonus points but you may save yourself some time and you will be better for it :))
"""

# list of num files to clean
files = ['2014-15-corporate-report-of-entity-tax-information.xlsx', \
       '2015-16-corporate-report-of-entity-tax-information.xlsx', \
       '2016-17-corporate-report-of-entity-tax-information.xlsx', \
       '2017-18-corporate-report-of-entity-tax-information.xlsx', \
       '2018-19-corporate-report-of-entity-tax-information.xlsx', \
       '2019-20-corporate-report-of-entity-tax-information.xlsx']


# Total Compilation Variable (empty list to append cleaned dataset)
dict_df = {}

for file in files:
  # DATA LOADING (2014-15, 2015-16)
  if (file[0:7] == '2014-15' or file[0:7] == '2015-16'):
    year = file[0:7]

    # Load df from a sheet "(year)"
    df = pd.read_excel(file, sheet_name = year)
    
    # Create a new column "Income year" to df
    # Use forloop to insert file of "(year)" to "Income year" column
    df['Income year'] = year

  # DATA LOADING (2016-17 ... 2019-20)                
  else:
    # Load df from a sheet "Income tax details" 
    df = pd.read_excel(file, sheet_name = 1)

  # Final Merge: add "df" to "dict_df" (save each cleaned dataframe by appending to empty list)
  year = file[2:4]
  df = df[df['Total income $'] >= 200000000].reset_index(drop = True)
  df.dropna(subset=['ABN'], inplace =True)
  df = df.rename(columns={'Total income $' : 'Total income_' + year, 'Taxable income $' : 'Taxable income_' + year, 'Tax payable $' : 'Tax payable_' + year})
  dict_df[file[0:7]] = df
  

dict_df['2014-15']

"""# New Section

**2.** For dataframes that disclose more than one year of data, filter out any late filings. i.e. Only keep data related to 2013-2014 that was disclosed in December of 2015 and same idea for all other years. Any data that is filed later will engender a later change in behavior, if any, which would make it harder to measure.
"""

for year in dict_df.keys() : 
  dict_df[year] = dict_df[year][dict_df[year]['Income year'] == year]
  dict_df[year] = dict_df[year].drop('Income year', axis = 1)

"""**3.** Perform a wide merge in which each firm has only one row of data and subsequent years of information are presented in additional columns."""

df_public_private = df_public_private.rename(columns={'Total income $' : 'Total income_' + '13',
                                                      'Taxable income $' : 'Taxable income_' + '13',
                                                      'Tax payable $' : 'Tax payable_' + '13'})
df_public_private = df_public_private.drop('Income Year', axis = 1)
df_public_private.head()

df_merge = df_public_private
for year in dict_df.keys() : 
  df_merge = pd.merge(df_merge, dict_df[year], how = 'left', on = ['Name', 'ABN'])

df_merge

"""**4.** Remove any excess columns that we no longer need.

**5.**	Once the data is in a wide format and only includes the firms you want to keep for your analysis, reformat the data into a traditional panel data format (each row relates to one time period for one firm). Follow the following three steps:
1. Reformat the data to be extra long such that each row is a different value (Taxable Income, Tax Payable, or Total Income) for each firm for each year.
2. Create a column that indicates which time period each row relates to.
3. Reformat the data again to be slightly wider such that each firm-year is one row and there is a different column for Taxable Income, Tax Payable, and Total Income (in addition to name and ABN and filing status). Your data should look as if you stacked the original seven DataFrames on top of each other. Using this longer process ensures that you only keep the firms you want to keep for a proper analysis.


As a check point, your final DataFrame should have data relating to **154 unique private firms and 643 unique public firms**.
"""

# Wide to extra long format
df_melt = pd.melt(df_merge, id_vars = ['Public/Private', 'Name', 'ABN'])
# Create column with time period
df_melt[['Metric', 'Income Year']] = df_melt['variable'].str.split('_', expand=True)
df_melt.drop('variable', axis = 1, inplace = True)
df_melt['Income Year'] = '20' + df_melt['Income Year']

# Reformat the data
df_reshaped = df_melt.pivot_table(index = ['Name', 'ABN', 'Public/Private', 'Income Year'], columns = 'Metric', values = 'value').reset_index()

df_reshaped

print("Number of unique public firms : ", str(df_reshaped[df_reshaped['Public/Private'] == 'public'].Name.nunique()))
print("Number of unique private firms : ", str(df_reshaped[df_reshaped['Public/Private'] == 'private'].Name.nunique()))

"""**6.	Once your final dataset is transformed, make sure that it is fully clean and ready for analysis.**

   **a.**	As noted on the first tab of the excel files, negative taxable incomes are not disclosed. Instead, this field is left blank. Similarly, tax liabilities of zero are not disclosed. For these firms, their tax payable field is left blank. Replace all taxable income and tax payable missing values with zero.

"""

df_reshaped[['Tax payable', 'Taxable income']] = df_reshaped[['Tax payable', 'Taxable income']].fillna(0)
df_reshaped.columns.name = ''
df_reshaped

"""**6b.**	Make sure all datatypes are appropriate. If not, adjust accordingly."""

df_reshaped.dtypes

df_reshaped['ABN'] = df_reshaped['ABN'].astype('int') 
df_reshaped['Income Year'] = df_reshaped['Income Year'].astype('int')

"""**6c.**	Take some time to understand the data you are working with. Are there any biases, errors or incomplete items that concern you? No need to explicitly answer that question but keep it in mind when performing the rest of your analysis. You can learn more about the data [here](https://www.ato.gov.au/Business/Large-business/In-detail/Tax-transparency/Corporate-tax-transparency-report-for-the-2014-15-income-year/)."""

df_reshaped.info()

"""**Export your data as a pickle file so that you can easily import it into part 2 of this case.**"""

# export cleaned data as a pickle file

# replace final with name of your dataframe
final = df_reshaped

# 'part1.p' is the name of the file that is exported
final.to_pickle('part1.p')

"""At a minimum, you must turn in your 3 questions before you can receive access to part 2 so that your questions are not influenced by the questions you will answer in Part 2. I am giving you leniency in how to manage your time but I highly recommend having your questions done and MOST of the cleaning done before class on 10/17. The whole case is due a week later on 10/24."""