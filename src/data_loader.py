import pandas as pd
import numpy as np

def load_data():
    # For your 6-hour sprint, we'll generate mock data if files don't exist
    try:
        ratings = pd.read_csv("data/raw/ratings.csv")
        stories = pd.read_csv("data/raw/stories.csv")
    except:
        stories = pd.DataFrame({
            'storyId': range(1, 101),
            'title': [f"Story {i}" for i in range(1, 101)],
            'genres': np.random.choice(['Romance|Drama', 'Horror|Thriller', 'Fantasy', 'Mystery'], 100)
        })
        ratings = pd.DataFrame({
            'userId': np.random.randint(1, 21, 500),
            'storyId': np.random.randint(1, 101, 500),
            'rating': np.random.randint(1, 6, 500)
        })
    return ratings, stories