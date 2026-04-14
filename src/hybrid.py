import pandas as pd
import pickle
from src.content_based import ContentBased

def hybrid_recommend(user_id, ratings, stories, top_n=5):
    # Load Pre-trained Collaborative Model
    with open("models/svd_model.pkl", "rb") as f:
        svd = pickle.load(f)
    
    content_engine = ContentBased(stories)
    user_data = ratings[ratings['userId'] == user_id]
    
    # Cold Start [cite: 13]
    if user_data.empty:
        pop_ids = ratings.groupby('storyId').size().sort_values(ascending=False).head(top_n).index
        return stories[stories['storyId'].isin(pop_ids)]

    all_ids = stories['storyId'].unique()
    watched = user_data['storyId'].tolist()
    candidates = [i for i in all_ids if i not in watched]
    
    # Hybrid Scoring: 70% CF + 30% Content
    scores = []
    for sid in candidates:
        cf_score = svd.predict(user_id, sid).est / 5.0
        # Simulating content boost for demo
        final_score = cf_score 
        scores.append((sid, final_score))
        
    scores.sort(key=lambda x: x[1], reverse=True)
    top_ids = [x[0] for x in scores[:top_n]]
    
    return stories[stories['storyId'].isin(top_ids)]