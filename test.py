import cv2
import numpy as np


def frequencePixels(image, height, weight):
    frenquece = np.zeros((256,), dtype=int)

    for i in range(height):
        for j in range(weight):
            frenquece[image[i][j]] += 1

    return frenquece


#read the image
image = cv2.imread("re-elmayer.jpg")

scale = 60
w = int(image.shape[1]*scale / 100)
h = int(image.shape[0]*scale / 100)
d = (w, h)

resized = cv2.resize(image, d, interpolation=cv2.INTER_AREA)

(h_resized, w_resized, d_resized) = resized.shape
#print("width = {}, height = {}, depth = {}".format(wr, hr, dr))

image_copy = resized.copy()
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

#transform a matrix into an array
#image_copy = np.reshape(image_copy, (h_resized*w_resized))

print(frequencePixels(image_copy, h_resized, w_resized))

#display image
#cv2.imshow('imaged', resized)
cv2.waitKey(0)

