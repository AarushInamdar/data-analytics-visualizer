import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


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

def repp(string):
    return string.replace("[","").replace("]","").replace("u'","").replace("',",",")[:-1]
#Apply that function to every entry    
movies_series = movies['actors_list'].apply(repp)
#Declare a list to store the split values
actors_list = []
for movie_actors in movies_series:
    actors_list.append([e.strip() for e in movie_actors.split(',')])
#Declare a dictionary and see if the actor name key exist and then count accordingly.
actor_dict = {}
for actor in actors_list:
    for a in actor:
        if a in actor_dict:
            actor_dict[a] +=1
        else:
            actor_dict[a] = 1

actor_dict


# Assuming 'data' has a 'Director' and 'Rating' column
# Convert categorical 'Director' to numeric
data['Director_code'] = data['Director'].astype('category').cat.codes

# Prepare features (X) and target (y)
X = data[['Director_code']]  # More features can be added here
y = data['Rating']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate the model
predictions = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, predictions))


# Split actors and explode the DataFrame
data['Actors_list'] = data['Actors'].str.split(',')
exploded_actors = data.explode('Actors_list')

# Analyze the average rating per actor
actor_ratings = exploded_actors.groupby('Actors_list')['Rating'].mean().sort_values(ascending=False)

# For a large dataset, consider visualizing the top 20 actors
sns.barplot(x=actor_ratings.head(20).values, y=actor_ratings.head(20).index)
plt.title("Average Rating for Top 20 Actors")
plt.show()


# Assuming 'data' has a 'Genre' and 'Rating' column
# Splitting genres since a movie can have multiple genres
data['Genres'] = data['Genre'].str.split(',')

# Explode the DataFrame so each genre gets its own row
exploded_genres = data.explode('Genres')

# Now, you can perform analysis on genres
genre_ratings = exploded_genres.groupby('Genres')['Rating'].mean().sort_values(ascending=False)
sns.barplot(x=genre_ratings.index, y=genre_ratings.values)
plt.xticks(rotation=90)
plt.title("Average Rating by Genre")
plt.show()


# Split actors and explode the DataFrame
data['Actors_list'] = data['Actors'].str.split(',')
exploded_actors = data.explode('Actors_list')

# Analyze the average rating per actor
actor_ratings = exploded_actors.groupby('Actors_list')['Rating'].mean().sort_values(ascending=False)

# For a large dataset, consider visualizing the top 20 actors
sns.barplot(x=actor_ratings.head(20).values, y=actor_ratings.head(20).index)
plt.title("Average Rating for Top 20 Actors")
plt.show()
