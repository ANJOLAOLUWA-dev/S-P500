<h1>S&P 500 Stock Price Analysis & Prediction</h1>

<p>This is a machine learning project focused on predicting stock price movements in the S&P 500. I used Python to build multiple regression models and a Command Line Interface (CLI) to simulate daily closing price predictions. The project explores historical stock data, applies feature engineering techniques, and evaluates various models to determine the most accurate one.</p>

<h2>About</h2>
<p>The dataset used in this project contains historical price data from the S&P 500 index. It includes multiple months of daily trading activity and captures financial indicators such as Open, High, Low, Close, and Volume. The aim of this project was to predict the next day's closing price using these features, allowing for a practical understanding of market behavior and basic financial forecasting using machine learning.</p>

<p>The project includes Exploratory Data Analysis (EDA), feature engineering (e.g., lag variables), model training, and performance evaluation. A CLI tool was developed to simulate predictions using real input values.</p>

<h2>Variables</h2>
<p>Each feature is a factor that potentially influences the closing price. These include technical indicators typically used in financial analysis.</p>

<h3>Market Features (Independent Variables):</h3>
<ul>
  <li><strong>Open:</strong> Opening stock price of the day (Continuous)</li>
  <li><strong>High:</strong> Highest stock price recorded during the day (Continuous)</li>
  <li><strong>Low:</strong> Lowest stock price recorded during the day (Continuous)</li>
  <li><strong>Close:</strong> Closing stock price of the day (Continuous)</li>
  <li><strong>Volume:</strong> Number of shares traded during the day (Continuous)</li>
  <li><strong>Daily_Change_%:</strong> Percentage change from the previous day's close (Continuous)</li>
  <li><strong>Moving Averages:</strong> Rolling averages over 10, 30, or 50 days (Continuous)</li>
  <li><strong>Lag Feature:</strong> Previous day’s closing price (Continuous)</li>
</ul>

<h3>Target Variable:</h3>
<ul>
  <li><strong>Next_Close_Price:</strong> The predicted closing price of the next trading day (Continuous)</li>
</ul>

<h2>Machine Learning Models Used</h2>
<ul>
  <li>Linear Regression</li>
  <li>Support Vector Machine (SVR)</li>
  <li>Random Forest Regressor</li>
  <li>K-Nearest Neighbors (KNN)</li>
</ul>

<p>The models were trained using scikit-learn and evaluated using:</p>
<ul>
  <li>R² Score</li>
</ul>

<h2>Deployment (CLI Tool)</h2>
<p>A simple CLI interface was built using Python to allow users to:</p>
<ul>
  <li>Input the previous day's Open, High, Low, and Close prices</li>
  <li>Generate next-day closing price predictions using all four models</li>
  <li>Identify the best-performing model based on accuracy</li>
</ul>

<h2>Visualizations</h2>
<ul>
  <li>Time-series plot of closing prices</li>
  <li>Bar chart showing daily % change (gain/drop)</li>
  <li>Scatter plot comparing Open vs Close</li>
  <li>Model prediction performance plots (Actual vs Predicted)</li>
  <li>Correlation heatmap of features</li>
</ul>

<h2>Dataset Link</h2>
<p><a href="https://www.kaggle.com/datasets/camnugent/sandp500" target="_blank">https://www.kaggle.com/datasets/camnugent/sandp500</a></p>
