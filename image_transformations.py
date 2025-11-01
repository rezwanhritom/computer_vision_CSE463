# Choose a specific subject (eg. cat, dog, horse, tree, car, etc) and collect 10 random images from the internet (Dataset1).
# Perform 5 different transformations

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
    shear_matrix = np.float32([
        [1, shear_x, 0],
        [shear_y, 1, 0]
    ])
    sheared_image = cv2.warpAffine(image, shear_matrix, (width + int(shear_x * height), height))

    images = [
        image[..., ::-1],
        flipped[..., ::-1],
        rotated[..., ::-1],
        resized_image[..., ::-1],
        translated_image[..., ::-1],
        sheared_image[..., ::-1]
        ]

    titles = ['Original', 'Flipped', 'Rotated', 'Resized', 'Translated', 'Sheared']

    plt.figure(figsize=(15, 5))
    for i in range(6):
        plt.subplot(1, 6, i + 1)
        plt.imshow(images[i])
        plt.title(titles[i])

    plt.suptitle(f"Transformations on {filename}", fontsize=14)
    plt.show()
