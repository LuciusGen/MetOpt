#мы подразумеваем, что у нас каноническая задача
import numpy as np


class Task:
    def __init__(self, C, X, A, B):
        self.C = C
        self.A = A
        self.B = B

    def __str__(self):
        Matr
        for i in range(len(self.A)):
            for j in range(len(self.A[i])):
                Matr[i].append(str(self.A[j]) + ' ');

            Matr[i].append('= ' + str(self.B[i]) + '\n')

        for i in range(len(self.C)):
            Matr[len(self.A)].append(str(self.C) + 'X' + str(i + 1))

        Matr.append('-> min\n')

        for i in range(len(self.C)):
            Matr[len(self.A + 1].append('X' + str(i + 1) + '> 0 ')

        return Matr

    def getReverseA(self):
        return np.linalg.inv(A)

    def getRand(self):
        return np.linalg.matrix_rank(A)