from fastapi import FastAPI
import pickle
import uvicorn ##ASGI
from urllib import response
import pandas as pd
from pydantic import BaseModel
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# 2. Create the app object
app = FastAPI()

@app.get('/')
def index():
    return {'Welcome To Our Product Recommender API'}

class filter(BaseModel):
    
    start_date:str
    end_date:str

class product(BaseModel):
    product_id:str
    
    
@app.post('/predictbasket')
async def product_rec(filter:filter):
    response = filter.dict()
    response_df = pd.DataFrame(response)
    cols = ['member_number', 'date','itemDescription']
    response_df[cols] = response_df[cols].applymap(lambda x: True if x>0 else False)
    model = pickle.load(open("basket.pkl", "rb"))
    counter = 0
    rec_list = []
    for index, row in enumerate(dataframe["antecedents"]):        
        for item in list(row):
            if item == product:
                rec_list.append(list(dataframe["consequents"][index])[0])
                counter += 1
                if counter == stop_num:
                    break
    return rec_list


