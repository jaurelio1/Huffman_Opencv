import cv2
import numpy as np
from Heap import Heap
from Huffman import Huffman
from Node import Node

if __name__ == '__main__':
    #read the image
    image = cv2.imread("img1.tif")

    scale = 60
    w = int(image.shape[1]*scale / 100)
    h = int(image.shape[0]*scale / 100)
    d = (w, h)

    resized = cv2.resize(image, d, interpolation=cv2.INTER_AREA)

    (h_resized, w_resized, d_resized) = resized.shape

    image_copy = resized.copy()
    image_copy = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

    #first operations
    node = Node()
    node.setFrequencePixels(image_copy, h_resized, w_resized)
    tmp = node.returnArrayNode()

    #here we construct txhe heap minimum bottom_up
    heap = Heap(tmp)
    S = heap.returnHeapMinimum()

    #build the tree of heap Max
    huff = Huffman(S)
    R = huff.returnHuff()

    #build the dictionary
    D = huff.goThroughTree(R)
    #print(D)

    string = '10010111100011011001000111100110'
    print(len(string))
    arr = ['0']*((len(string)//8))
    print(arr)

    index = 0
    bitcont = 0

    for i in range(len(string)):
        op = int(arr[index], 2) << 1 | int(string[i], 2)
        arr[index] = bin(op)
        bitcont += 1
        if (bitcont == 8):
            bitcont = 0
            index += 1

    print(arr)

    #T = huff.bitWiseOp(image_copy, w_resized, h_resized, D)
    #print(T)

    #display image
    #cv2.imshow('imaged', resized)
    cv2.waitKey(0)