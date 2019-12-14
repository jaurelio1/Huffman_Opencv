class Heap:

    def __init__(self, S=None):
        self.heapmin = []
        self.node = S

    #construct up to down
    def heapDown(self, S, i):
        E = i << 1
        D = i << 1 | 1
        M = i

        if E < len(S) and S[E].frequence < S[M].frequence:
            M = E
        if D < len(S) and S[D].frequence < S[M].frequence:
            M = D

        if (M != i):
            aux = S[i]
            S[i] = S[M]
            S[M] = aux
            self.heapDown(S, M)
    #..............................................

    # construct down to up
    def dad(self, i):
        return i >> 1

    def heapUp(self, S, i):
        if i != 0 and S[self.dad(i)].frequence > S[i].frequence:
            aux = S[i]
            S[i] = S[self.dad(i)]
            S[self.dad(i)] = aux
            self.heapUp(S, self.dad(i))

    # ...............................................

    #construct the heap minimum
    def buildHeapMin(self, S):
        for i in range(len(S)-1, -1, -1):
            self.heapmin.append(S[i])
            self.heapUp(S, len(self.heapmin)-1)

    def returnHeapMinimum(self):
        self.buildHeapMin(self.node)
        return self.node
    #..............................................

    #extract the element
    def extract(self, S):
        R = S[0]
        S[0] = S[len(S)-1]
        S[len(S)-1] = R
        S.pop(len(S)-1)
        self.heapDown(S, 0)
        return R
