"""
地球を半径 R [m] の凹凸の無い球体だと近似する。
R = 6378137.0 m, h = 1.6 m として、人から地平線までの距離 L を求める。
"""
import math
# 与えられた値
R = 6378137.0  # 地球の半径（メートル）
h = 1.6        # 目の高さ（メートル）

# 距離 L の計算
L = math.sqrt(2 * R * h + h ** 2)

# キロメートルに換算
L_km = L / 1000

print(f"目の高さが {h} m の人が地平線までの距離は {L_km} km です。")