from fastapi import FastAPI
import pickle

app = FastAPI()

with open('apriori_model.pkl','rb')as f:
    rules = pickle.load(f)

@app.get('/products/{product_name}')
def similar_products(product_name:  str):
    results = [result[1] for result in rules if result[0] == product_name]
    
    return{'similar products are': results}

       
    