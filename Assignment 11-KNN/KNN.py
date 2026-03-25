from sklearn.neighbors import NearestNeighbors
import numpy as np

# Features: [Action, Comedy]
data = np.array([[5,1],[4,2],[1,5]])

model = NearestNeighbors(n_neighbors=2)
model.fit(data)

# New user preference
new_user = [[5,1]]

dist, ind = model.kneighbors(new_user)

print("Nearest Users Index:", ind)
print("Distances:", dist)