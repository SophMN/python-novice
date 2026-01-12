##Creating, reading and writing

#Import pandas library
import pandas as pd

#Create a pandas DataFrame
pd.DataFrame({'Yes': [20, 21], 'No': [130, 3]})

pd.DataFrame({'Bob': ['Disagree', 'Neutral'], 
              'Sue': ['Strongly agree', 'Agree']})

#Adding row labels using the index parameter
pd.DataFrame({'Bob': ['Disagree', 'Neutral'], 
              'Sue': ['Strongly agree', 'Agree']}, 
              index = ['Question1', 'Question2'])

#Pandas Series
pd.Series([30, 35, 40], index = ['2015 sales', '2016 sales', '2017 sales'], 
name = 'ProductA')

#Reading data
ebola_data = pd.read_csv("ebola_data_db_format.csv")

#Get the dimensions of the data
ebola_data.shape

#Get the first and last 5 entries of the dataset
ebola_data.head()
ebola_data.tail()
