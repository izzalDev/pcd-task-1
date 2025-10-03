from __future__ import annotations
from pcd_task_1.kernel import Kernel
import numpy as np
from typing import Any


class Image:
    def __init__(self, arr: Any):
        a = np.asarray(arr)
        if a.ndim not in (2, 3):
            raise ValueError("Image data must be a 2D (H,W) or 3D (H,W,C) array")
        self._data = a.astype(np.float64, copy=False)

    @property
    def array(self) -> np.ndarray:
        return self._data

    def copy(self) -> "Image":
        return Image(self._data.copy())

    def _extract_kernel(self, kernel: Kernel) -> np.ndarray:
        if isinstance(kernel, np.ndarray):
            k = kernel
        else:
            for attr in ("array", "kernel", "matrix", "data"):
                if hasattr(kernel, attr):
                    k = getattr(kernel, attr)
                    break
            else:
                raise AttributeError(
                    "Kernel must be a numpy array or have attribute 'array'/'kernel'/'matrix'/'data'"
                )
        k = np.asarray(k, dtype=np.float64)
        if k.ndim != 2:
            raise ValueError("Kernel must be a 2D array")
        return k

    def _pad_for_kernel(self, img2d: np.ndarray, kshape: tuple[int, int]) -> np.ndarray:
        kh, kw = kshape
        pad_h = kh // 2
        pad_w = kw // 2
        return np.pad(img2d, ((pad_h, kh - pad_h - 1), (pad_w, kw - pad_w - 1)), mode="constant", constant_values=0)

    def corelate2D(self, kernel: Kernel) -> "Image":
        k = self._extract_kernel(kernel)
        kh, kw = k.shape

        data = self._data
        if data.ndim == 2:
            out = self._correlate2d_single(data, k)
        else:
            channels = []
            for c in range(data.shape[2]):
                channels.append(self._correlate2d_single(data[:, :, c], k))
            out = np.stack(channels, axis=2)

        return Image(out)

    def convolve2D(self, kernel: Kernel) -> "Image":
        k = self._extract_kernel(kernel)
        k_flipped = np.flip(np.flip(k, axis=0), axis=1)
        return self.corelate2D(k_flipped)

    def _correlate2d_single(self, img2d: np.ndarray, k: np.ndarray) -> np.ndarray:
        h, w = img2d.shape
        kh, kw = k.shape
        padded = self._pad_for_kernel(img2d, (kh, kw))
        out = np.zeros((h, w), dtype=np.float64)

        for i in range(h):
            for j in range(w):
                window = padded[i : i + kh, j : j + kw]
                out[i, j] = np.sum(window * k)
        return out

    def to_uint8(self, clip: bool = True) -> np.ndarray:
        a = self._data
        if clip:
            a = np.clip(a, 0, 255)
        return a.astype(np.uint8)

    def __repr__(self) -> str:
        return f"Image(shape={self._data.shape}, dtype={self._data.dtype})"
