# Linear Regression Practice

The purpose of today's pair is to use sklearn and fit a model of your own.

#### Part 1: Read in and explore the data
Read in the two data sets in this folder. 

#### Part 2: Create visualizations to explore the data
Use Seaborn's heatmap function (```sns.heatmap()```) to visualize the correlations between the variables. 
Use Seaborn's pairplot function (```sns.pairplot()```) to visualize the relationship between each variable.  
What do these plots tell you?

#### Part 3: Fit and score a model
Fit a model on the train set and score it on both the train and test sets. Compare the R-squared values. What do these results mean?

#### Part 4: Go beyond R-squared
Use the below code snippet to calculate the RMSE (root mean squared error) on both the train and test sets. What do these results mean?

```
from sklearn.metrics import mean_squared_error
from math import sqrt
```
