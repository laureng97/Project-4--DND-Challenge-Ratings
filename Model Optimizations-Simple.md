# Model Decisions and Optimizations

This document hopes to catalog the testing and optimization of the machine learning model for this project.

## Initial Model Testing

***Which type of model should we create to train our model on?***

### Random Forest Model

Initial Model Performance Results  
Mean Absolute Error (MAE): 0.8745576923076924  
Mean Squared Error (MSE): 1.8194926682692307  
R² Score: 0.9421731254340034  

### Linear Regression Model

Initial Model Performance Results  
Mean Absolute Error (MAE): 0.9295491226103343  
Mean Squared Error (MSE): 1.5490721701816692  
R² Score: 0.9507675938238425  

### Ridge Regression Model

Initial Model Performance Results  
Mean Absolute Error (MAE): 0.9620136056352142  
Mean Squared Error (MSE): 1.5827684584436645  
R² Score: 0.9496966628612464  

### Gradient Boosting Regressor Model

Initial Model Performance Results  
Mean Absolute Error (MAE): 0.9813791427579789  
Mean Squared Error (MSE): 2.3888187835194996  
R² Score: 0.924078878379389  

**Results:** Linear Regression Models should be the best fit for our data set.

## Linear Model Improvements

***What improvements to the initial Linear Regression model can be made?***

**Initial Model**  
Initial LinReg. Model with StandardScaler for numeric columns and OneHotEncoder for categorical text columns  
*Performance Results:*  
Mean Absolute Error (MAE): 0.9295491226103343  
Mean Squared Error (MSE): 1.5490721701816692  
R² Score: 0.9507675938238425  

**SlantedLogarithm Model**  
like Initial Model, but before StandardScaling numeric columns, apply `np.log1p` to all columns with a `skew` value greater than 0.5  
*Performance Results:*  
Mean Absolute Error (MAE): 1.1908070739552812  
Mean Squared Error (MSE): 2.5867197052850703  
R² Score: 0.917789217542053  
