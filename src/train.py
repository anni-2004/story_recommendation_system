from surprise import Dataset, Reader, SVD
import pickle
import os

def train_model(ratings):
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings[['userId','storyId','rating']], reader)
    trainset = data.build_full_trainset()
    
    model = SVD(n_factors=50, n_epochs=20)
    model.fit(trainset)
    
    os.makedirs("models", exist_ok=True)
    with open("models/svd_model.pkl", "wb") as f:
        pickle.dump(model, f)
    return model