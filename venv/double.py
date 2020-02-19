#Строим двойственную задачу ЛП
#считаем, что задача уже сведена к каноническому виду, потому что см.п.1 на гите
from task import Task
from accessify import private
import numpy as np

class Double(Task):
    @private
    def toCanoinan(self):
        Atmp = list(list())
        Ctmp = list()
        len0A = len(self.A)

        for i in range(len(self.A)):
            Atmp.append(list())
            for j in range(len(self.A[i])):
                Atmp[i].append(self.A[i][j])
                Atmp[i].append(-self.A[i][j])

        for i in range(len(self.C)):
            Ctmp.append(self.C[i])
            Ctmp.append(-self.C[i])

        self.A = Atmp
        self.C = Ctmp

        for i in range(len0A):
            for j in range(i):
                self.A[i].append(0)

            self.A[i].append(1)

            for j in range(len0A - i - 1):
                self.A[i].append(0)

            self.C.append(0);

        self.A = np.array(self.A)
        self.C = np.array(self.C)

        for i in range(len(self.B)):
            if self.B[i] < 0:
                self.A[i] = -1 * self.A[i]
                self.B[i] = -1 * self.B[i]

    def __init__(self, Task):
        self.A = np.transpose(Task.A)
        self.C = -Task.B
        self.B = Task.C
        self.toCanoinan()


#Восстановим решение задачи по решению двойственной
#воспользуемся второй теоремой двойственности

class Solve:
    def __init__(self, A, YOpt):
        self.Y = YOpt
        self.A = A

    def findOtherSolve(self):
        A = list(list())
        B = list()
        for i in range(len(self.A)):
            A.append(list())
            for j in range(len(self.A[i])):
                A[i].append(self.A[i][j] * self.Y[i])

            B.append(self.A[i][0] * self.Y[i])

        A = np.array(A)
        B = np.array(B)

        return np.linalg.solve(A, B)