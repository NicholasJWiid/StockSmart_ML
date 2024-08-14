# StockSmart_ML

## Live Website: https://stocksmartml.pythonanywhere.com/

## Team Members
Debbie Lim, Marco Martinez, Nate Whipple, Owen Wang, Nicholas Wiid


## Overview
Stocksmart ML aims to use machine learning to find a new investment strategy. We study the impact of multiple factors from 2015-2023 against the individual stocks in the 2024 S&P 500 stocks. Factors considered include the following:

CEO Factors: gender, salary, tenure
Company Factors: GICS sector, headquarter location
External Factors: year, interest rate, consumer Price Index (CPI), unemployment rate, GDP growth rate

Our project aimed to determine if this particular selection of company and economic factors had an impact on a company’s stock performance. Stock performance was measured in relation to the S&P 500 index using the compound annual growth rate (CAGR) metric. CAGR measures how much an investment grows over some period. In our analysis, we measured the CAGR of individual companies for each year between 2015 and 2023 against the CAGR of the S&P 500 for the same years. If an individual stock had a CAGR greater than the S&P 500 CAGR, it was classified as “outperforming” the market. This classification column was the target of our Machine Learning testing. By looking at 500 companies over 9 years, we compiled approximately 4500 data points (it was actually about 4300 because not all companies were in business for all 9 years).


## Tools, Libraries and Languages
Tools: postgresql, Jupyter notebook
Libraries: flask, chart.js, sklearn, matplotlib, tensorflow, pandas, hvplot
Languages: python, javascript, CSS


## Data Sources
We retrieved a list of the current S&P 500 companies from an online search.

From here, we manually researched information related to CEO compensation, CEO gender, CEO transition, and CEO tenure. This research was conducted via Google searches with the help of ChatGPT. We also hired a friendly Bengladeshi research team to help with a small portion of this work.

CEO salary information was found on the AFL-CIO’s “Highest Paid CEOs” page.

Data points related to CPI, GDP, Employment Rates, and Interest Rates were found on various government websites.

Definitions for measures like CAGR were also found via web searches.

Historical stock data was retrieved from YFinance (Yahoo Finance’s API).


## Financial Definitions
The S&P 500 is a market-capitalization-weighted index of 500 leading publicly traded companies in the United States. Standard and Poor’s, a credit rating agency, launched the index in 1957. Since its inception, the S&P 500 has served as an important benchmark through which to measure the performance of the American equity market and the American economy at large.

Eligibility Criteria:
** Must be a U.S.-domiciled company
** Must have a primary listing on one of the major U.S. exchanges
** Must be a corporation issuing equity, mortgage REITs, or common stock
** Must have a market ≥ $18B

The S&P 500 is reconstituted annually, after market close of the third Friday in June.

The index is weighted by float-adjusted market capitalization every quarter. The weights of individual company performance on the index changes depending on the quarterly updates to the market cap metrics. Companies that fall below the market cap threshold are removed but no new companies are added until the next reconstitution date.

Limitations of the S&P 500:
The top 500 companies, exclude the mid and small-cap companies. Macroeconomic conditions can affect these stocks differently. A more thorough analysis would report on the same metrics for the mid and small-cap markets.

In an ideal world, we would have looked at all companies listed in the US, as well as incorporated many more economic and corporate indicators.


## Model Approach
We applied a comprehensive approach to unsupervised and supervised learning to explore the data and determine the best algorithms. 


### Unsupervised Learning - Stock clusters
In unsupervised learning our goal was to review clustering of stock performance combined with company factors to identify stocks with the highest annual return and lowest annual variance. We used daily data to calculate annual means (mean open, mean high, mean low, mean close) as well as annual return and annual variance for each stock for each year, and included several company features (Sector, Headquarters location and CEO Gender). Numeric data was scaled using the scikit-learn preprocessing function StandardScaler(), and categorical variables were converted to numeric data using the pandas .get_dummies() function. The Elbow method was then used to determine the optimal number of clusters, whereby the KMeans algorithm was used to cluster the data. The cluster results were then visualized using a scatter plot, plotting Annual Return (y axis) vs Annual Variance (x axis).


### Supervised Learning
For Supervised learning we chose to use both classification and neural network algorithms to test the different approaches.


