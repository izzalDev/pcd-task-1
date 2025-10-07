import numpy as np

def flip(kernel: np.ndarray) -> np.ndarray:
    m, n = kernel.shape

    if m % 2 == 0 or n % 2 == 0:
        raise ValueError("kernel size must be odd (e.g., 3x3, 5x5).")

    flipped = np.zeros_like(kernel)
    for i in range(m):
        for j in range(n):
            flipped[i, j] = kernel[m - 1 - i, n - 1 - j]
    return flipped


def correlate2d(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    Y, X = image.shape      # ukuran citra
    M, N = kernel.shape     # ukuran kernel

    if M % 2 == 0 or N % 2 == 0:
        raise ValueError("kernel size must be odd (e.g., 3x3, 5x5).")

    k = M // 2              # setengah tinggi kernel
    l = N // 2              # setengah lebar kernel

    R = np.zeros_like(image, dtype = float)

    # loop setiap posisi valid
    for x in range(k, Y - k):
        for y in range(l, X - l):
            sum = 0.0
            for i in range(-k, k + 1):
                for j in range(-l, l + 1):
                    sum += image[x + i, y + j] * kernel[i + k, j + l]
            R[x, y] = sum 

    return R

def convolve2d(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    return correlate2d(image, flip(kernel))


