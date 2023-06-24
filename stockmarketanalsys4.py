# -*- coding: utf-8 -*-
"""StockMarketAnalsys4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EiSCjKwIXHsBE9iB9jQ5xawzU157OH2q
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
plt.style.use('seaborn-darkgrid')

df = pd.read_csv('ADANIENT.NS.csv')

df.head(50)

df.info()

df.describe()

df.shape

"""**EDA**


"""

plt.figure(figsize=(20,10))
plt.title('ADANIPORTS STOCK PRICES',fontsize=24,style='italic',fontweight='bold',color='#1AA260')
plt.xlabel('Days', fontsize=20,style='italic',fontweight='bold',color='#56A5EC')
plt.ylabel('Opening Price USD ($)',style='italic',fontweight='bold', fontsize=20,color='#FAF0DD')
plt.plot(df['Open'])
plt.style.use('dark_background')
plt.rc('lines', markersize=4)
plt.show()

plt.figure(figsize=(20,10))
plt.title('ADANIPORTS STOCK PRICES', fontsize=24,style='italic',fontweight='bold',color='#6F2DA8')
plt.xlabel('Days',fontsize=20,style='italic',fontweight='bold',color='#660000')
plt.ylabel('High Price USD ($)',style='italic',fontweight='bold', fontsize=20,color='#7F4E52')
plt.plot(df['High'])
plt.style.use('dark_background')
plt.rc('lines', markersize=4)
plt.show()

plt.figure(figsize=(20,10))
plt.title('ADANIPORTS STOCK PRICES', fontsize=24,style='italic',fontweight='bold',color='#1589FF')
plt.xlabel('Days',fontsize=20,style='italic',fontweight='bold',color='#1AA260')
plt.ylabel('Low Price USD ($)',style='italic',fontweight='bold', fontsize=20,color='#C34A2C')
plt.plot(df['Low'])
plt.style.use('dark_background')
plt.rc('lines', markersize=4)
plt.show()

plt.figure(figsize=(20,10))
plt.title('ADANIPORTS STOCK PRICES', fontsize=24,style='italic',fontweight='bold',color='#FF6347')
plt.xlabel('Days',fontsize=20,style='italic',fontweight='bold',color='#B38481')
plt.ylabel('Closing Price USD ($)',style='italic',fontweight='bold', fontsize=20,color='#DC143C')
plt.plot(df['Close'])
plt.style.use('dark_background')
plt.rc('lines', markersize=4)
plt.show()

ma_day = [10, 20, 50]

for ma in ma_day:
    for company in df:
        column_name = f"MA for {ma} days"
        df[column_name] = df['Close'].rolling(ma).mean()

fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_figheight(10)
fig.set_figwidth(15)
df[[ 'Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot(ax=axes[0,0])
axes[0,0].set_title('Adani')
plt.style.use('dark_background')
plt.rc('lines', markersize=4)

"""**Dataframe with respec to Closing Stock**"""

df2 = df['Close']

df2.tail(50)

df2 = pd.DataFrame(df2)

df2.tail(50)

future_days = 40
df2['Prediction'] = df2['Close'].shift(-future_days)

df2.tail(50)

X = np.array(df2.drop(['Prediction'], 1))[:-future_days]
print(X)

y = np.array(df2['Prediction'])[:-future_days]
print(y)

"""**Linear and Decision Tree** **Regression**

"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

tree = DecisionTreeRegressor().fit(x_train, y_train)
lr = LinearRegression().fit(x_train, y_train)

x_future = df2.drop(['Prediction'], 1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)
x_future

tree_prediction = tree.predict(x_future)
print(tree_prediction)

lr_prediction = lr.predict(x_future)
print(lr_prediction)

predictions = tree_prediction
valid = df2[X.shape[0]:]
valid['Predictions'] = predictions

plt.figure(figsize=(20,10))
plt.title('ADANIPORTS STOCK PRICES',fontsize=24,style='italic',fontweight='bold',color='#6C2DC7')
plt.xlabel('Days',fontsize=20,style='italic',fontweight='bold',color='#FFB8BF')
plt.ylabel('Close Price USD ($)',style='italic',fontweight='bold', fontsize=20,color='#FFF9E3')
plt.plot(df2['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(["Original", "Valid", 'Predicted'])
plt.style.use('dark_background')
plt.rc('lines', markersize=4)
plt.show()

fig, ax = plt.subplots()
df2.plot(x='Close', y=['Prediction'], kind='bar',color='#5865F2', ax=ax)
plt.title('Comparison Predicted vs Actual Price in Sample data selection',
      fontsize=24.,style='italic',fontweight='bold',color='#848B79')
plt.xlabel('Close',fontsize=20,style='italic',fontweight='bold',color='#6AFB92')
plt.ylabel('Prediction', fontsize=14,style='italic',fontweight='bold',color='#FFDEAD')
plt.show()

"""overfiting"""

tree.score(x_train, y_train),tree.score(x_future,tree_prediction)

"""**Dataframe with Respect to High price Stock**"""

df3 = df['High']

df3.tail(50)

df3 = pd.DataFrame(df3)

df3.tail(50)

future_days = 40
df3['Prediction'] = df3['High'].shift(-future_days)

df3.tail(50)

A = np.array(df3.drop(['Prediction'], 1))[:-future_days]
print(X)

y = np.array(df3['Prediction'])[:-future_days]
print(y)

"""**Linear and Decision Tree Regression**"""

from sklearn.model_selection import train_test_split
x1_train, x1_test, y1_train, y1_test = train_test_split(X, y, test_size = 0.2)

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

tree1 = DecisionTreeRegressor().fit(x_train, y_train)
lr1 = LinearRegression().fit(x_train, y_train)

x1_future = df3.drop(['Prediction'], 1)[:-future_days]
x1_future = x1_future.tail(future_days)
x1_future = np.array(x_future)
x1_future

tree1_prediction = tree.predict(x1_future)
print(tree1_prediction)

lr1_prediction = lr.predict(x1_future)
print(lr1_prediction)

predictions = tree1_prediction
valid = df3[X.shape[0]:]
valid['Predictions'] = predictions

plt.figure(figsize=(20,10))
plt.title('ADANIPORTS STOCK PRICES',fontsize=24,style='italic',fontweight='bold',color='#D2691E')
plt.xlabel('Days',fontsize=20,style='italic',fontweight='bold',color='#665D1E')
plt.ylabel('High Price USD ($)',fontsize=20,style='italic',fontweight='bold',color='#FFA600')
plt.plot(df3['High'])
plt.plot(valid[['High', 'Predictions']])
plt.legend(["Original", "Valid", 'Predicted'])
plt.style.use('dark_background')
plt.rc('lines', markersize=4)
plt.show()

fig, ax = plt.subplots()
df3.plot(x='High', y=['Prediction'], kind='bar',color='#5865F2', ax=ax)
plt.title('Comparison Predicted vs Actual Price in Sample data selection',
      fontsize=24.,style='italic',fontweight='bold',color='#848B79')
plt.xlabel('High',fontsize=20,style='italic',fontweight='bold',color='#6AFB92')
plt.ylabel('Prediction', fontsize=14,style='italic',fontweight='bold',color='#FFDEAD')
plt.show()