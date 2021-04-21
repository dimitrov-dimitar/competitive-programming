import numpy as np
from matplotlib import pyplot as plt

data = np.array([
    [1, 1],
    [4, 2],
    [3, 1],
    [1, 2],
    [0, 2],
    [0, 1],
    [1, 0],
    [1, 3],
])
x, y = data.T
plt.scatter(x, y)
plt.show()
