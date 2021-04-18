# Project 3

## Project Description
* Using two machine learning methods predict population values at 100 x 100 meter resolution throughout your selected country.
* Validate the two models using different methods presented in this class.
* Write a report assessing the two approaches and which of the two models was more accurate. Be sure to account for spatial variation throughout your selected location and provide substantive explanations for why those variations occurred.

## Data
I chose to model the population of Jordan. Jordan is a small country (both area and number of residents), so there were not very administrative boundaries, which meant that the data was easier for the model to process for the whole country.

#### Actual population of Jordan
![ActPop](https://sglott.github.io/Data310_workbook/ActPop.png)

#### Validation Methods:
* Simple difference between actual and predicted population values
* Mean Absolute Error
* Root Mean Squared Error

## Linear Regression
#### Population predicted by Linear Regression Model
![LRpop](https://sglott.github.io/Data310_workbook/LR_pop.png)

#### Difference between LR predicted population and actual population (subtracted actual population from predicted population)
![LRpopdiff](https://sglott.github.io/Data310_workbook/LR_popdiff.png)
![LRstats](https://sglott.github.io/Data310_workbook/LRStats.png)
![diffLR](https://sglott.github.io/Data310_workbook/diffLR.png)

The figure showing population difference across the country along with the statistics showing actual vs. predicted population numbers indicates that the linear regression model underpredicts the population. According to the simple validation shown above, the most underpredicted areas were the urban areas and the most overpredicted areas were the rural areas. Because the first validation method was very simple, I tried MAE and RMSE. 

#### LR Mean Absolue Error
![LRMAE](https://sglott.github.io/Data310_workbook/MAELR.png)

#### LR Root Mean Squared Error
![LRrmse](https://sglott.github.io/Data310_workbook/rmseLR.png)

Both the MAE and RMSE further emphasize the underprediction in the urban areas. Maybe the Random Forest model will better predict population. 

## Random Forest
#### Population predicted by Random Forest Model
![RFpop](https://sglott.github.io/Data310_workbook/RFpop.png)

#### Most important variable for predicting population
![LRvarimp](https://sglott.github.io/Data310_workbook/LRvarimp.png)

#### Difference between RF predicted population and actual population (subtracted actual population from predicted population)
![RFpopdiff](https://sglott.github.io/Data310_workbook/RFpopdiff.png)
![RFStats](https://sglott.github.io/Data310_workbook/RFStats.png)
![diffRF](https://sglott.github.io/Data310_workbook/diffRF.png)

The figure showing population difference across the country along with the statistics showing actual vs. predicted population numbers indicates that the random forest model underpredicts the population. According to the simple validation shown above, the most underpredicted areas were the urban areas and the most overpredicted areas were the rural areas. Because the first validation method was very simple, I tried MAE and RMSE. 

The linear regression model just barely predicted population better than the random forest model according to the simple difference validation. Linear regression had a 8959955 difference and random forest had a 9000918 difference.

#### RF Mean Absolute Error
![RFMAE](https://sglott.github.io/Data310_workbook/MAERF.png)

#### RF Root Mean Squared Error
![RFrmse](https://sglott.github.io/Data310_workbook/rmseRF.png)

Both the MAE and RMSE further emphasize the underprediction in the urban areas. The Random Forest model did not perform better. Maybe if we narrow down the view from the whole country, to just the most populated area, the model will perform better. 

## Spatial Variation
