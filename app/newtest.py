import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

#read the dataset
df = pd.read_csv("Groceries_dataset.csv")

#transaction encoder
te = TransactionEncoder()
te_ary = te.fit(df).transform(df)
df = pd.DataFrame(te_ary, columns=te.columns_)

#apriori algorithm 
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)

#save the model as a pickle file
frequent_itemsets.to_pickle("apriori_model.pkl")

#load the pickle file
frequent_itemsets = pd.read_pickle("apriori_model.pkl")

#take user input
product = input("Enter a product: ")

#make recommendations
recommendations = list(frequent_itemsets[frequent_itemsets['itemsets'].str.contains(product)].sort_values(by='support', ascending=False)['itemsets'])
print("Recommended itemsets: ", recommendations)



#Importing Libraries
import pandas as pd
import numpy as np
from apyori import apriori
import pickle

#Reading the dataset
df = pd.read_csv('groceries.csv')

#Creating a list of lists using the transactions
transactions = []
for i in range(0, len(df)):
    transactions.append([str(df.values[i, j]) for j in range(0, len(df.columns))])

#Building the model
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

#Sorting the rules by lift
rules = sorted(rules, key = lambda x: x[2][0][3], reverse = True)

#Saving the model
pickle.dump(rules, open("model.pkl", 'wb'))

#Loading the model
model = pickle.load(open("model.pkl", 'rb'))

#Function to recommend similar products
def recommend_products(product):
    #Creating an empty list
    recommended_products = []
    #Iterating through the rules
    for i in range(len(model)):
        #Iterating through the left side of the rules
        for j in range(len(model[i][2][0][0])):
            if(product == model[i][2][0][0][j]):
                recommended_products.append(model[i][2][0][1])
    return recommended_products

#Testing the function
recommend_products('whole milk')

#Deploying the model
#Creating a FastAPI
from fastapi import FastAPI

#Creating an instance of FastAPI
app = FastAPI()

#Creating a route
@app.get("/recommend/{product}")
def recommend(product):
    return recommend_products(product)