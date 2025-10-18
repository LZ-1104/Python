import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. 创建 p 和 q 的网格
p_vals = np.arange(0.01, 1.0, 0.02)
q_vals = np.arange(0.01, 1.0, 0.02)
P, Q = np.meshgrid(p_vals, q_vals) # 创建网格
#为什么要创建网格？因为我们需要计算每一对 (p, q) 对应的熵值 H(p, q)，

# 2. 计算 r = 1 - p - q
R = 1 - P - Q

# 3. 将无效区域（p+q >= 1）的熵设为 NaN
invalid_region = R <= 0 # 标记无效区域
R[invalid_region] = np.nan 
P[invalid_region] = np.nan
Q[invalid_region] = np.nan

# 4. 计算熵 H(p,q,r)
H = -(P * np.log2(P) + Q * np.log2(Q) + R * np.log2(R))

# 5. 绘制三维曲面
fig = plt.figure(figsize=(7, 7)) # 创建图形,设置大小,7x7英寸
ax = fig.add_subplot(111, projection='3d') # 创建3D坐标轴,111表示1行1列的第1个图,projection='3d'表示3D图形

surf = ax.plot_surface(P, Q, H, cmap='viridis', edgecolor='none') # 绘制曲面

# 6. 设置坐标轴标签和标题
ax.set_xlabel('p')
ax.set_ylabel('q')
ax.set_zlabel('H(p,q)')
ax.set_title('p-q-H(p,q)')
fig.colorbar(surf, shrink=0.5, aspect=10, label='H(p,q)')

ax.view_init(elev=30, azim=45) # 设置视角

plt.show()