import numpy as np
from sklearn.feature_extraction import image
from sklearn.datasets import load_sample_image
from skimage import io
from skimage.feature import canny
from skimage import filters
from skimage import exposure
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage import segmentation
from skimage.color import label2rgb
from scipy import ndimage as ndi

wood = io.imread('Desktop/wood.jpg')
woodArray=np.asarray(wood)
grayscale = rgb2gray(woodArray)
print(woodArray.shape)

val = filters.threshold_otsu(grayscale)
hist, bins_center = exposure.histogram(grayscale)

elevation = sobel(grayscale)
markers = np.zeros_like(grayscale)
markers[grayscale < val] = 1
markers[grayscale > val] = 2
segmentation= segmentation.watershed(elevation, markers)

segmentation = ndi.binary_fill_holes(segmentation - 1)
labeled, _ = ndi.label(segmentation)
image_label_overlay = label2rgb(labeled, image=grayscale < (val), bg_label=0)

fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
axes[0].imshow(grayscale, cmap=plt.cm.gray)
axes[0].contour(segmentation, [0.5], linewidths=0.2, colors='y')
axes[1].imshow(image_label_overlay)

for a in axes:
    a.axis('off')

plt.tight_layout()

plt.show()


plt.figure(figsize=(9, 4))
plt.subplot(141)
plt.imshow(grayscale , cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(142)
plt.imshow(grayscale < (val), cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(143)
plt.imshow(grayscale > (val), cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(144)
plt.plot(bins_center, hist, lw=2)
plt.axvline(val, color='k', ls='--')

plt.tight_layout()
plt.show()
