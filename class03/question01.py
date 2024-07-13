import numpy as np

# 係数行列
A = np.array([
    [2, -1, 3],
    [7, -4, -1],
    [-1, 1, 2]
])

# 定数ベクトル
B = np.array([-2, 2, 0])

# 連立方程式の解
X = np.linalg.solve(A, B)

print("連立方程式の解:")
print(f"x = {X[0]:.2f}, y = {X[1]:.2f}, z = {X[2]:.2f}")
