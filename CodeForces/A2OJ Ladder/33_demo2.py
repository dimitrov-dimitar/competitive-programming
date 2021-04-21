import numpy as np
from matplotlib import pyplot as plt

data = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
])
x, y = data.T
plt.scatter(x, y)
plt.show()
