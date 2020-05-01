import math
import matplotlib.pyplot as plt
from numpy import arange, log


def golden_section(a, b, f, eps):
    t = arange(a, b, 0.01)
    fi = 0.382

    # Вычисляем значения функций f(x_1), f(x_2)
    x_1 = a + 0.382 * (b - a)
    x_2 = b - 0.382 * (b - a)
    f_x_1 = f(x_1)
    f_x_2 = f(x_2)

    k = 2
    while True:
        if f_x_1 < f_x_2:
            b = x_2
        else:
            a = x_1

        if math.fabs(b - a) < eps:
            return abs(b - a)/2
        else:
            if b == x_2:
                x_2 = x_1
                f_x_2 = f_x_1
                x_1 = a + fi * (b - a)
                f_x_1 = f(x_1)
            if a == x_1:
                x_1 = x_2
                f_x_1 = f_x_2
                x_2 = b - fi * (b - a)
                f_x_2 = f(x_2)
        k += 1