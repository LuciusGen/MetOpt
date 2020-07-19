import sys
import time
from scipy import optimize
from sympy import diff, symbols, solve


def function(x):
    return -2 * x[0] - 4 * x[1] + pow(x[0], 2) + 2 * pow(x[1], 2)


def grad_func(x):
    return [-2 + 2*x[0], -4 + 4*x[1]]


def read_data(file):
    g_i, counter = list(), 0
    b = []
    for line in file:
        g_i.append([])

        for i in line.split():
            g_i[counter].append(int(i))
        b.append(g_i[counter].pop(len(g_i[counter]) - 1))
        counter += 1

    return g_i, b


def build_z(x):
    grad = grad_func(x)
    z = []
    for i in grad:
        z.append(i)

    return z


def solve_lp(x, g_i, b):
    answer = optimize.linprog(c=build_z(x), A_ub=g_i, b_ub=b)

    if answer.success is True:
        return answer.x
    else:
        return False


def find_alpha(x, z):
    alpha = symbols('alpha', real=True)
    x_new = []
    for i in range(len(x)):
        x_new.append(x[i] + alpha*(z[i] - x[i]))

    tmp = [i for i in solve(diff(function(x_new)))]

    return min(1, *tmp)


def new_x(x, g_i, b):
    z = solve_lp(x, g_i, b)
    if z is not False:
        alpha = find_alpha(x, z)
        x_new = []
        for i in range(len(x)):
            x_new.append(x[i] + alpha*(z[i] - x[i]))

        return x_new
    return False


def solve_ysl(eps, x_0, g_i, b):
    r=1
    x_k, x_prev = new_x(x_0, g_i, b), x_0
    if x_k is False:
        return False
    norm = []
    for i in range(len(x_k)):
        norm.append((x_k[i] - x_prev[i]) ** 2)
    while sum(norm) > pow(eps, 2):
        x_prev = x_k
        r += 1
        x_k = new_x(x_prev, g_i, b)
        if x_k is False:
            return False
        norm = []
        for i in range(len(x_k)):
            norm.append((x_k[i] - x_prev[i]) ** 2)

    return x_k, r


sys.stdout = open("out.txt", "w")
g_i, b = read_data(open("input.txt", "r"))
stat_time = time.time()
#print(solve_ysl(0.01, [-75, -95], g_i, b))
print("time = ", time.time() - stat_time)
print("--------------------------------------------")
