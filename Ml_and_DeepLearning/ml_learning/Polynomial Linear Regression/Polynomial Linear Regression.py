"""
Polynomial Linear Regression basics one topic of ML.
If we have unbalanced and non-linear PLR algorithm is the best of one.
--> Polynomial linear regression formula -> y = b0 + b1*x + b2*x^2 + ... + bn*x^n
--> It is calling Polynomial Linear Regression because the coefficient value type is polynomial. Coefficient  -> x^n
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Read csv file
df = pd.read_csv("polynomial+regression.csv", sep=";")

# Change data reshape for scikitlearn library
y = df.araba_max_hiz.values.reshape(-1, 1)
x = df.araba_fiyat.values.reshape(-1, 1)

plt.scatter(x, y)
plt.show()


polynomial_regression = PolynomialFeatures(degree=4)  # Degree == x^degree input -> x^2
x_polynomial = polynomial_regression.fit_transform(x)

linear_regression2 = LinearRegression()
linear_regression2.fit(x_polynomial, y)

y_head2 = linear_regression2.predict(x_polynomial)

plt.plot(x, y_head2, color='blue', label='Polynomial')
plt.legend()
plt.show()
