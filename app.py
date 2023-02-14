from fastapi import FastAPI
from pydantic import BaseModel
from mlxtend.frequent_patterns import apriori
import pickle

# Initialize the FastAPI
app = FastAPI()

# Load the pre-trained apriori model
model = pickle.load(open('basketAnalysis.pickle', 'rb'))

# Create a class to store the user input
class UserInput(BaseModel):
    product: str

# Create a route for the API
@app.post("/predict")
def predict(user_input: UserInput):
    # Get the user input
    product = user_input.product
    
    # Make predictions using the model
    predictions = model.apriori(product)
    
    # Return the prediction
    return {
        "Product": product,
        "Recommendations": predictions
    }