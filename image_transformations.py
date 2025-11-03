# Choose a specific subject (eg. cat, dog, horse, tree, car, etc) and collect 10 random images from the internet (Dataset1).
# Perform different transformations

import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

source_dir = "/home/cse463"

image_files = []
for i in range(1, 11):
    filename = "img" + str(i) + ".jpeg"
    image_files.append(filename)

for filename in image_files:
    image_path = os.path.join(source_dir, filename)
    image = cv2.imread(image_path)

# Crop
    cropped_image = image[100:243, 100:277]

# Flip
    flipped = cv2.flip(image, 0)

# Rotate
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -90, 0.5)
    rotated = cv2.warpAffine(image, M, (cols, rows))

# Resize
    width = int(image.shape[1] * 0.5)
    height = int(image.shape[0] * 0.5)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# Translate / Shift
    shift_x = 50
    shift_y = 30
    translation_matrix = np.float32([[1, 0, shift_x],
                                     [0, 1, shift_y]])
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Shear
    shear_x = 0.5
    shear_y = 0.0
    shear_matrix = np.float32([[1, shear_x, 0],
                                [shear_y, 1, 0]])
    sheared_image = cv2.warpAffine(image, shear_matrix, (width + int(shear_x * height), height))

# Stretch
    height, width = image.shape[:2]
    stretch_x = 2
    stretch_y = 1.0
    stretch_matrix = np.float32([
                                [stretch_x, 0, 0],
                                [0, stretch_y, 0]])
    stretched_image = cv2.warpAffine(image, stretch_matrix, (int(width * stretch_x), int(height * stretch_y)))


    images = [
        image[..., ::-1],
        cropped_image[..., ::-1],
        flipped[..., ::-1],
        rotated[..., ::-1],
        resized_image[..., ::-1],
        translated_image[..., ::-1],
        sheared_image[..., ::-1],
        stretched_image[..., ::-1],
        ]

    titles = ['Original', 'Cropped', 'Flipped', 'Rotated', 'Resized', 'Translated', 'Sheared', 'Stretched']

    plt.figure(figsize=(25, 5))
    for i in range(8):
        plt.subplot(1, 8, i + 1)
        plt.imshow(images[i])
        plt.title(titles[i])

    plt.suptitle(f"Transformations on {filename}", fontsize=14)
    plt.show()
