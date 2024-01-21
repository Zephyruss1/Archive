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
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('random+forest+regression+dataset.csv', sep=";", header=None)

x = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values.ravel()

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(x, y)

y_head = rf.predict(x)

from sklearn.metrics import r2_score

print("r_score: ", r2_score(y, y_head))
