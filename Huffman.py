from Heap import Heap
from Node import Node
import numpy as np

class Huffman:

    def __init__(self, S):
        self.huff = S
        self.node = None
        self.heap = Heap()
        self.l = []
        self.cont = 0

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
    #this method build the code of each pixel
    def goThroughTree(self, H, cod=''):
        if H.left == None and H.right == None:
            self.l.append((H.data, cod))
        else:
            self.goThroughTree(H.left, cod=cod + '0')
            self.goThroughTree(H.right, cod=cod + '1')
        d = dict(self.l)
        return d
    #....................................................

    def compressOp(self, image, weight, height, dic):
        bitstring = ''
        for i in range(height):
            for j in range(weight):
                bitstring = bitstring + dic[image[i][j]]

        arr = [0]*((len(bitstring)//8)+1)
        index = 0
        bitcont = 0

        for i in range(len(bitstring)):
            arr[index] = int(arr[index]) << 1 | int(bitstring[i])
            bitcont += 1
            if (bitcont == 8):
                bitcont = 0
                index += 1

        return arr, index

    #............................................


    #operations to decompress
    def returnValue(self, H, value):
        t = value[self.cont]
        if(H.left == None and H.right == None):
            self.cont = 0
            return H.data
        else:
            if(value[self.cont]== '0'):
                self.cont += 1
                self.returnValue(H.left, value)
            else:
                self.cont += 1
                self.returnValue(H.right, value)

    def decompressOp(self, file, H):
        l = []
        value = ''
        filedata = file.readline()
        for i in filedata:
            if i != ' ':
                value = value + i
                continue
            a = self.returnValue(H, bin(int(value)))
            l.append(a)
            value = ''
        return l