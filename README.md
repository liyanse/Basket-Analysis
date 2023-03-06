Market basket analysis is a data mining technique that is used to identify association rules between items in large data sets of transactional data. It is used to identify which items are frequently purchased together in order to understand consumer behavior and to identify potential opportunities for product bundling or cross-selling.

For example, a market basket analysis of a grocery store's transaction data might reveal that customers who purchase bread are very likely to also purchase butter. This information could be used to create a product bundle (e.g., a "baking essentials" bundle including bread and butter) or to cross-sell butter to customers who are purchasing bread (e.g., by placing the butter near the bread in the store).

### For this project we will be;

1. Analyse and preprocess the dataset
2. Visualize the weekly, monthly and yearly sales and draw insights from the plotted graphs
3. Visualize the top and bottom selling products
4. Visualize the top customers for this business
5. Genarate association rules to be used to determine the relationships of the products
6. Identify the frequently purchased products4. Association Rules with Apriori Algorithm

### Association Rules with Apriori Algorithm
Association Rules are based on the concept of strong rules, are widely used to analyze retail basket or transaction data and are intended to identify strong rules discovered in transaction data using measures of interestingness. Association rules are used to unveil the relationship between one item and another when purchased, mainly denotes as X and Y. X is the main product being purchased while Y is the best product to be bought together with X. These rules are developed by three terminologies;

1. Support - It is used to represent the number of transactions in which product X appears from thee total number of transactions. That is, the popularity of product X.
2. Confidence - It is the likelyhood that product Y being purchased when item X is purchased.
3. Lift -  This says how likely item Y is purchased when item X is purchased while controlling for how popular item Y is.
The Apriori algorithm generates association rules, but it does so under the condition that

1. All subsets of the frequent itemset must all be frequent.
2. For any infrequent itemset all it's supersets must be infrequent too
The method may take some time to construct if all rules are taken into account, thus if the lift of these chosen itemsets (rules) is less than a threshold, the rules are removed. the Apriori algorithm generates association rules, but it does so under the condition that

1. Subsets of the frequent itemset must all be frequent.
2. Similar to this, the algorithm operates in such a way that iterations take place with frequent itemsets and a minimum support value is determined if an infrequent subset has an infrequent parent set. Until removal is impossible, itemsets and subsets are disregarded if their support falls below the threshold.
The method may take some time to construct if all rules are taken into account, thus if the lift of these chosen itemsets (rules) is less than a threshold, the rules are removed.


### Getting Started
The requirements for this project are,
Have the following installed;
  - apriori
  - pandas
  - FastAPI
  - Uvicorn
1. The first srep is to clone this repo 
$ git clone https://github.com/liyanse/Basket-Analysis

2. Install the necessary libraries
I have definetely not included all the libraries used in this project but I have listed some of them in the requirements.txt file

 3. Run the main.py file with uvicorn (since we are using FASTApi, we have to use Uvicorn server to run our endpoint)
 4. Alternatively, you can build a docker image from the docker file provided in the project, just run the following commands
 $ docker build -t 'imagename' .  
 
 Then run the image file as; 
 $ docker run -p 80:80 'imagename'
 
 The termnal should give you a link and when you open the link, replace it with
 localhost:80 , it should return the message "Welcome to the Recommendations platform"
 


## API
I chose to deploy this algorithm with fastapi where a user inputs a product and it recommends other products based on the association rules developed.
This is a snippet of what the deployment looks like;
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sqetevka9vwjk3f4ugwf.png)
