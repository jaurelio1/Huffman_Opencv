class Heap:

    def __init__(self, S=None):
        self.heapmin = []
        self.node = S

    # heap minimum for frequences
    def heapMin(self, S, i):
        E = (2 * i) + 1
        D = (2 * i) + 2
        M = i

        if E < len(S) and S[E].frequence < S[M].frequence:
            M = E
        if D < len(S) and S[D].frequence < S[M].frequence:
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
    def dad(self, i):
        return i//2

    def heapUp(self, S, i):
        if i != 0 and S[self.dad(i)].frequence > S[i].frequence:
            aux = S[self.dad(i)]
            S[self.dad(i)] = S[i]
            S[i] = aux
            self.heapUp(S, self.dad(i))

    def builHeapUp(self, S):
        for i in range(len(S)-1, -1, -1):
            self.heapmin.append(S[i])
            self.heapUp(self.heapmin, len(self.heapmin)-1)

    def returnHeapUp(self):
        self.builHeapUp(self.node)
        return self.heapmin
    #...............................................


    #extract the element
    def extract(self, S):
        R = S[0]
        S[0] = S[len(S)-1]
        S[len(S)-1] = R
        S.pop(len(S)-1)
        self.heapMin(S, 0)
        return R
