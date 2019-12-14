from Heap import Heap
from Node import Node
import numpy as np

class Huffman:

    def __init__(self, S):
        self.huff = S
        self.node = None
        self.heap = Heap()
        self.l = []

    #build Tree of heap Max
    def buildTree(self):
        while len(self.huff)-1 > 0:
            self.node = Node()

            P1 = self.heap.extract(self.huff)
            P2 = self.heap.extract(self.huff)

            if(P1.frequence > P2.frequence):
                self.node.left = P2
                self.node.right = P1
            else:
                self.node.left = P1
                self.node.right = P2

            self.node.frequence = P1.frequence + P2.frequence
            self.node.data = -1
            self.huff.append(self.node)
            self.heap.heapUp(self.huff, len(self.huff)-1)

        return self.heap.extract(self.huff)
    #.......................................................

    def returnHuff(self):
        return self.buildTree()

    #go through the tree, build the codification and add in a dictionary
    def goThroughTree(self, H, cod=''):
        if H.left == None and H.right == None:
            self.l.append((H.data, cod))
        else:
            self.goThroughTree(H.left, cod=cod + '0')
            self.goThroughTree(H.right, cod=cod + '1')
        d = dict(self.l)
        return d
    #....................................................

    def bitWiseOp(self, image, weight, height, dic):
        bitstring = ''
        for i in range(height):
            for j in range(weight):
                bitstring = bitstring + dic[image[i][j]]

        arr = ['0']*(len(bitstring)//8)
        index = 0
        bitcont = 0

        for i in range(len(bitstring)):
            op = int(arr[index], 2) << 1 | int(bitstring[i], 2)
            arr[index] = bin(op)
            bitcont += 1
            if (bitcont == 8):
                bitcont = 0
                index += 1

        return arr