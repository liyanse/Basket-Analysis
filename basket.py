import pandas as pd
import numpy as np

## for association rules
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import warnings; warnings.simplefilter('ignore')

df =pd.read_csv("Groceries_dataset.csv")

df["InvoiceNo"] = df["Member_number"].astype(str) + "_" + df["Date"]
df.groupby(["InvoiceNo"] , as_index = False)['itemDescription'].sum()
