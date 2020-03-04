from task import Task
import numpy as np
from itertools import combinations



def splitXkN(xkN):
    NkPlus = np.array(list(filter(lambda i: xkN[i] > 0, range(len(xkN)))))
    Nk0 = np.array(list(filter(lambda i: xkN[i] == 0, range(len(xkN)))))

    xkNPlus = np.array(list(filter(lambda i: i > 0, range(len(xkN)))))
    xkN0 = np.array(list(filter(lambda i: i == 0, range(len(xkN)))))

    return xkNPlus, NkPlus, xkN0, Nk0

#Метод искусственного базиса
def Basis(a: Task):
    A, B = a.A, a.B
    EMM = np.eye(len(B))

    ADop = np.concatenate((A, EMM), axis=1)
    cDop = np.concatenate((np.zeros(len(A[0]), np.ones())))

    tmp = Task(ADop, B, cDop)
    xStart = np.concatenate((np.zeros(len(A[0]))), B)
    #call simplex
    #xres and Nres
    #если найдено решение
    #x0N = xres[:len(A[0])]
    #_,NkPlus,_,_ = splitXkN(x0N)
    #if len(NkPlus) == len(B):
        #return x0N, NkPlus

def simplexK(a:Task, xkN):
    A, C = a.A, a.C
    _, NPlus, _, N0 = splitXkN(xkN)
    NList = combinations(list(range(len(N0))), len(len(B) - NPlus))

    for Nk in NList:
        Ak = np.array([A[:, i] for i in Nk]).T

        _, NkPlus, _, Nk0 = splitXkN(xkN)
        Lk = np.array(list(filter(lambda idx: idx not in Nk, Nk0))).astype(int)

        if np.linalg.det(AMNk) == 0:
            continue

        AInvk = np.linalg.inv(Ak)

        CNk = np.array([C[i] for i in Nk])
        ykM = np.matmul(AInvk.T, CNk)
        dkN = C - np.matmul(AMN.T, ykM)
        dkLk = np.array([dkN[int(i)] for i in Lk])

        if np.min(dkLk) >= 0:
            return xkN, Nk, True

        jk = Lk[list(filter(lambda j: dkLk[j] < 0, range(len(Lk))))[0]]
        ukNk = np.matmul(AInvk, A[:, jk])

        if np.max(ukNk) <= 0:
            return np.array(list(np.inf for _ in range(len(A[0])))), Nk, True

        _, NkPlus, _, Nk0 = splitXkN(xkN)

        if len(NkPlus) == len(Nk) \
                or max([ukNk[i] for i in filter(lambda j: Nk[j] not in NkPlus, range(len(Nk)))]) < 0:
            ukN = [ukNk[list(Nk).index(i)] if i in Nk else 0 for i in range(len(A[0]))]
            ukN[jk] = -1

            thetaK = min([xkN[i] / ukN[i] for i in filter(lambda j: ukN[j] > 0, Nk)])

            return xkN - np.multiply(thetaK, ukN), Nk, False

        return xkN, np.array([]), True