from task import Task
import numpy as np
from  double import Double


A = np.array([[-1, 3, -5], [2, -1, 4], [3, 1, 1]])
B = np.array([12, 24, 18])
C = np.array([2, 1, 3])

a = Task(A, B, C)
#a.print()
ad = Double(a)
ad.print()