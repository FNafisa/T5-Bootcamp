#### Pair Problem

I have generated two datasets and I want to see how you can model each of them using Linear Regression in sklearn.

There are two pairs of files in the data folder. For each pair (*1_train.csv*, *1_test.csv* for example),
 build a model using the features and target in the training data, and then test on the test data. 

For this problem, the better score a model can produce on the test set, the better the model is. 
Your task is to get the best possible model. 

You are welcome to view, plot, and explore the training data as much as you please (you can also generate new features, drop rows, etc). 
But you can only do two things with the test data: read it to a DataFrame and use it to score your model. **Note**: you
may also need to perform the same feature engineering steps on the test data as you did on the train data. 

Here is some starter code. You can use this as a starting point for all two datasets.

    from sklearn.linear_model import LinearRegression
    import pandas as pd
    
    df = pd.read_csv('data/1_train.csv')
    df_test = pd.read_csv('data/1_test.csv')
    
    m = LinearRegression()
    m.fit(df[['x1','x2']],df['y'])
    m.score(df[['x1','x2']],df['y'])
    
    m.score(df_test[['x1','x2']],df_test['y'])
