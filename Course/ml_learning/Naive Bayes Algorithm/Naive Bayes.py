"""
Imagine there is given data contain 0 and 1's.
Naive Bayes Algorithm basically doing predict X data is from 0 or 1. (0 and 1 is data name variable this algorithm not working only binary datasets.)
Algorithm Formula:
    P -> Probability
    zero -> Our data example
    X -> Data we want to detect who it from ? (0 or 1)
    | -> Probability of given X

                            -> likelihood: How many total zero data in the observation / length(zero)
            P(zero|X) = P(X|zero) * P(zero)         -> prior probability: (X / length(Data point))
            ------------------------------
                        P(X)            -> marginal likelihood (Similarity range): (How many total data is in the observation
                                            (Similarity range) we determined / length(Data point))
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
data = pd.read_csv("data.csv")

# %%
data.drop(["id", "Unnamed: 32"], axis=1, inplace=True)
data.tail()
# malignant = M  kotu huylu tumor
# benign = B     iyi huylu tumor

# %%
M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]
# scatter plot
plt.scatter(M.radius_mean, M.texture_mean, color="red", label="kotu", alpha=0.3)
plt.scatter(B.radius_mean, B.texture_mean, color="green", label="iyi", alpha=0.3)
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.legend()
plt.show()

# %%
data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis=1)

# %%
# normalization
x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))

# %%
# train test split
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
# %%

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
nb.fit(x_train, y_train)

print("Accuracy:", nb.score(x_test, y_test))
