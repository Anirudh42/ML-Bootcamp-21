#!/usr/bin/env python
# coding: utf-8

# # ML Bootcamp 2021 - Week 1: Assignment
# 
# - Please Read the Instructions very very carefully.
# - Name the variables exactly as is mentioned in the comments
# - Failure to do so would result in the grader marking the values wrongly
# - If the comment asks you to name the variable 'a' then name it 'a' and not 'A'
# - ****Please do not remove any missing values from the dataset for the following calculation****

# ## Q1. Create a list of integers starting from 1 to 100,000 where each number is squared.

# In[2]:


# Write your code below the comments in this cell
# Important
# Save you list in a variable called 'squared_integers'
# Example: squared_integers = [1, 4, 9, 16, 25, 36,....., 100000000]

squared_integers = [i**2 for i in range(100000+1)]


# ## Q2. Create a function to print the maximum of two given values

# In[3]:


# Write your code below the comments in this cell
# Important
# The name of the function should be max_two_numbers
# The function SHOULD ONLY return EXACTLY 1 value which is the maximum of the two numbers
def max_two_numbers(a,b):
    return max(a,b)


# ## Q3. How many columns and rows are there in the test dataset?

# In[5]:


# Write your code below the comments in this cell
# Important
# Save your row value in a variable called 'row'
# Save your columns value in a variable called 'col'
row = 418
col= 11


# ## Q4. What is the youngest and oldest Age recorded on the ship (Train dataset)?

# In[6]:


# Write your code below the comments in this cell
# Important
# Save your youngest Age value in a variable called 'age_youngest'
# Save your oldest Age value in a variable called 'age_oldest'
age_youngest=0.42
age_oldest=80


# ## Q5. What are the proportions of male and female passengers (Train dataset)?

# In[7]:


# Write your code below the comments in this cell
# Important
# Save the integer number for female passengers in a variable called 'female_count'
# Save the integer number for male passengers in a variable called 'male_count'
female_count=314
male_count=577


# ## Q6. What is the average ticket price per Passenger Ticket Class(Train dataset) ?

# In[8]:


# Write your code below the comments in this cell
# Important
# Save the value for each ticket class as a variable called "p_classnumber_avg_fare" (Eg: p_1_avg_fare)
p_1_avg_fare = 84.15
p_2_avg_fare = 20.66
p_3_avg_fare = 13.68


# ## Q7. Explore the 'Names' feature and find out how many titles are present? A title stands for 'Mr', 'Miss', 'Dr' etc. appended before any person's name (Train dataset). 
# - Hint: Check the "Strings" part of the tutorial notebook

# In[9]:


# Write your code below the comments in this cell
# Important
# Your output should be a dictionary called 'title_count'
# Each key of the dictionary is the name of the title as is, Eg: Mr, Miss, Mrs, etc.
# Value of each key is the number of times that that particular title has occurred
# Example output
# {'Mr':5,'Capt':20,'Miss':12 and so on}
title_count = {'Capt': 1,
 'Col': 2,
 'Countess': 1,
 'Don': 1,
 'Dr': 7,
 'Jonkheer': 1,
 'Lady': 1,
 'Major': 2,
 'Master': 40,
 'Miss': 182,
 'Mlle': 2,
 'Mme': 1,
 'Mr': 517,
 'Mrs': 125,
 'Ms': 1,
 'Rev': 6,
 'Sir': 1}


# In[ ]:




