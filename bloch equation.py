import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


def rotMatrix(angle):
    c = np.cos(np.radians(angle))
    s = np.sin(np.radians(angle))
    return np.array([[c, -s], [s, c]])


flag = 0


def data_gen(num):
    """Data generation"""

    global flag
    if num == 90 and flag == 0:
        flag = 1
    elif num == 180 and flag == 1:
        flag = 0

    z = num / 18

    if flag == 0 and not z == 10:
        ax.cla()
        ax.quiver(0, 0, 0, z, 0, (5 - z), pivot="tail", color="red")

    elif flag == 1 and not z == 10:
        z = z - 5
        v = np.array([0, (5 - z)])
        v30 = rotMatrix(num * 16).dot(v)
        ax.cla()
        ax.quiver(0, 0, 0, v30[0], v30[1], z, pivot="tail", color="red")

    ax.quiver(0, 0, 0, 0, 0, 5, pivot="tail", color="black",
              linestyle="dashed")

    ax.set_xlim3d([-5, 5])
    ax.set_xlabel('X')

    ax.set_ylim3d([-5, 5])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-5, 5])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data_gen(0)
ani = animation.FuncAnimation(fig, data_gen, 181, interval=1, blit=False)
# ani.save('animated_gif.gif', writer=animation.PillowWriter(fps=30))
plt.show()