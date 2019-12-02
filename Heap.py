class Heap:

    def __init__(self, S=None):
        self.node = S

    # heap minimum for frequences
    def heapMin(self, S, i):
        if(i == 0):
            E = 1
            D = 2
            M = 0
        else:
            E = 2 * i
            D = (2 * i) + 1
            M = i

        if (E <= i and S[E].frequence < S[M].frequence):
            M = E
        if (D <= i and S[D].frequence < S[M].frequence):
            M = D

        if (M != i):
            aux = S[M]
            S[M] = S[i]
            S[i] = aux
            self.heapMin(S, M)

    def buildHeapMin(self, S):
        for i in range(len(S) // 2, 0, -1):
            self.heapMin(S, i)
    #..............................................

    def returnHeapMinimum(self):
        heapmin = self.node
        self.buildHeapMin(heapmin)
        return heapmin
