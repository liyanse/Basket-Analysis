##Importing the necessary libraries
import numpy as np
import pandas as pd
from fastapi import FastAPI
## for association rules
from apyori import apriori
import warnings; warnings.simplefilter('ignore')

## Reading the dataset
df = pd.read_csv("Groceries_dataset.csv")
## Grouping the member's basket by the id, date and the number of items in the basket
basket = df.groupby(['Member_number','Date'])
basket.count()

## Convert it into a dataFrame
df.groupby(['Member_number','Date'], as_index = False)['itemDescription'].sum()

## Let's try to see what items where in the baskets from transactions
list_transactions = [i[1]['itemDescription'].tolist() for i in list(basket)]
list_transactions[:20]

## Building the rules for apriori with the customer's baskets in list_transactions
rules = apriori(list_transactions, min_support=0.001, min_confidence=0.05, min_lift=1.2, min_length=2, max_length=2)

results = list(rules)

def inspect(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    support = [result[1]*100 for result in results]
    confidence = [result[2][0][2]*100 for result in results]
    lift = [result[2][0][3] for result in results]
    return list(zip(lhs,rhs,support,confidence,lift))
final_result = pd.DataFrame(inspect(results), columns=['Antecedent','Consequent','Support(%)','Confidence(%)','lift'])
final_result['Rule'] = final_result['Antecedent'] + '->' + final_result['Consequent']

final_result

# Use FASTAPI to deploy the model
from fastapi import FastAPI

app = FastAPI()
@app.get("/predict")
def predict_basket(Product1: str):
    # Get the rules related to the input item
    item_rules = rules([Product1])
        # Sort the rules by the lift in descending order
    item_rules = item_rules.sort_values(by='lift', ascending=False)
    
    # Return the consequents of the top 5 rules
    return item_rules['consequents'].head().to_list()