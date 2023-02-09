from fastapi import FastAPI
from mlxtend.frequent_patterns import apriori
import pickle

# create the fastapi object
app = FastAPI()

# load the pickle file
model_file = open('basketAnalysis.pickle', 'rb')
model = pickle.load(model_file)

# create the endpoint
@app.get("/market_basket/{product1}/{product2}/{support}/{confidence}")
def market_basket_recommender(product1: str, product2: str, support: float, confidence: float, lift: float):
    recommendations = model.apriori(product1, product2, support, confidence, lift)
    return {"recommendations": recommendations}