import numpy as np
import pandas as pd

# Importing data visualize library
import seaborn as sns
import matplotlib.pyplot as plt

# Importing machine learning library
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

df = pd.read_csv('data.csv')
df = df.drop(['Unnamed: 32', 'id'], axis=1, inplace=True)
df.diagnosis = [1 if each == "M" else 0 for each in df.diagnosis]

y = df.diagnosis.values
x_data = df.drop(["diagnosis"], axis=1)


# Check null data percentage
def print_percent_null(data):
    nan_percent = data.isna().sum() / len(data)
    return nan_percent.apply(lambda x: f"{x:.1%}")


x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

results = []

models = [
    LogisticRegression(),
    SVC(),
    GaussianNB(),
    RandomForestClassifier(),
    DecisionTreeClassifier(),

]
algorithms = [
    'LogisticRegression',
    'SVC',
    'GaussianNB',
    'RandomForestClassifier',
    'DecisionTreeClassifier',

]

for model, algorithm in zip(models, algorithms):
    model.fit(x_train, y_train)

    pred = model.predict(x_test)

    accuracy = accuracy_score(pred, y_test)

    results.append({'Algorithm': algorithm, 'Accuracy': accuracy})

report = pd.DataFrame(results)
report.sort_values('Accuracy', ascending=False)
