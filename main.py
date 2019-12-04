import cv2
from Heap import Heap
from Huffman import Huffman
from Node import Node

if __name__ == '__main__':
    #read the image
    image = cv2.imread("re-elmayer.jpg")

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

    #here we construct the heap minimum bottom_up
    heap = Heap(tmp)
    S = heap.returnHeapUp()


    #display image
    #cv2.imshow('imaged', resized)
    cv2.waitKey(0)