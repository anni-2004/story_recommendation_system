from fastapi import FastAPI
import sys
import os

# Add root to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_data
from src.preprocess import preprocess
from src.hybrid import hybrid_recommend

app = FastAPI()
ratings, stories = load_data()
ratings = preprocess(ratings)

@app.get("/recommend/{user_id}")
def get_recs(user_id: int):
    recs = hybrid_recommend(user_id, ratings, stories)
    return recs.to_dict(orient="records")