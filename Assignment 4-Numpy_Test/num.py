import time, numpy as np

n = 1000000

t=time.time()
[x*2 for x in range(n)]
print("List:",time.time()-t)

t=time.time()
np.arange(n)*2
print("NumPy:",time.time()-t)