# -*- coding: utf-8 -*-
"""
"""
##!pip install fastapi uvicorn

# 1. Library imports
from urllib import response
# from sci.demand_forecasting.app.mains import *
import uvicorn ##ASGI
import pickle
import pandas as pd
from fastapi import FastAPI
from sklearn.preprocessing import LabelEncoder

from pydantic import BaseModel

# 2. Create the app object
app = FastAPI()

@app.get('/')
def index():
    return {'Welcome To Demand Forecasting API'}


class filter(BaseModel):
    start_date:str
    end_date:str

class product(BaseModel):
    product_id:str

@app.post('/predictdemand')
async def demandpredictor(filter:filter):
    response = filter.dict()
    response_df = pd.DataFrame(response)
    cols = ['inventory_id', 'product_name', 'category', 'uom', 'warehouse_id','order_date',
        'customer_id', 'customer_name', 'county', 'subcounty']
    response_df[cols] = response_df[cols].apply(LabelEncoder().fit_transform)
    model = pickle.load(open("../Models/sarimaxmodel.pkl", "rb"))
    predictions = model.predict(response_df)
    # res = totalprods.to_json(orient="records")
    return predictions

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload


