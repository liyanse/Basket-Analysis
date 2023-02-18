from fastapi import FastAPI
import pickle

app = FastAPI()

with open('apriori_model.pkl','rb')as f:
    rules = pickle.load(f)

@app.get('/products/{product_name}')
def similar_products(product_name:  str):
    results = [rule[2] for rule in rules if rule[1] == product_name]
    
    return{'similar products are': results}
       
    