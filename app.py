from fastapi import FastAPI
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from pydantic import BaseModel

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

@app.post('/predictdemand')
async def product_rec(dataframe, product, stop_num = 3):
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
product_rec(rules, "soda")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload