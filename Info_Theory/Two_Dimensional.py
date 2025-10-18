import matplotlib.pyplot as plt
import numpy as np

p = np.linspace(0, 1, 100)
q = 1-p
Hx = -p * np.log2(p + 1e-10) - q * np.log2(q + 1e-10)#计算熵,

plt.figure(figsize=(6,4))
plt.plot(p, Hx, label='H(x)')
plt.scatter(p[::10], Hx[::10], color='red')
plt.title('H(x)')
plt.xlabel('p')
plt.ylabel('Hx')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()