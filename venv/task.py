#мы подразумеваем, что у нас каноническая задача
import numpy as np


class Task:
    def __init__(self, C, X, A, B):
        self.C = C
        self.A = A
        self.B = B

    def __str__(self):
        Matr = list()
        for i in range(len(self.A)):
            for j in range(len(self.A[i])):
                Matr.append(str(self.A[j]) + ' ');

            Matr.append('=' + str(self.B[i]) + '\n')

        for i in range(len(self.C)):
            Matr.append(str(self.C) + 'X' + str(i + 1))

        Matr.append('-> min')

        return Matr

    def getReverseA(self):
        return np.linalg.inv(A)

    def getRand(self):
        return np.linalg.matrix_rank(A)