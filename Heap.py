class Heap:

    def __init__(self, S=None):
        self.node = S

    # heap minimum for frequences
    def heapMin(self, S, i):
        E = (2 * i) + 1
        D = (2 * i) + 2
        M = i

        if E <= len(S) and S[E].frequence < S[M].frequence:
            M = E
        if D <= len(S) and S[D].frequence < S[M].frequence:
            M = D

        if (M != i):
            aux = S[M]
            S[M] = S[i]
            S[i] = aux
            self.heapMin(S, M)

    def buildHeapMin(self, S):
        for i in range(len(S) // 2, 0, -1):
            self.heapMin(S, i)

    def returnHeapMinimum(self):
        self.buildHeapMin(self.node)
        return self.node
    #..............................................

    #construct down to up
    def heapUp(self, S, i):
        if i != 0 and S[i//2].frequence > S[i].frequence:
            aux = S[i//2]
            S[i//2] = S[i]
            S[i] = aux
            self.heapUp(S, i//2)

    def builHeapUp(self, S):
        print(len(S)-1)
        for i in range(len(S)-1, 0, -1):
            self.heapUp(S, i)

    def returnHeapUp(self):
        self.builHeapUp(self.node)
        return self.node
    #...............................................