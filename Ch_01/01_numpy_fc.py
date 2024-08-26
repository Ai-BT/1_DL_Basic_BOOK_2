# %%

import numpy as np

W1 = np.random.randn(2, 4)  # (2,4)
b = np.random.randn(4)  # (4,)
x = np.random.randn(10, 2)  # (10,2)
h = np.matmul(x, W1) + b  # 10,4

print(b.shape)
print(h.shape)

# %%

W1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  # (2,4)
b = np.array([1, 2, 3, 4])  # (4,) // 브로드캐스트로 다 더해짐
x = np.array([[1, 2],
              [3, 4],
              [5, 6],
              [7, 8],
              [9, 10],
              [11, 12],
              [13, 14],
              [15, 16],
              [17, 18],
              [19, 20]])  # (10,2)
h1 = np.matmul(x, W1) + b
h2 = np.matmul(x, W1)

print(h1)  # (4,)
print(h2)  # (10,4)
