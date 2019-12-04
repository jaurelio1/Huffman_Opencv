import numpy as np


class Node:
    frequences = np.zeros((256,), dtype=int)

    def __init__(self, data=None, frequence=None, r=None, l=None, heap=[]):
        self.H = heap
        self.data = data
        self.right = r
        self.left = l
        self.frequence = frequence

    # show the frequence of the pixels in the image

    def setFrequencePixels(self, image, height, weight):
        for i in range(height):
            for j in range(weight):
                self.frequences[image[i][j]] += 1

    # ..........................................

    # store the nodes in an array
    def storeNode(self):
        for i in range(256):
            #..................data, frequence of pixel
            self.H.append(Node(i, self.frequences[i]))
    # .............................................

    def returnArrayNode(self):
        self.storeNode()
        return self.H