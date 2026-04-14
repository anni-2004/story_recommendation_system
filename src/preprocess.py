def preprocess(ratings):
    # Only keep high-engagement signals (Rating >= 4) [cite: 13]
    return ratings[ratings['rating'] >= 4].copy()