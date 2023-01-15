# %% [markdown]
# # Homework 2
# 
# Nothing in this notebook should be hard coded except when I ask you to input data such as in Exercise 1a.

# %% [markdown]
# <font color='red' size = '5'> Exercise 1: Lists </font>
# 
# **a.** Make a list with 6 numerical values. Include at least one number above 100, one number with decimals, and one negative number. Make sure your list is not in ascending or descending order and name your list ``mylist``.

# %%
# enter your answer here

mylist = [101, 0.5, -2, 50, 20, 30]

# %% [markdown]
# **b.** Use list subsetting to extract the second item in the list and save it to a variable named ``second``.

# %%
mylist[1:-4]

second = mylist[1:-4]

second

# %% [markdown]
# **c.** Raise the variable ``second`` to the 3rd power and name the resulting solution ``third``.

# %%
third = 0.5**3
third

# %% [markdown]
# **d.** Use list subsetting to make a new list named ``newlist`` that includes every other item, starting with the second item from your first list.

# %%
newlist = mylist[1::]
newlist

# %% [markdown]
# **e.** Save the minimum value in ``newlist`` as ``lowest``.

# %%
lowest = min(newlist)
lowest

# %% [markdown]
# <font color='red' size = '5'> Exercise 2: Dictionaries </font>
# 
# **a.** Make a dictionary to store the following data:
# 
# - 3 keys- each the name of a course you are taking
# - 3 values for each key- expected difficulty (easy, medium, hard), expected grade, level of enthusiasm for the subject (1-10)
# 
# Make sure at least one class has an expected difficulty of 'easy' but that not all have an expected difficult of 'easy'.
# 
# Name your dictionary ``classes``.

# %%
classes = {'Act499r' : ['hard','b',5], 'Isom352' : ['medium','a',6], 'Isom475' : ['easy','a',7]}
classes

# %% [markdown]
# **b.** Use dictionary subsetting and a list method to add an item that specifies whether the second course in your dictionary is an elective or required course.

# %%
classes['Isom352'] = ['medium','a',6,'elective']
classes

# %% [markdown]
# **c.** Add a fourth class to your dictionary with the same three values you listed for the other courses.

# %%
classes['Fin423'] = ['hard','a',6]
classes

# %% [markdown]
# **d.** Write a for loop to print out the following information for each class in your dictionary:
# ```python
# 
# Classname  Expected Difficulty
# ```

# %%
for key, value in classes.items():
    print(key, str(value[0]))

# %% [markdown]
# **e.** Write a for loop that only prints your expected grade for a subject *if* you labeled the expected difficulty as 'easy'. Output should look like:
# 
# ```python
# 
# Classname Expected Grade
# ```

# %%
for key, value in classes.items():
    if value[0] == "easy":
        print(key, str(value[1]))

# %% [markdown]
# <font color='red' size = '5'> Exercise 3: Functions </font>
# 
# Use a function to calculate the future value of a \$10 investment made today. The investment will earn 2\% per year and you plan to invest the money for 50 years. Make your code dynamic (easy to update). Save your answer under the variable name ``investment``.

# %%
import math

interest = 0.02
time = 50
loan = 10
payment = 0

# %%
investment = loan*(1+interest)**time
investment

# %% [markdown]
# <font color='red' size = '5'> Exercise 4: NBV Function </font>
#     
# Finish the function we started in class on Wednesday: 
# 
# Create a function that calculates the net book value of an asset. 
# 
#    <font size = 4> Net Book Value = Historical Cost - Accumulated Depreciation </font>
# 
# **Note that we should not depreciate below the asset's residual value.** This consideration should be included in your function.

# %%
#approach 1:
#Net Book Value = Historical Cost - (Per Year Depreciation x Total Number of Years of Using it)
#we need 4 arguments (historical_cost, accumulated_depreciation (annual_depreciation, total_years))
#we need to define the function and put those 4 arguments

def net_book_value(historical_cost, accumulated_depreciation):
    accumulated_depreciation = (annual_depreciation*total_years)
    return(net_book_value)

# %%
#approach 2: assign the dictionary and loop it with depreciation value and using boolean value for the condition for the "we should not depreciate below the asset's residual value"
data = {'Chair': [50, 10, 3],
        'Table': [100, 10, 5],
        'Building': [500000, 100000, 25],
        'Land': [150000, 100000, 100]}

# %%
data.items()

# %%
def dep(historical_cost, salvage_value, useful_life):
    return (historical_cost - salvage_value)/useful_life

# %%
def net_book_value(historical_cost, periods):
    for k, v in data.items():
        if dep (v[0], v[1], v[2]) > v[1]:
            print(k, "Not Depreciated")
        else:
            acc_dep = dep (v[0], v[1], v[2])*periods
            nbv = int(historical_cost - acc_dep)
        return(nbv)

# %%
net_book_value (100,5)

# %% [markdown]
# <font color='red' size = '5'> Exercise 5: Markdown </font>
# 
# Add a cell below and make it a markdown cell. In that cell answer the following questions:
# 
# a. On a scale from 1-10, what is your current comfort level with Python and the content we have covered so far?
# 
# b. What if anything are you currently struggling the most with in Python?

# %%
# a. 5 overall
# b. Creating loops that have multiple lists and key values within them. I still need to look at my notes back and forth and think.

# %% [markdown]
# <font color='red' size = '5'> Extra Credit: Nested Loop </font>
#     
# Create a dictionary that holds the same four assets we studied in class.
# 
# Create a loop that iterates over the assets in our dictionary over 10 years and returns the net book value of each asset in each year.
# 
# Note: Your answer will have two loops- one nested inside of another. You may want to play around with which loop should be the outside versus inside loop. Be sure to use the net book value function you created in exercise 4.

# %%
assets = {'Table' : ['total_years'], 'Chair' : ['total_years'], 'Building' : ['total_years'], 'Land' : ['total_years']}
assets

# %%
def net_book_value(historical_cost, accumulated_depreciation):
    accumulated_depreciation = (annual_depreciation*total_years)
    return(net_book_value)

for key, value in assets.items():
    if value >= '10':
        print(key + net_book_value)

# %% [markdown]
# ## Read for Monday's Class
# 
# In class next week we will complete Trina’s Trinkets case study. Please read the first 2 pages and skim pages 3 and 4 of Trina’s Trinkets so that you’re familiar with the scenario.


