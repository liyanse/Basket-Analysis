from typing import List
from fastapi import FastAPI, File, UploadFile
import joblib

app = FastAPI()

# Load your trained recommender system model
model = joblib.load("basketAnalysis.pickle")

@app.post("/recommend/")
async def recommend(user_preferences: List[str]):
    # Use the model to make recommendations based on the user's preferences
    recommendations = model.predict(user_preferences)
    return {"recommendations": recommendations}