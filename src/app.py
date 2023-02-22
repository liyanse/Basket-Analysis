##Importing the necessary libraries
from fastapi import FastAPI
import pickle

## Create FASTAPI instance
app = FastAPI()

## opening the pickle file for predictions
with open('apriori_model.pkl','rb')as f:
    rules = pickle.load(f)
    
# Define the GET request endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Recommendations platform"}
    
 
@app.post("/recommendations/{product}")
async def get_recommendations(product:str):
    # Get the recommendations based on the input product
    recommendations = [x for x in rules if product in x[0]]
    # Return the recommendations
    return {"recommendations": recommendations}
