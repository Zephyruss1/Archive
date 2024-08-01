import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# read csv file
df = pd.read_csv('linear_regression_dataset.csv', sep=';')
df.columns = ['deneyim', 'maas']

# y = b0 + b1 * x,
# b0 = constant(blas),
# b1 = coefficient
# x = features
# b1 = a / b, maas = b0 + b1 * deneyim

# residual = y - y_head
# if residual is negative then we get MSE = sum(residual^2) / n, n = sample count
plt.scatter(df.deneyim, df.maas)
plt.xlabel('deneyim')
plt.ylabel('maas')
plt.show()


linear_reg = LinearRegression()

x = df.deneyim.values.reshape(-1, 1)
y = df.maas.values.reshape(-1, 1)

# fit() -> fit the model according to the given training data
linear_reg.fit(x, y)

# predict() -> predict using the linear model
b0 = linear_reg.predict([[11]])
print('b0: ', b0)

b0_ = linear_reg.intercept_
print('intercept: ', b0_)

b1 = linear_reg.coef_
print('coef: ', b1)

# y = b0 + b1 * x -> maas = 1663 + 1138 * deneyim

maas_yeni = 1663 + 1138 * 11
print('maas_yeni: ', maas_yeni)

array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]).reshape(-1, 1)
plt.scatter(x, y)
plt.show()

y_head = linear_reg.predict(array)  # predicted salaries

plt.plot(array, y_head, color='red')
plt.show()
