class Heap:

    def __init__(self, S=None):
        self.node = S

    # heap minimum for frequences
    def heapMin(self, S, i):
        E = 2 * i
        D = (2 * i) + 1
        M = i

        if (E <= i and S[E] < S[M]):
            M = E
        if (D <= i and S[D] < S[M]):
            M = D

        if (M != i):
            aux = S[M]
            S[M] = S[i]
            S[i] = aux
            self.heapMin(S, M)

#Error 'list' object (S) has no attribute 'frequence'
    def buildHeapMin(self, S):
        for i in range(len(S) // 2, 0, -1):
            self.heapMin(S.frequence, i)
    #..............................................

    def returnHeapMinimum(self):
        heapmin = self.node
        self.buildHeapMin(heapmin)
        return heapmin