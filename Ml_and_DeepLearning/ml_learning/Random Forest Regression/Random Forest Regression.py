"""
Random Forest Regression is family member of Ensemble Learning using all ML algorithms to find average prediction.
Firstly we need have a data and after to use Random Forest Regression need select n sample from data.
N sample data -> is calling sub data this sub data have n number of trees after all algorithms processing
average result.
Basically using recommended systems. EX: Film sites, predict stocks...
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('random+forest+regression+dataset.csv', sep=";", header=None)

x = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values.ravel()

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(x, y)

print(rf.predict([[7.5]]))

x_ = np.arange(min(x), max(x), 0.01).reshape(-1, 1)
y_head = rf.predict(x_)

plt.scatter(x, y, color="red")
plt.plot(x_, y_head, color="green")
plt.xlabel("Tribune level")
plt.ylabel("Price")
plt.show()
