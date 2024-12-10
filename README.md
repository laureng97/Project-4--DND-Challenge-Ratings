# Project Theme: Dungeons and Dragons Challenge Ratings

# Datasets used: 
We used two resources to pull information for this project:

-Kaggle Dataset: https://www.kaggle.com/datasets/shadowtime2000/dungeons-dragons?select=monsters.csv
Contained 5 CSV’s about Monsters, Equipment, Race, Classes, and Spells
Mainly focused on the Monsters CSV, which contains 322 unique monster records


-DND API: 
https://www.dnd5eapi.co/
This is the 5th edition Dungeons and Dragons API, the dataset above pulled information from this API


# Project Description
For background: Dungeons & Dragons (D&D) is a collaborative role-playing game (RPG) where players work together to tell a story in a fantasy world, playing as fantasy heroes to fight monsters, grow stronger, and work through a story told by the Dungeon Master (DM).

Our group wants to create a machine learning model that can give a designated monster a Challenge Rating (CR) based on the monster's attributes, such as hit points (HP), Speed, attacks and abilities. 

# Notable Sources
https://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options (read_csv error clearing)
https://www.geeksforgeeks.org/replace-nan-values-with-zeros-in-pandas-dataframe/ (NaN data filling)
https://aspm.faa.gov/aspmhelp/index/Types_of_Delay.html [explanation for presentation]](https://www.geeksforgeeks.org/show-all-columns-of-pandas-dataframe-in-jupyter-notebook/ (for display of data columns for cleaning)
https://saturncloud.io/blog/matplotlib-bar-chart-spacing-out-bars-for-better-data-visualization/ (bar chart spacing)
https://saturncloud.io/blog/how-to-replace-a-string-value-with-nan-in-pandas-data-frame-python/ (null replacements for cleaning)
https://saturncloud.io/blog/what-is-the-best-way-to-remove-characters-from-a-string-in-pandas/ (string cleanup)
https://docs.python.org/3/library/stdtypes.html#str.title (string cleanup helping)
*We also would like to note that Alexis suggested we use hyperparameter tuning for our linear regression model and pointed us to this resource: https://www.geeksforgeeks.org/hyperparameter-tuning-in-linear-regression/*
*It should also be noted that when Lauren encountered an issue with github not deploying a dynamic page that would provide the predictions, she used chat GPT to see what her options were for site hosting*


# Contributions
This project was a collaborative effort of the following individuals: Andrew Pohle, Caitlin McMahill, Jessica Maranto, and Lauren Graves. 
The code files are labeled "Data_Cleaning_SQL_ML_Models.ipynb" and "Monsters EDA.ipynb". Please reference our dataset resources and presentation resources for the source of additional information we obtained and used during the presentation. 

# Files
The coding files can be found in the folder labeled "Monsters EDA.ipynb" and "Data_Cleaning_SQL_ML_Models.ipynb. 
The SQL database is labeled "monsters.db"
The html and flask files are labeled "app.py" and "index.html". Please note the requirements.txt file is needed for the flask to run properly.  
The slide presentation used is in the folder labeled "Presentation". 
The data set csv files are in the "Resources" folder. 

# Data Observations (Exploratory Data Analysis)
Prior to creating the machine learning model, we wanted to learn more about the data we had on hand. We looked at overall Challenge Rating Counts across all monsters. The most common being 2, and least common being 19. We also looked at Monster size distribution, to see what size was more or less common. Medium and large sized monsters are fairly common, where as gargantuan accounts for less than 20 of the 322 monsters. 

![Challenge_Rating_Overall](https://github.com/user-attachments/assets/9b9e5983-afed-464f-8a1c-54deed9aab7d)


![Monster_Size_Distribution](https://github.com/user-attachments/assets/32883fee-a553-455e-8e1d-3f636e21b747)


We looked at average Hit Points (HP) and average Armor Class (AC) by Challenge Rating (CR).These features are essential to understanding the monsters durability and defense varies with their CR. The higher the CR the higher HP and AC are. Both HP and CR increase as CR increases, but HP tends to scale more significantly. As monsters become stronger they can survive more damage. 

![Average_HP](https://github.com/user-attachments/assets/bd4a3774-c486-49ac-892b-f6407d8db0f6)

![Average_CR](https://github.com/user-attachments/assets/f15c0b23-6514-471e-b7bb-d13d813203b2)

We also wanted to see what the stat averages were for Monsters per their Challenge Rating. We can also see that dexterity tends to be the highest stat amongst lower challenge rated Monsters. We can see that strength and constitution  go up in average as challenge rating increases. This is key information, since constitution is a measure of a character’s health, stamina, and vital force. Essentially it allows a character to withstand a lack of food, fight off disease/poison, and last longer during combat.

![Stat_Averages_Per_CR](https://github.com/user-attachments/assets/27a1a73a-ae49-4f53-bfa3-144d41ed19ef)

Why Analyze Distribution of Damage Immunities?
Game Balance Insight:
Knowing which damage types are frequently immune can help identify common monster traits, potentially influencing player strategy (e.g., avoid relying on fire attacks if "fire immunity" is very common).
 
Model Training:
When building a machine learning model, knowing the prevalence of damage immunities can guide feature selection (e.g., a highly common immunity like "poison" might carry less predictive power than rare ones).

![Most_Common_Damage_Immunities](https://github.com/user-attachments/assets/151eab59-7e6b-4990-8c7e-b23553d1d7a4)

Correlation Heatmap for Attributes
Goal: 
Identify relationships between monster stats (e.g., strength, dexterity) and challenge rating to inform ML model features.
How This Helps:
Identifies which attributes (e.g., strength, hit points) correlate strongly with challenge rating.
Features with strong correlations are likely to be important predictors in machine learning models.

![Correlation_Stat_CR](https://github.com/user-attachments/assets/7ceaea4e-d489-4d98-aa1d-28446d58127b)


# Model Analysis and Optimizations

The next step in predicting the data was to determine what type of machine learning model could be effectively used on the data we have. We tested many different model types; chief among them were Random Forest, Linear Regression, Ridge Regression, and Gradient Boosting Regressor.

All 4 created models were given their default parameters, trained on the full dataset, and were scored on Mean Absolute Error (MAE), Mean Squared Error (MSE), and R2. In the end, the best-working model of these choices was the Linear Regression model.

![Models_Results](https://github.com/user-attachments/assets/67e03d60-36d4-430f-98a6-02d0f6750d5e)

Further testing was done using GridSearchCV to determine the optimal parameters for each model, to get a better grasp on which model would work the best for the data.We attempted to perform hyperparameter tuning on the linear model, but it brought the R-squared value down. 

![Hyperparameter_Tuning](https://github.com/user-attachments/assets/6be0345a-b90c-4c35-b1aa-a90e3dab605e)

While the models optimized with GridSearchCV made a strong showing in terms of accuracy, the initial test of the Linear Regression Model ultimately has the best performance stats of all models tested on our data, and should thus be the optimal model to use in our CR prediction software.

# The Active Site
This site allows the user to input their own monster data for creation. The tool will predict the monster's challenge rating based on all of the features that are input! *Please note that most monsters do end up with a higher than usual challenge rating, based on our predictive model*

https://laureng97.github.io/Project-4--DND-Challenge-Ratings/

# Future Enhancements and Research
While the models optimized with GridSearchCV made a strong showing in terms of accuracy, the initial test of the Linear Regression Model ultimately has the best performance stats of all models tested on our data, and should thus be the optimal model to use in our CR prediction software.

