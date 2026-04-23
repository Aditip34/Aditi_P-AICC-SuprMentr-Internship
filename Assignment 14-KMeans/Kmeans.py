import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("mall.csv")

X = df[['Annual Income', 'Spending Score']]

kmeans = KMeans(n_clusters=4)
df['Cluster'] = kmeans.fit_predict(X)

print(df.groupby('Cluster').mean())