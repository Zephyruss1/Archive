"""
Confusion matrix clearly giving us chance to analysis data in advanced mode.
"""

import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
data.drop(["id", 'Unnamed: 32'], axis=1, inplace=True)


def print_null_percent(df):
    null_perc = df.isna().sum() / len(df)
    return null_perc.apply(lambda x: f"{x:.1%}")


print_null_percent(data)

data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(['diagnosis'], axis=1)

x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=42)

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()
dtc.fit(x_train, y_train)

print("Accuracy:", dtc.score(x_test, y_test))

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, random_state=1)
rf.fit(x_train, y_train)
print("Accuracy:", rf.score(x_test, y_test))

y_pred = rf.predict(x_test)
y_true = y_test

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_true, y_pred)

import seaborn as sns
import matplotlib.pyplot as plt

f, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(cm, annot=True, linewidths=0.5, linecolor='red', fmt='.0f', ax=ax)
plt.xlabel('y_pred')
plt.ylabel('y_true')
plt.show()
