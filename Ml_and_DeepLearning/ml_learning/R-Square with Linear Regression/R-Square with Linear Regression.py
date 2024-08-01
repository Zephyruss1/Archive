"""
R-Square is measuring algorithm predictions is balanced.
Formula:
    SSR:

    residual = y - y_head
    square residual = (residual)^2
    sum square residual = sum((y-y_head)^2) -> SSR

    SST:
    y_avg = get average value from plots.
    sum square total = sum((y-y_avg)^2) -> SST

"""
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

y_head = linear_reg.predict(x)

plt.plot(x, y_head, color="red")

from sklearn.metrics import r2_score

print("r_score: ", r2_score(y, y_head))