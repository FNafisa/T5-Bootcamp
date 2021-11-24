#### Pair Problem

Same deal as the first regression + feature engineering pair. There are 3 datasets in the 'data' folder that have
 not been split into train-val-test. Do the split yourself and see how high you can get the score on the test set to be.

Try to explore all the datasets, so don't spend too much time on one. Some of them are tough/tricky, but there is a 
little lesson behind each. 

Here is starter code:

    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    import pandas as pd
    
    df = pd.read_csv('data/1.csv')
    X_train, X_test, y_train, y_test = train_test_split(df[['x1','x2','x3','x4','x5']], df['y'], test_size=0.33, random_state=42)
    
    m = LinearRegression()
    m.fit(X_train,y_train)
    m.score(X_train,y_train)
    m.score(X_test,y_test)
