from fastapi import FastAPI
import pickle

app = FastAPI()

with open('apriori_model.pkl','rb')as f:
    rules = pickle.load(f)
    
 
@app.get("/recommendations/{product}")
def get_recommendations(product: str):
    # Get the recommendations based on the input product
    recommendations = [x for x in rules if product in x[0]]
    # Return the recommendations
    return {"recommendations": recommendations}
