#Строим двойственную задачу ЛП
#считаем, что задача уже сведена к каноническому виду, потому что см.п.1 на гите
from task import Task
from accessify import private
import numpy as np
#забыл про ограничение на знак для yi

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

        for i in range(len(self.B)):
            if self.B[i] < 0:
                self.A[i] *= -1
                self.B[i] *= -1

    def __init__(self, Task):
        self.A = np.transpose(Task.A)
        self.C = Task.B
        self.B = Task.C
        self.toCanoinan()