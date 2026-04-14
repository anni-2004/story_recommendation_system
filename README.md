# StoryRanker

A hybrid recommendation system built to simulate how content platforms personalize what users see. The focus here is less about the model itself and more about building a proper end-to-end ML system — training pipeline, inference, API serving, and a frontend all working together.

---

## Why I built this

Most recommendation tutorials stop at "train a model and print some predictions." I wanted to go further and actually wire everything together the way you'd see it in production: a separate training step, a serving layer, and a UI that talks to it. The goal was to understand how these pieces connect, not just how the math works.

---

## How it works

Users generate interaction signals (ratings, reads). The system learns from those signals to predict what a given user will enjoy. For new users with no history, it falls back to popular content so they still get something useful.

---

## Approach

**Collaborative Filtering (SVD)**
Learns patterns from user-item interaction data. If two users rated similar stories highly, they probably share taste — so surface content one user liked to the other.

**Content-Based Filtering**
Uses genre metadata to find stories similar to ones a user has already engaged with.

**Hybrid Scoring**
Final score = 70% collaborative signal + 30% content similarity. This blends personalization with item-level features.

**Cold Start Fallback**
New users with no history get the most popular stories until enough signal accumulates.

---

## Project structure

```
StoryRanker/
├── src/          # core ML logic (data loading, preprocessing, models)
├── api/          # FastAPI backend — serves recommendations
├── app/          # Streamlit frontend — UI for testing
├── models/       # saved trained models
├── data/         # raw and processed datasets
└── main.py       # training entry point
```

---

## How to run

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Train the model**
```bash
python main.py
```

**Start the API**
```bash
uvicorn api.app:app --reload
```

**Start the frontend** (in a separate terminal)
```bash
streamlit run app/app.py
```

Then open the Streamlit app, enter a user ID, and get recommendations.

---

## Current status

- [x] System architecture designed and implemented
- [x] Hybrid recommendation logic working
- [x] FastAPI backend serving predictions
- [x] Streamlit frontend connected to the API
- [ ] Model training on real dataset (in progress)
- [ ] Evaluation metrics (precision@k, recall@k)
- [ ] Deployment

---

## What I focused on

The ML part here is not novel — SVD and content filtering are well-known techniques. What I cared about was the system design:

- **Separation of concerns**: training is decoupled from inference
- **Cold start handling**: new users don't get a blank screen
- **Extensibility**: the hybrid scorer is easy to tune or swap out
- **Real serving**: the model runs behind an actual API, not just a notebook

This is closer to how recommendation systems work in practice, where the engineering layer matters as much as the model.

---

## Next steps

- Train on the MovieLens dataset and evaluate properly
- Add a content-based score that actually uses TF-IDF or embeddings instead of the placeholder
- Log recommendation quality metrics
- Deploy the API somewhere accessible

---

## A note

This is a learning project. The dataset is MovieLens mapped to a "stories" domain as a proxy. The architecture reflects how I'd approach this problem in a real system, even if the data and scale are simplified.
