import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'movie': [
        'Inception',
        'Inception',
        'Inception',
        'Inception',
        'Titanic',
        'Titanic',
        'Titanic',
        'Titanic',
        'Avatar',
        'Avatar',
        'Avatar',
        'Avatar',
        'The Matrix',
        'The Matrix',
        'The Matrix',
        'The Matrix',
        'Interstellar',
        'Interstellar',
        'Interstellar',
        'Interstellar',
    ],
    'user': [
        'A',
        'B',
        'C',
        'D',
        'A',
        'B',
        'C',
        'D',
        'A',
        'B',
        'C',
        'D',
        'A',
        'B',
        'C',
        'D',
        'A',
        'B',
        'C',
        'D',
    ],
    'rating': [
        9,
        8,
        9,
        10,
        7,
        8,
        6,
        9,
        8,
        10,
        9,
        7,
        10,
        9,
        8,
        9,
        10,
        9,
        10,
        8,
    ],
    'genre': [
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Romance',
        'Romance',
        'Romance',
        'Romance',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
        'Sci-Fi',
    ],
}

df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 2)
axes[0].set_title('Average Rating By Title')
axes[1].set_title('Average Rating By Genre')
movie_ratings = df.groupby('movie')['rating'].mean()
genre_ratings = df.groupby('genre')['rating'].mean()
sns.barplot(
    color='darkgreen', ax=axes[0], y=movie_ratings, x=movie_ratings.index
)
sns.barplot(color='purple', ax=axes[1], y=genre_ratings, x=genre_ratings.index)
sns.set_style('dark')
for tick in axes[0].get_xticklabels():
    tick.set_rotation(45)
plt.show()
