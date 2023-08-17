import matplotlib.pyplot as plt
import pandas as pd
netflix_df = pd.read_csv('dataSets/netflix_data.csv')

# filtering data for genre movie
subset_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# getting columns
movies_only = subset_movies_only[[
    'title', 'country', 'genre', 'release_year', 'duration']]

# creating scatter plot
# fig = plt.figure(figsize=(12, 8))
# plt.scatter(movies_only['release_year'], movies_only['duration'])
# plt.title('movie duration by year')
# # plt.show()

# filtering short movies
short_movies = movies_only[movies_only['duration'] < 60]
print(short_movies[0:20])

# Marking non feature films
colors = []
for lab, row in movies_only.iterrows():
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('green')
    elif row['genre'] == 'Stand-Up':
        colors.append('blue')
    else:
        colors.append('black')

print(colors[0:20])

# Ploting results
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12, 8))

plt.scatter(movies_only['release_year'], movies_only['duration'], c=colors)
plt.xlabel('release year')
plt.ylabel('duration (min)')
plt.title('movie duration by year release')

plt.show()