#### Data preparation
Data was prepared in the same way for both approaches. Monthly data was extracted for each stock and each year from 2015 to 2023. Year values were then computed for each year (year open, year high, year low, year close, and year volume), after which the CAGR was calculated for each stock. The same variables were then calculated for the S&P 500 index for each year, including the S&P 500 CAGR and the datasets were merged. A new column was then added to the dataset showing the “outcome” of the CAGR comparison, indicating if the stock CAGR for any given year had outperformed the S&P 500 CAGR (1 for yes and 0 for no). This was the target of our Machine Learning testing. External economic factors (Interest Rate, CPI, Unemployment Rate and GDP Growth Rate) and company specific factors (Sector, Sub-Sector, Year Founded, CEO Gender, CEO Transition, CEO Tenure, Headquarters US state or other Country, and CEO Salary Range) were then merged for each year of the data for each stock/company. Finally, all stock price and CAGR columns were dropped from the dataframe (Year_Open, Year_High, Year_Low, Year_Close, Year_Volume, Stock_CAGR, SP500_Open, SP500_High, SP500_Low, SP500_Close, SP500_CAGR) to create the final machine learning dataframe.


#### Data preprocessing
Data was then preprocessed to be ready for the classifier and neural network models. Categorical variables were converted to numeric data using the pandas .get_dummies() function. The data was split into features (company and economic factors) and the target array (Outcome of the CAGR comparison), and further split into training data and testing data, with a rough ratio of 3 to 1 training to testing. Training and testing features were then scaled using the scikit-learn preprocessing function StandardScaler().


### Supervised Learning - Classification
For Classification Unsupervised learning, our goal was to test different models to compare confusion matrices and classification report results to find the best one. We ran four different classifier models (KNN, ExtraTrees, Random Forest, Bagging Classifier) to review confusion matrices, classification reports and feature importances. For the decision tree classification algorithms, we were further able to extract the feature importance for each feature in the model, which was then plotted in a bar graph. The feature importance is a measure of the percentage impact each feature has on the total model accuracy.


### Supervised Learning - Neural Network
For Neural Network modeling our goal was to test different configurations with more and less features to maximize model accuracy. We created 6 models, each with a different number of layers and nodes, and multiple tests for each model choosing either 50, 100 or 200 epochs. Model test schedule shown below.
ADD Neural Network - Model Test Details IMG

Finally, a model optimization technique was run using the keras tuner. This technique is designed to find the best model, testing all possible model configurations within the given tuner parameters. Parameters chosen for this optimization process were based on the model tests conducted previously. The following tuner parameters were fed into the optimizer: Any number of layers between 3 and 5; Any number of nodes between 10 and 128; A maximum epochs 50; An activation function of either ‘relu’ or ‘tanh’.


## Results
### Unsupervised learning - Cluster results
The point of this exercise was simply to see if distinct clusters were identifiable based on the stock performance data. The “Stocks by Cluster - Annual Return vs Annual Variance” chart below shows the results of the stock clustering exercise. Each color represents a different cluster.

https://github.com/deleyeem/StockSmart_ML/blob/main/images/Stocks%20by%20Cluster.png

The chart shows the stocks separated into five relatively distinct clusters based on the variables compared:
Red: Low return, high variance.
Grey: Low return, low to medium variance.
Blue: Low to medium return, low variance.
Yellow: Low return, low variance.
Green: Medium to high return, low variance.

For any particular investment strategy, stocks with medium to high return and low variance would be the most favorable to include. These particular stocks in this Green cluster would need to be analyzed further and this would then be built into a future iteration of a model that can consistently identify these high performers.

The second “Stocks by Gender” chart below, shows the same data except that the stocks are now colored by CEO gender. 
https://github.com/deleyeem/StockSmart_ML/blob/main/images/Stocks%20by%20Gender.png

At a high level it appears that companies run by women have in general lower annual variance in stock prices than companies run by men. However, this result may be due to a much lower % of female CEO run companies showing on the chart, and further analysis would be required to confirm this finding. Investigating and controlling for possible causation would help further tease out phenomena associated with the benefits of diverse leadership.


### Supervised learning - Classification Results
The accuracy scores of the four classifier models run are as follows:
** Bagging Classifier: 0.68
** Random Forest: 0.66
** Extra Trees: 0.65
** KNN: 0.52

From the perspective of the Confusion Matrix, the goal in this particular case is firstly to maximize the number of True Positives, and secondly to maximize the number of True Negatives. A successful model would show very few False Positives and False Negatives, which would mean that the model is good at using company factors to determine stock performance. True positives would be priority, because this would then become a major determinant in choosing to invest in that particular stock, which according to a highly accurate model would be correctly predicting exceptional stocks. True negatives in the results are obviously less desirable because the goal is to find strong investment opportunities, however, this knowledge is still useful as it would indicate what not to invest in.

