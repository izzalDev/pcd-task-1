import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from pcd_task_1 import convolve2d

image = Image.open("lena.jpg")
image = image.convert("L")  # grayscale
image = np.array(image)

# sobel
kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

edge_v = convolve2d(image, kernel)

plt.imshow(edge_v, cmap='gray')
plt.title('Vertical Edge')
plt.axis('off')
plt.show()
