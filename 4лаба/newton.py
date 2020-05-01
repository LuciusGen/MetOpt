from math import cos, sin, sqrt
import numpy as np
from grad1 import func_grad, func


def hesse_coef(x1, x2):
    F_1_1 = -36 * cos(6 * x1 + x2) + 8
    F_1_2 = -6 * cos(6 * x1 + x2)
    F_2_1 = -6 * cos(6 * x1 + x2)
    F_2_2 = 2 - cos(6 * x1 + x2)
    return F_1_1, F_1_2, F_2_1, F_2_2


def det(F_1_1, F_1_2, F_2_1, F_2_2):
    return F_1_1 * F_2_2 - F_2_1 * F_1_2


def newton(x_start:np.array = np.array([0.0, 0.0])):
    x1 = x_start[0]
    x2 = x_start[1]
    res = [x_start]
    eps = 0.01
    F_1, F_2 = func_grad([x1, x2])
    while pow(F_2, 2)+pow(F_1, 2) > pow(eps, 2):
        F_1_1, F_1_2, F_2_1, F_2_2 = hesse_coef(x1, x2)
        detH = det(F_1_1, F_1_2, F_2_1, F_2_2)

        F_1, F_2 = func_grad([x1, x2])

        x1 = x1 - 1/detH*(F_2_2 * F_1-F_2_1 * F_2)
        x2 = x2 - 1/detH*(F_1_1 * F_2 - F_1_2 * F_1)
        res.append(np.array([x1, x2]))

    print("x1 = ", x1, "x2 = ", x2, "f(x1,x2) =", func([x1,x2]))
    return res


res = newton()
print(len(res))