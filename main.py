import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node
import zipfile

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

    #codification of the picture
    T, index = huff.compressOp(image_copy, w_resized, h_resized, D)

    #writing the codification in a file
    file = open('test.txt', 'w')
    for i in range(index):
        file.write(str(T[i])+' ')

    file1 = open('test.txt', 'r')

    #result of the decompress
    dc = huff.decompressOp(file1, R)
    print(dc)

    file.close()
    file1.close()


    #display image
    #cv2.imshow('imaged', resized)
    cv2.waitKey(0)