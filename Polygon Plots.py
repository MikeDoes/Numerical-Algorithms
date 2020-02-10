## NA Assignment 11
## Authors: Prasanna Mayilvahanan & Michael Mazourik

## Imports

import numpy as np
import random
import matplotlib.pyplot as plt


## Generate n points between -1 to 1

def generate_arrays(n, numLow = -1000, numHigh = 1000):
    x = np.random.randint(numLow, numHigh, n-1)
    y = np.random.randint(numLow, numHigh, n-1)
    
    x = np.append(x, - np.sum(x))
    y = np.append(y, - np.sum(y))
    
    x = x/abs(x).max()
    y = y/abs(y).max()
    
    return x, y

## Function to compute norm 2

def norm2(x): return np.sqrt(np.sum(np.square(x)))

## Function that returns the Averaging matrix

def return_M(n):
    M = np.zeros((n, n))
    for i in range(n-1):
        M[i, i] = 1
        M[i, i+1] = 1
    M[n-1, n-1] = 1
    M[n-1, 0] = 1
    M = M/2
    return M

## Number of points

N = 50

## Generating 3 sets of random initial polygons
x = {}
y = {}
for i in range(3):
    x[i], y[i] = generate_arrays(N)

## Get averaging matrix

M = return_M(N)


## Returns P(k)

def return_points(k, x = x, y = y, M = M):
    for i in range(k):
        u = np.matmul(M, x)
        v = np.matmul(M, y)

        x = u/norm2(u)
        y = v/norm2(v)
    
    return x, y

## Find P(k) for all the 3 sets after iterations 50, 100,...., 1000

x_new = {}
y_new = {}
for i in range(3):
    x_new[i] = {}
    y_new[i] = {}
    for j in range(50, 1001, 50):
        x_new[i][j], y_new[i][j] = return_points(j, x = x[i], y = y[i], M = M)


## Polygon 1 plot

temp = 0
for k in x_new[temp].keys():
    plt.plot(x_new[temp][k], y_new[temp][k], label = str(k))
plt.title('Polygon1')
plt.legend(loc = 'lower right')
plt.show()

## Polygon 2 plot

temp = 1
for k in x_new[temp].keys():
    plt.plot(x_new[temp][k], y_new[temp][k], label = str(k))
plt.title('Polygon2')
plt.legend(loc = 'lower right')
plt.show()

## Polygon 3 plot

temp = 2
for k in x_new[temp].keys():
    plt.plot(x_new[temp][k], y_new[temp][k], label = str(k))
plt.title('Polygon3')
plt.legend(loc = 'lower right')
plt.show()






