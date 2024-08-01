import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data
df = pd.read_csv('multiple_linear_regression_dataset.csv', sep=';')
df.columns = ['deneyim', 'maas', 'yas']

# Multiple LR -> y= b0 + b1*x1 + b2*x2 + ... + bn*xn

x = df.iloc[:, [0, 2]].values
y = df.maas.values.reshape(-1, 1)

multiple_linear_regression = LinearRegression()
multiple_linear_regression.fit(x, y)

print("b0:", multiple_linear_regression.intercept_)
print("b1, b2:", multiple_linear_regression.coef_)

input_data = np.array([[10, 35], [5, 35]])

mlr_predict = multiple_linear_regression.predict(input_data)
print("mlr_predict: ", mlr_predict)
plt.plot(mlr_predict)
plt.show()

