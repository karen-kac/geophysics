"""
Python を利用して、numpy や math を使って、ベクトル a = (1, 3) を反時計回りに80度回転させたベクトルを求める。
"""
# import numpy as np
# # ベクトル a
# a = np.array([1, 3])

# # 回転角度（ラジアン）
# theta = np.deg2rad(80)

# # 回転行列
# rotation_matrix = np.array([
#     [np.cos(theta), -np.sin(theta)],
#     [np.sin(theta), np.cos(theta)]
# ])

# # 回転後のベクトル
# a_rotated = np.dot(rotation_matrix, a)

# print(f"回転後のベクトル: {a_rotated}")

import numpy as np
import math
# ベクトルa
a = np.array([1, 3])

# 回転角度（度数法からラジアンに変換）
theta = math.radians(80)

# 回転行列
R = np.array([[math.cos(theta), -math.sin(theta)],
            [math.sin(theta), math.cos(theta)]])

# 回転後のベクトル
b = R.dot(a)
#b = R@a
print(f"回転後のベクトル: {b}")