The most accurate model in our analysis was the Bagging classifier, showing:
** 376 True Negatives
** 353 True Positives
** 187 False Positives
** 176 False Negatives

https://github.com/deleyeem/StockSmart_ML/blob/main/images/Classification%20-%20Bagging%20Classifier%20confusin%20matrix.png

The second most accurate model in our analysis was the Random Forest, showing:
** 380 True Negatives
** 341 True Positives
** 183 False Positives
** 183 False Negatives

The Random Forest model showed slightly lower True Positives and higher True Negatives, which is why it achieved a lower overall accuracy. There is clearly plenty of room for improvement on the classifier model, with the aim to reduce the number of False Negatives and False Positives.
https://github.com/deleyeem/StockSmart_ML/blob/main/images/Classification%20-%20RandomForest%20-%20Confusion%20Matrix.png

From a feature importance perspective, the chart below shows the feature importance contributions for the top 20 features, ranked by their contribution.
https://github.com/deleyeem/StockSmart_ML/blob/main/images/Classification%20-%20RandomForest%20-%20Features%20Importance.png

All the economic factors show the highest importance (between 3-4%), likely due to their equal effect of every stock. The rest of the top twenty features are made up of various values for Tenure, Salary and Sector, all with relatively low influence in their individual capacity (1-1.5%). This highlights the lack of influence of one or two particular factors (for example CEO demographics) on stock performance in this particular analysis.  
https://github.com/deleyeem/StockSmart_ML/blob/main/images/Classification%20-%20ExtraTrees%20Feature%20Importance.png

Looking at the Extra Trees feature importance, we do see CEO gender and CEO Transition appearing in the top 20 influential features, however, they both only have around 1% influence on the model on their own.


### Supervised learning - Neural Network Results
#### Initial Model Test Results
The table below outlines the best test result for each of the six models run.
https://github.com/deleyeem/StockSmart_ML/blob/main/images/Neural%20Network%20-%20Results%20Summary%20R1.png

The progression of modeling that the model achieves high accuracy with additional layers and more nodes, with the best accuracy score being achieved in model 5 with 4 layers, 256 nodes per layer, run for 50 epochs, using the ‘relu’ activation function, and with the Sub-Sector and Founded Year features removed.


#### Model Optimization Results
Optimization was run with the keras tuner as described in the model approach above.
The best model hyper parameters are shown in the image below, with 6 layers, a range of 15 - 125 nodes per layer, run for 7 epochs, using the ‘relu’ activation function, and with the Sub-Sector and Founded Year features removed.
activation function, 
https://github.com/deleyeem/StockSmart_ML/blob/main/images/Optimization%20Model%20Rank%201.png

This best model was able to achieve an accuracy score of 0.62 as shown in the image below.
https://github.com/deleyeem/StockSmart_ML/blob/main/images/Optimization%20Model%20Rank%201%20-%20Results.png


## Conclusions
Our model failed to confidently determine that women perform better than men in the stock performance of the companies they lead. It did provide evidence that female-led companies have more stable stock returns. Overall, the outputs of our model indicate that we cannot consider the model to be accurate enough to make real word stock performance predictions. However, the accuracy was still higher than expected for the limited number of features able to be collected and included within the two week project timeframe. In industry, we know that AI/ML are used extensively in stock picking, but successful models are some of the most tightly held secrets, as they are highly profitable. One of the main weaknesses of our model are the limitations in factors studied and the limitation in time period studied. A true test of our model would require putting our money where our mouth is and using the model to pick stocks in the future, then test whether the predictions come true, then fine-tuning our model against larger trends.

Overall, both the classifier and the neural network models appear to benefit from fewer features, although more testing will be required to determine how slim the model can get while maintaining this accuracy. More likely to have an impact on the model would be the inclusion of additional features that have a stronger influence on overall company performance. With an accuracy of 0.68 for the best classifier model and 0.62 for the best neural network there is still some way to go to conclude with any certainty that the model is correctly classifying at a highly accurate level. 

We would like to build our model to use more robust factors. Examples of additional potentially useful factors include:

Financial Factors
** Revenue and revenue growth and related metrics like price to earnings
** Debt-to-Equity Ratio
** Cash Flow
** Operational Factors
** CapEx
** R&D Expenditure
** Revenue per employee
** Market Factors
** Market Capitalization
** rading Volume
** Qualitative Factors
** Management Team
** Brand Strength

