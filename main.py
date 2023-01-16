from fastapi import FastAPI
import uvicorn
import pickle

app = FastAPI()

@app.get("/")
def home():
    return{"text": "Market basket analysis"}

@app.get('/predict')
def predict(Product1: str, Product2:str):
    model = pickle.load(open('C:/Users/Lian.s/Desktop/Basket Analysis/basketAnalysis.pickle'))
    makeprediction = model.predict([[Product1, Product2]])
    output = round(makeprediction[0],2)
    
    return{'You can buy products like: {}'.format(output)}

    
    
    
    
if __name__ == '__main__':
    uvicorn.run(app)
