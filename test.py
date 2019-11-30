import cv2
import numpy as np

#construction of the node for the priority queue
class Node:
    def __init__(self, data, frequence, R, L):
        self.data = data
        self.frenquence = frequence
        self.right = R
        self.left = L


#show the frequence of the pixels in the image
def frequencePixels(image, height, weight):
    frenquece = np.zeros((256,), dtype=int)

    for i in range(height):
        for j in range(weight):
            frenquece[image[i][j]] += 1

    return frenquece
#..........................................

#functions of construction of heaps
#heap minimum for frequences
def heapMin(S, i):
    E = 2*i
    D = (2*i) + 1
    M = i

    if(E <= (len(S)-1) and S[E] < S[M]):
        M = E
    if(D <= (len(S)-1) and S[D] < S[M]):
        M = D

    if(M != i):
        aux = S[M]
        S[M] = S[i]
        S[i] = aux
        heapMin(S, M)

def builHeapMin(S):
    for i in range(len(S)//2, 1, -1):
        heapMin(S, i)
#and heap maximum for Huffman coding
def heapMax(S, i):
    E = 2*i
    D = (2*i) + 1
    M = i

    if(E <= (len(S)-1) and S[E] > S[M]):
        M = E
    if(D <= (len(S)-1) and S[D] > S[M]):
        M = D

    if(M != i):
        aux = S[M]
        S[M] = S[i]
        S[i] = aux
        heapMin(S, M)

def buildHeapMax(S):
    for i in range(len(S)//2, 1, -1):
        heapMin(S, i)
#................................................

#functions of construction of priority queue


#................................................

#main
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

#array with frequence of pixels
array_pixels = frequencePixels(image_copy, h_resized, w_resized)
cpy_pixels = array_pixels.copy()

builHeapMin(cpy_pixels)

print(cpy_pixels)

#display image
#cv2.imshow('imaged', resized)
cv2.waitKey(0)

