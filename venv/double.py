#Строим двойственную задачу ЛП
#считаем, что задача уже сведена к каноническому виду, потому что см.п.1 на гите
from task import Task
from accessify import private


class Double(Task):
    @private
    def toCanoinan(self):
        for i in range(len(self.A)):
            for j in range(i):
                self.A[i].append(0)

            A[i].append(1)

            for j in range(len(A) - i - 1):
                self.A[i].append(0)

            C.append(0);

        for i in range(self.B):
            if B[i] < 0:
                A[i] *= -1
                B[i] *= -1


    def __init__(self, Task):
        self.A = Task.A.transpose
        self.C = Task.B.transpose
        self.B = Task.C.transpose