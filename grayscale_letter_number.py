# Create your own grayscale letters and numbers!
# Use a numpy array to create a grayscale image of this code. 

import matplotlib.pyplot as plt

Letter_H = np.array([
    [0, 255, 0],
    [0, 255, 0],
    [0,   0, 0],
    [0, 255, 0],
    [0, 255, 0]
])

Letter_R = np.array([
    [0,   0, 255],
    [0, 255,   0],
    [0,   0, 255],
    [0, 255,   0],
    [0, 255,   0]
])

Digit_Two = np.array([
    [255,   0, 255],
    [0,   255,   0],
    [255,   0, 255],
    [0, 255,   255],
    [0,     0,   0]
])

Digit_Three = np.array([
    [0,   0, 255],
    [255, 255,   0],
    [255,   0, 255],
    [255, 255,   0],
    [0,   0, 255]
])

Space = np.array([
    [255],
    [255],
    [255],
    [255],
    [255],
])

Code = np.hstack((Space, Letter_H, Space, Letter_R, Space, Digit_Two, Space, Digit_Three, Space))

plt.imshow(Code, cmap='gray')
plt.title("Grayscale Image of Code: HR23")
plt.show()