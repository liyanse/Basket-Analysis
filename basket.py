import pandas as pd
import numpy as np
import pickle
import uvicorn ##ASGI

## for association rules
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import warnings; warnings.simplefilter('ignore')

df =pd.read_csv("Groceries_dataset.csv")

df["InvoiceNo"] = df["Member_number"].astype(str) + "_" + df["Date"]
df = df.groupby(["InvoiceNo", "itemDescription"])["itemDescription"].count().unstack(). \
fillna(0)

df = df.applymap(lambda x: True if x>0 else False)

frequent_itemsets = apriori(df, min_support=0.001, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.01)
rules

#lift değerine göre sıralıyoruz ve ürün tavsiyesi verecek olan fonksiyonu yazıyoruz
rules = rules.sort_values("lift", ascending=False).reset_index(drop=True)  

def product_rec(dataframe, product, stop_num = 3):
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
product_rec(rules, "yogurt")
