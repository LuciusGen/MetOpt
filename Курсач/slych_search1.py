import sys
import time

import numpy as np
from ysl_grad import function, read_data


def uniform_gen(n : int) -> np.array:
    return np.random.uniform(-1, 1, n)


def uniform_gen2(n : int) -> np.array:
    return np.random.uniform(0, 1, n)


def rand_search_fail_return(x_0:list, lamb_0, eps, func, g_i, b) -> list:
    x_r, lamb_r, n, x_r2 = x_0, lamb_0, len(x_0), list()
    K, k = 3 * n, 0
    max_counter, counter = 1000, 0
    r = 1

    while True:
        psi_r = uniform_gen(n)
        r += 1
        norm_psi_r = np.linalg.norm(psi_r)
        flag = False
        x_r2 = x_r + lamb_r * (psi_r / norm_psi_r)

        for i in range(len(g_i)):
            if sum(np.array(g_i[i]) * np.array(x_r2)) > b[i]:
                flag = True
                counter += 1
                break

        if flag is True:
            continue

        if counter == max_counter:
            break

        if func(x_r2) < func(x_r):
            k = 1
            x_r = x_r2
            continue
        else:
            k += 1

        if abs(func(x_r2) - func(x_r)) < eps:
            return x_r2, r

        if k == K:
            lamb_r = lamb_r * np.random.random()
            k = 0


def random_research_best_probe(x_0:list, lamb_0, eps, func, g_i, b) -> list:
    x_r, lamb_r, n, x_r2 = x_0, lamb_0, len(x_0), list()
    M = 5
    max_counter, counter = 1000, 0
    r = 1
    while True:
        r += 1
        psi_r = uniform_gen(n)
        norm_psi_r = np.linalg.norm(psi_r)
        x_r2 = x_r + lamb_r * (psi_r / norm_psi_r)

        for _ in range(M):
            psi_r = uniform_gen(n)
            norm_psi_r = np.linalg.norm(psi_r)
            x_r_tmp = x_r + lamb_r * (psi_r / norm_psi_r)

            if counter == max_counter:
                break

            if func(x_r_tmp) < func(x_r2):
                x_r2 = x_r_tmp

        if not in_d(x_r2, g_i, b):
            counter += 1
            continue

        if func(x_r2) < func(x_r):
            x_r = x_r2
            continue
        else:
            lamb_r = lamb_r * np.random.random()

        if abs(func(x_r2) - func(x_r)) < eps:
            return x_r2, r


def find_index_max_x(x_r_i, func):
    f_max = -np.inf
    k = 0
    for i in range(len(x_r_i)):
        f_tmp = func(x_r_i[i])
        if f_max < f_tmp:
            k = i
            f_max = f_tmp

    return k


def reflection(x_r_i, k, n, alpha):
    x_c_r = (np.array(sum(x_r_i)) - x_r_i[k]) / (n-1)

    x_r_i[k] = x_c_r + alpha * (x_c_r + x_r_i[k])
    return x_r_i


def in_d(x, g_i, b):
    for i in range(len(g_i)):
        if sum(np.array(g_i[i]) * np.array(x)) > b[i]:
            return False
    return True


def random_research_complex(x_0:list, l, eps, func, g_i, b) -> list:
    x_r = x_0
    x_r_i = list()
    i, n, N = 0, len(x_0), 2 * len(x_0)
    alpha = 1.0
    r = 1

    x_r_i.append(np.array(x_0))

    while i < N - 1:
        psi_r = uniform_gen2(n)
        pos_x = psi_r
        if in_d(pos_x, g_i, b) and pos_x[0] > 0 and pos_x[1] > 0:
            x_r_i.append(np.array(pos_x))
            i += 1

    while True:
        r += 1
        k = find_index_max_x(x_r_i, func)
        x_k_r = x_r_i[k]
        while True:
            x_r_i = reflection(x_r_i, k, N, alpha)
            if not in_d(x_r_i[k], g_i, b):
                x_r_i[k] = x_k_r
                r+=1
                alpha /= 2
                continue
            if func(x_r_i[k]) >= func(x_k_r):
                x_r_i[k] = x_k_r
                alpha /= 2
                r+=1
                continue
            break

        x_c_r = sum(x_r_i)/N
        if np.sqrt(sum([np.linalg.norm(i - x_c_r) for i in x_r_i]))/n < eps:
            return [x_c_r, r]


def count_med(method, function, g_i, b):
    tmp1 = list()
    tmp2 = list()
    for i in range(100):
        tmp = method([0, 0], 1, 0.001, function, g_i, b)
        tmp1.append(tmp[0])
        tmp2.append(tmp[1])

    print(np.array(sum(tmp1)) / 100, sum(tmp2) / 100)


g_i, b = read_data(open("input.txt", "r"))
stat_time = time.time()
count_med(rand_search_fail_return, function, g_i, b)
print("time = ", (time.time() - stat_time)/100)
print("--------------------------------------------")
stat_time = time.time()
count_med(random_research_best_probe, function, g_i, b)
print("time = ", (time.time() - stat_time)/100)
print("--------------------------------------------")
stat_time = time.time()
count_med(random_research_complex, function, g_i, b)
print()
print("time = ", (time.time() - stat_time)/100)
sys.stdout.close()
