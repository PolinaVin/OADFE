
# coding: utf-8

# In[1]:


#!/usr/bin/env python3



from collections import namedtuple





Result = namedtuple('Result', ('nfev', 'cost', 'gradnorm', 'x'))

Result.__doc__ = """Результаты оптимизации



Attributes

----------

nfev : int

    Полное число вызовов модельной функции

cost : 1-d array

    Значения функции потерь 0.5 sum(y - f)^2 на каждом итерационном шаге.

    В случае метода Гаусса—Ньютона длина массива равна nfev, в случае ЛМ-метода

    длина массива — менее nfev

gradnorm : float

    Норма градиента на финальном итерационном шаге

x : 1-d array

    Финальное значение вектора, минимизирующего функцию потерь

"""
def gauss_newton(y, f, j, x0, k=1, tol=1e-4):
    nfev = 0
    cost = []  #Значения целевой ф-ции
    gradnorm = 2 * tol
    while gradnorm > tol:
        nfew += 1
        residual = y - f(*x0)
def f(a, b, c):
    return a * b + c
x = [1, 2, 3]
f(*x)

