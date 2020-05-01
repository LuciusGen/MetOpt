from lab_3_golden_section import golden_section
from numpy import linalg, dot, array
from typing import Callable, NewType
from math import cos, sin

Point = NewType('Point', array)
Vector = NewType('Vector', array)


def func(x: Point):
    return 4*pow(x[0], 2) + pow(x[1], 2) + cos(6 * x[0] + x[1]) - x[0] + 2 * x[1]


def func_grad(x: Point):
    return [-6 * sin(6 * x[0] + x[1]) + 8 * x[0] - 1, -1 * sin(6 * x[0] + x[1]) + 2 * x[1] + 2]


def gradient_descent(function, gradient, nullPoint, Eps):
    x_k = nullPoint
    while True:
        yield x_k
        grad_x_k = gradient(x_k)
        grad_x_k_norm = linalg.norm(grad_x_k)
        if pow(grad_x_k_norm, 2) < pow(Eps, 2):
            return x_k
        alpha_k = golden_section(0, 10, lambda alpha: function(x_k - dot(alpha, grad_x_k)), Eps)
        x_k = x_k - dot(alpha_k, grad_x_k)


def run_gradient_descent(f, grad, x0=Point([-1., 2.]), Eps=0.01, output_filename="out.txt"):
    steps = list(gradient_descent(f, grad, x0, Eps))
    with open(output_filename, "w+") as file_out:
        file_out.write(str(steps[len(steps) - 1][0]) + " " + str(steps[len(steps) - 1][1]) + "\n")
        file_out.write(str(len(steps)) + "\n")
        file_out.write("f =" + str(func([steps[len(steps) - 1][0], steps[len(steps) - 1][1]])))
    return steps


run_gradient_descent(func, func_grad, array([0, 0]))
