import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from fastapi import FastAPI

app = FastAPI()

@app.get("/recommendations")
def get_recommendations(product: str):
    # Read in the dataset
    df = pd.read_csv("Groceries_dataset.csv")

    # Convert the dataframe into a list of lists
    data = df.values.tolist()

    # Use the TransactionEncoder to convert the list of lists into a one-hot encoded numpy array
    te = TransactionEncoder()
    te_ary = te.fit(data).transform(data)

    # Create a dataframe from the one-hot encoded numpy array
    df = pd.DataFrame(te_ary, columns=te.columns_)

    # Use the apriori function to find frequent itemsets
    frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)

    # Create a dictionary of the items and their corresponding support values
    items = frequent_itemsets['itemsets'].apply(lambda x: x.name)
    support = frequent_itemsets['support'].tolist()
    item_support = dict(zip(items, support))

    # Find the products that are frequently bought with the input product
    recommendations = []
    for itemset in frequent_itemsets['itemsets']:
        if product in itemset:
            recommendations.extend(list(itemset))
    recommendations = list(set(recommendations) - set([product]))

    # Sort the recommendations by support value and return the top 5
    recommendations = sorted(recommendations, key=lambda x: item_support[x], reverse=True)[:5]
    return recommendations

