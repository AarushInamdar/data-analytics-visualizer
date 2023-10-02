import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

yourCSVLink = 'IMDB-Movie-Data.csv' #enter your own csv link here to view trhe data analytics and statistics on that csv

data = pd.read_csv(yourCSVLink)

topTen = data.head(10) #providing top ten rows of the data set

bottomTen = data.tail(10) #providing bottom ten rows of the data set

dataShape = data.shape #getting the shape of the data with the shape attribute of the pandas library

print("Number of rows: ", dataShape[0])
print("Number of columns: ", dataShape[1])

dataInfo = data.info #register all the information into a variable using the pandas attribute .info

print("Are there any missing values? - ", data.isnull().values.any())  #Checks the data frame to consider whether there is a null value or not

nullData = data.isnull().sum() #shows all the areas where the data is null

sns.heatmap(data.isnull()) # creates a heatmap of all the areas where there is null data using seaborn heatmap method

percent_missing = nullData * 100/len(data) #shows what percent of values are missing from which column

print(percent_missing)

clearedData = data.dropna(axis=0) #dropna method of pandas helps us view on all rows and columns with proper data in them

dupData = data.duplicated().any() #checks whether there is any amount of duplicates in the data and whether or not it 

print("Are there any duplicate values in our data: ", dupData) 

data = data.drop_duplicates()

data.describe() #use describe method to sow the quantiles, min, max, median, std, count and box plots of the values for the given values | overall statsitics for the data set are given

# data.describe('all') | includes categorical and numerical values in the description as shown above

cols = data.columns #getting the column name attributes using the .columns panda attribute

data[data['Runtime (Minutes)']>=180]['Title'] #attributes edited and based on what qualifications you prefer, here it is by the amount of minutes as a minimum you want
     
highestVotes = data.groupby('Year')['Votes'].mean().sort_values(ascending=False) #Obtain the ascneidng order of votes in a given year by the number of votes in each year

sns.barplot(x='Year', y="Votes", data=data) #Creating a bar plot to show relationship between categorical data and numerical data, in thgis case the year and the amount of votes in that year
plt.title("Votes by year")
plt.show()

highestRevenue = data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)
sns.barplot(x='Year', y="Revenue (Millions)", data=data) #Creating a bar plot to show relationship between categorical data and numerical data, in thgis case the year and the revenue in that year
plt.title("Revenue by year")
plt.show()

data.groupby('Director')['Rating'].mean().sort_values(ascending=False) #getting the highest mean ratings for each director

largestRuntime = data.nlargest(10, 'Runtime (Minutes)') #getting the highest (top 10) number of directors lengthy movies and returning their title and runtime

largestRuntime.set_index('Title')

print(largestRuntime)

sns.barplot(x='Runtime (Minutes)',y=largestRuntime.index, data=largestRuntime) #Creates a barplot with the largest runtime of the given data



