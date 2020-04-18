from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftshift

fig = plt.figure()
ax = fig.add_subplot(111)

z = np.random.rand(100)
x = np.linspace(0, 100, len(z))

ax.set_xlabel('Z', fontsize=20)
ax.set_ylabel('Y', fontsize=20)
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.plot(x, z, label="Bz")
ax.legend(loc="upper left")
plt.show()

