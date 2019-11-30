from Heap import Heap
from Node import Node

class Huffman:

    def __init__(self):
        self.huff = []
        self.heap = Heap()
        self.node = Node()

    #heap maximum
    def heapMax(self, S, i):
        E = 2 * i
        D = (2 * i) + 1
        M = i

        if (E <= (len(S) - 1) and S[E] > S[M]):
            M = E
        if (D <= (len(S) - 1) and S[D] > S[M]):
            M = D

        if (M != i):
            aux = S[M]
            S[M] = S[i]
            S[i] = aux
            self.heapMax(S, M)

    def buildHeapMax(self, S):
        for i in range(len(S) // 2, 1, -1):
            self.heapMax(S, i)
    #.......................................

    # priority queue functions
    def extract(self, S):
        if (len(S) > 0):
            R = S[1]
            S[1] = S[len(S) - 1]
            S[len(S) - 1] = R
            del (S[len(S) - 1])
            self.heapMax(S, 1)
            return R
    #..........................................

    def constructHuffman(self):
        aux = self.heap.returnHeapMinimum()
        for i in range(len(aux)):
            p1 = self.extract(aux)
            p2 = self.extract(aux)
            add = p1.frequence + p2.frequence

            self.node.frequence = add
            self.node.data = -1

            if(p1 > p2):
                self.node.left = p2
                self.node.right = p1
            else:
                self.node.left = p1
                self.node.right = p2

            self.huff.append(self.node)
            self.heapMax(self.huff, 1)
    #.............................................

    def returnHuff(self):
        return self.huff
