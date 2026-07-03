import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the image in GRAYSCALE (so we deal with 1 channel first)
img = cv2.imread("images/faces.png", cv2.IMREAD_GRAYSCALE)
img_resized = cv2.resize(img, (640, 480))

# 2. Let's create that mask from your last lesson!
mask = np.zeros(img_resized.shape, dtype="uint8")
cv2.rectangle(mask, (100, 100), (560, 300), 255, -1)

# 3. Compute Histogram for the WHOLE image
hist_full = cv2.calcHist([img_resized], [0], None, [256], [0, 256])

# 4. Compute Histogram for JUST the masked region (the football faces box)
hist_masked = cv2.calcHist([img_resized], [0], mask, [256], [0, 256])

# --- DISPLAY THE RESULTS ---

# Show the images using matplotlib
plt.figure(figsize=(12, 5))

# Plot 1: The Histogram Chart
#Syntax: cv2.calcHist([images], [channels], mask, [histSize], [ranges])

plt.subplot(1, 2, 1)
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Brightness (0 - 255)")
plt.ylabel("Number of Pixels")
plt.plot(hist_full, color="black", label="Full Image")
plt.plot(hist_masked, color="red", label="Masked Region Only")
plt.xlim([0, 256])
plt.legend()

# Plot 2: Show the masked image so you can compare
masked_img = cv2.bitwise_and(img_resized, img_resized, mask=mask)
plt.subplot(1, 2, 2)
plt.title("What the Masked Histogram Sees")
plt.imshow(masked_img, cmap="gray")
plt.axis("off")

plt.show()