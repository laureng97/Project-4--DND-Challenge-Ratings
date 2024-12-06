# Model Decisions and Optimizations

This document hopes to catalog the testing and optimization of the machine learning model for this project.

## Initial Model Testing

***Which type of model should we create to train our model on?***

### Random Forest Model

Initial Model Performance Results 
Mean Absolute Error (MAE): 0.8332692307692307  
Mean Squared Error (MSE): 1.655410769230769  
R² Score: 0.947387954578258  

### Linear Regression Model

Initial Model Performance Results  
Mean Absolute Error (MAE): 0.838766290841251  
Mean Squared Error (MSE): 1.2481504025734464  
R² Score: 0.9603314495145673  

### Ridge Regression Model

Initial Model Performance Results  
Mean Absolute Error (MAE): 0.8560257329830987  
Mean Squared Error (MSE): 1.2788014059602113  
R² Score: 0.9593573033918162  

### Gradient Boosting Regressor Model

Initial Model Performance Results  
Mean Absolute Error (MAE): 0.8871108948733702  
Mean Squared Error (MSE): 1.9670740985394144  
R² Score: 0.9374827119988  

**Results:** Linear Regression Models should be the best fit for our data set.

## Linear Model Improvements

***What improvements to the initial Linear Regression model can be made?***

**Initial Model**  
Initial LinReg. Model with StandardScaler for numeric columns and OneHotEncoder for categorical text columns  
*Performance Results:*  
Mean Absolute Error (MAE): 0.838766290841251  
Mean Squared Error (MSE): 1.2481504025734464  
R² Score: 0.9603314495145673  

**SlantedLogarithm Model**  
like Initial Model, but before StandardScaling numeric columns, apply `np.log1p` to all columns with a `skew` value greater than 0.5
*Performance Results:*  
Mean Absolute Error (MAE): 1.0715546579837305  
Mean Squared Error (MSE): 1.9414245724477757  
R² Score: 0.9382979018337716  