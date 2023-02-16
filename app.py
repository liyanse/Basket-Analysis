import pickle
from typing import List
from fastapi import FastAPI

app = FastAPI()

## loading my apriori algorithm
with open('association_rules.pkl', 'rb') as f:
    apriori_model = pickle.load(f)
    
    
@app.post("/recommend")
def recommend_product(products: List[str]):
    # perform basket analysis on the list of products
    recommended_product = apriori_model.final_result(products)
    return {"recommended_product": recommended_product}
    
    
    
    