# importing libraries
import numpy as np
import pandas as pd


# Constructing polynomial
def f():
    order = int(input("enter the order of the polynomial"))
    list_of_rgs = []
    for _ in range(order+1):
        list_of_rgs.append(float(input("enter the current coefficient")))

    fx = np.poly1d(list_of_rgs)
    print("f(x) : \n", fx)
    return fx


# Defining derivative of function
def g(fx):
    gx = np.polyder(fx, 1)
    print("f'(x) of order = 1 : \n", gx)
    return gx


def newtonRaphson(x0, e, N, fx, gx):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')

    step = 1
    flag = 1
    condition = True
    while condition:
        if gx(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - fx(x0) / gx(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, fx(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(fx(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
fx = f()
gx = g(fx)
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)

# Starting Newton Raphson Method
newtonRaphson(x0, e, N, fx, gx)