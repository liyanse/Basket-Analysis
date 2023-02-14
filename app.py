from fastapi import FastAPI
from pydantic import BaseModel
from mlxtend.frequent_patterns import apriori
import pickle

# Initialize the FastAPI
app = FastAPI()

@app.get("/predict/{product}")
def get_recommendation(product: str):
    # load the model
    model = pickle.load(open('basketAnalysis.pickle','rb'))
    # make prediction
    results = model[model.Antecedent == {product}]
    # return results
    return results