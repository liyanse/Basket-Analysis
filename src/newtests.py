from fastapi import FastAPI
import pandas as pd 
import pickle
from apyori import apriori

app = FastAPI()

@app.get("/recommend/")
def recommend(product: str):
    #Read the dataset
    data = pd.read_csv('Groceries_dataset.csv')
    data.head()

    # Grouping the member's basket by the id, date and the number of items in the basket
    basket = data.groupby(['Member_number','Date'])
    basket.count()

    # Convert it into a dataFrame
    data.groupby(['Member_number','Date'], as_index = False)['itemDescription'].sum()

    # Let's try to see what items where in the baskets from transactions
    list_transactions = [i[1]['itemDescription'].tolist() for i in list(basket)]
    list_transactions[:20]

    # Building the rules for apriori with the customer's baskets in list_transactions
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

    #make recommendations
    recommendations = list(final_result[final_result['Antecedent'].str.contains(product)].sort_values(by='Support(%)', ascending=False)['Consequent'])

    return {"Recommended products": recommendations}