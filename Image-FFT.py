import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['font.size'] = 8.0
np.random.seed(19680801)

img = cv2.imread('p2.jpg', 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
y1 = np.abs(f) / len(f)
x = np.linspace(0, 100, int(len(y1)))

magnitude_spectrum = 20 * np.log(np.abs(fshift))
phase = np.angle(fshift)

images = []

fig, axs = plt.subplots(2, 2)
for i in range(2):
    for j in range(2):
        axs[i, j].set_yticklabels([])
        axs[i, j].set_xticklabels([])

fig.suptitle('FFT Components')
data = [img, magnitude_spectrum, phase]

images.append(axs[0, 0].imshow(data[0], cmap='gray'))
axs[0, 0].set_title('Input Image')

images.append(axs[1, 0].imshow(data[1], cmap='gray'))
axs[1, 0].set_title('Magnitude Spectrum')

images.append(axs[1, 1].imshow(data[2], cmap='gray'))
axs[1, 1].set_title('Phase Spectrum')

axs[0, 1].plot(x, y1)
axs[0, 1].set_title('FFT')

plt.show()

# plt.figure(4)
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.subplot(),plt.imshow(phase, cmap = 'gray')
# plt.title('Phase'), plt.xticks([]), plt.yticks([])
# plt.show()

###############################################################
