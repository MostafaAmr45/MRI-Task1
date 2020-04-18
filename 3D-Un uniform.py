from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100
xs = np.linspace(0, n, n)
ys = np.linspace(0, 0, n)
zs = np.random.rand(100)

ax.plot3D(xs, ys, zs, 'red', label="Bz")
ax.set_xlabel('Z', fontsize=20)
ax.set_ylabel('X', fontsize=20)
ax.set_zlabel('Y', fontsize=20)
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_zticklabels([])
ax.legend(loc="upper left")
plt.show()
