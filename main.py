from src.data_loader import load_data
from src.preprocess import preprocess
from src.train import train_model

if __name__ == "__main__":
    ratings, stories = load_data()
    ratings = preprocess(ratings)
    train_model(ratings)
    print("✅ Training Complete. Models saved to /models/")