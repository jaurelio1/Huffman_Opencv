from Heap import Heap
from Node import Node

class Huffman:

    def __init__(self, S):
        self.huff = S
        self.node = None
        self.heap = Heap()

    #build Tree of heap Max
    def buildTree(self):
        for i in range(len(self.huff)-1):
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
            self.huff.insert(0, self.node)
            self.heap.heapUp(self.huff, len(self.huff)-1)


    def returnHuff(self):
        self.buildTree()
        return self.huff
