import pandas as pd 
from mlxtend.frequent_patterns import apriori

# Load the Groceries dataset
data = pd.read_csv('Groceries_dataset.csv')

# Transform the data into a one-hot encoding
data_hot_encoded = data.drop('Item(s)', axis=1).apply(pd.Series.value_counts)
data_hot_encoded = data_hot_encoded.fillna(0).astype(int).reset_index()

# Run the Apriori algorithm to generate frequent itemsets
frequent_itemsets = apriori(data_hot_encoded, min_support=0.01, use_colnames=True)

# Generate the rules from the frequent itemsets
from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Use FASTAPI to deploy the model
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_item(item: str):
    # Get the rules related to the input item
    item_rules = rules[rules['antecedents'] == {item}]
    
    # Sort the rules by the lift in descending order
    item_rules = item_rules.sort_values(by='lift', ascending=False)
    
    # Return the consequents of the top 5 rules
    return item_rules['consequents'].head().to_list()