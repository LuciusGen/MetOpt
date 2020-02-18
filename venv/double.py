#Строим двойственную задачу ЛП
#считаем, что задача уже сведена к каноническому виду, потому что см.п.1 на гите
from task import Task


class Double(Task):
   def __init__(self, Task):
       self.A = Task.A.transpose
       self.C = Task.B.transpose
       self.B = Task.C.transpose

   def __str__(self):
       Matr
       for i in range(len(self.A)):
           for j in range(len(self.A[i])):
               Matr[i].append(str(self.A[j]) + ' ');

           Matr[i].append('>= ' + str(self.B[i]) + '\n')

       for i in range(len(self.C)):
           Matr[len(self.A)].append(str(self.C) + 'X' + str(i + 1))

       Matr.append('-> max\n')

       return Matr
