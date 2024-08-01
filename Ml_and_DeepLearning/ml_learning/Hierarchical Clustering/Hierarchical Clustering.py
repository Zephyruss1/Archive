"""
 Step:
   1) Choose each data point convert to cluster.
   2) Choose nearest two point convert to cluster.
   3) Choose nearest two cluster convert to one cluster.
   4) Repeat 3'rd step.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = np.random.normal(25, 5, 1000)
y1 = np.random.normal(25, 5, 1000)

x2 = np.random.normal(55, 5, 1000)
y2 = np.random.normal(35, 5, 1000)

x3 = np.random.normal(75, 5, 1000)
y3 = np.random.normal(80, 5, 1000)

x = np.concatenate((x1, x2, x3), axis=0)
y = np.concatenate((y1, y2, y3), axis=0)

dictionary = {'x': x, 'y': y}

df = pd.DataFrame(dictionary)

plt.scatter(x1, y1, color='black')
plt.scatter(x2, y2, color='black')
plt.scatter(x3, y3, color='black')
plt.show()

from scipy.cluster.hierarchy import dendrogram, linkage

merg = linkage(df, method='ward')

dendrogram(merg, leaf_rotation=90)
plt.xlabel('data points')
plt.ylabel('euclidean distance')
plt.show()

from sklearn.cluster import AgglomerativeClustering

hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
cluster = hc.fit_predict(df)

df['label'] = cluster

plt.scatter(df.x[df.label == 0], df.y[df.label == 0], color='red')
plt.scatter(df.x[df.label == 1], df.y[df.label == 1], color='green')
plt.scatter(df.x[df.label == 2], df.y[df.label == 2], color='blue')