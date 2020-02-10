#!/usr/bin/env python
# coding: utf-8
#ASSIGNMENT 4 EXERCISE 2
#Authors: Prasanna Mayilvahanan & Michael Mazourik

import numpy as np
import time
from math import sin, cos, pi
import matplotlib.pyplot as plt

def main():
    ####Function that returns actual mapping f(t) in the form of 'x' and 'y's given set of parameters/points 't_set'
    def return_curve(t_set):
        x=[]
        y=[]        
        for i in range(len(t_set)):
            coeff = (((25*(t_set[i]**2))+2)/((25*(t_set[i]**2))+1))
            x+=[float(coeff*sin((t_set[i]*pi)/2))]
            y+=[float(coeff*cos((t_set[i]*pi)/2))]
        return x,y

    ####Function that returns set of points 't_set' between [-1, 1] given number of points 'n'
    def return_sample_points(n):
        t_set = np.zeros(n+1)
        for i in range(n+1):
            t_set[i] = (2.*(i/n))-1
        return t_set


    ####Computes alpha for Neville
    def alpha(t, t_ij, t_i):
        return (t_ij - t)/(t_ij - t_i)

    ####nevilles algorithm for one point 't'
    def neville(t, t_set, x, y):
        n = len(t_set)
        qx=x.copy()
        qy=y.copy()
        for j in range(1, n):
            for i in range(0, n-j):
                qx[i] = qx[i]*alpha(t, t_set[i+j], t_set[i]) + qx[i+1]*(1 - alpha(t, t_set[i+j], t_set[i]))
                qy[i] = qy[i]*alpha(t, t_set[i+j], t_set[i]) + qy[i+1]*(1 - alpha(t, t_set[i+j], t_set[i]))
        return qx[0], qy[0]

    ####nevilles algorithm that returns set of points f(t) for points 't_set'
    def return_points_neville(sample, t_set, x, y):
        x_new = []
        y_new = []
        for i in range(len(sample)):
            temp1, temp2 = neville(sample[i], t_set, x, y)
            x_new.append(temp1)
            y_new.append(temp2)
        return x_new, y_new

    ####Dictionary for different cases d = [10, 20, 40], x and y are actual outputs of different points with their size d as keys.
    dict_cases = [10, 20, 40]
    x = dict()
    y = dict()

    ####t is different number of equally spaced points (d = [10, 20, 40]) between [-1, 1]
    t = dict()
    for d in dict_cases:
        t[d] = return_sample_points(d)
        x[d], y[d] = return_curve(t[d])
    
    ####sample is 10001 equally spaced points between [-1, 1]
    sample = return_sample_points(10000)

    ####For plotting f
    x[10000], y[10000] = return_curve(sample)


    ####nx, ny is neville's output with keys d, sample is 10001 points between [-1, 1], n_time is neville's running time through all cases.
    nx = dict()
    ny = dict()
    n_start = time.time()
    for d in dict_cases:
        nx[d], ny[d] = return_points_neville(sample, t[d], x[d], y[d])
    n_end = time.time()
    n_time = n_end - n_start
    

    ####plotting neville's curves P10, P20, P40, and actual polynomial f
    for d in dict_cases:
        plt.plot(nx[d], ny[d], label = "P"+str(d)+"_neville")
        plt.xlim(x[d][0], x[d][-1])
        plt.ylim(0, 2.0)
    plt.plot(x[10000], y[10000], label = "f")
    plt.legend()
    plt.show()


    # Barycenter form

    ####Function to calculate weights for barycenter form
    def return_w(t_set):
        w = np.zeros(len(t_set))
        for i in range(0, len(t_set)):
            w[i] = 1
            for j in range(0, len(t_set)):
                if j != i:
                    w[i]*=1/(t_set[i] - t_set[j])
        return w


    ####barycenter algorithm for one point 't'
    def barycenter(w, t, t_set, x, y):
        n = len(t_set)
        Nx = 0
        Dx = 0
        Ny = 0
        Dy = 0
        for i in range(0, n):
            if t == t_set[i]:
                return x[i], y[i]
            else:
                W = w[i]/(t-t_set[i])
               
                Nx = Nx + W*x[i]
                Dx =  Dx + W
                
                Ny = Ny + W*y[i]
                Dy =  Dy + W
        return Nx/Dx, Ny/Dy
            

    ####barycenter algorithm that returns set of points f(t) for points 't_set'
    def return_points_barycenter(sample, t_set, x, y):
        w = return_w(t_set)
        x_new = []
        y_new = []
        for i in sample:
            temp1, temp2 = barycenter(w, i, t_set, x, y)
            x_new.append(temp1)
            y_new.append(temp2)
        return x_new, y_new

    ####bx, by is barycenter's output with keys d, sample is 10001 points between [-1, 1], b_time is barycenter's running time through all cases.

    bx = dict()
    by = dict()
    b_start = time.time()
    for d in dict_cases:
        bx[d], by[d] = return_points_barycenter(sample, t[d], x[d], y[d])
    b_end = time.time()
    b_time = b_end - b_start



    ####plotting barycenter's curves P10, P20, P40, and actual polynomial f
    for d in dict_cases:
        plt.plot(bx[d], by[d], label = "P"+str(d)+"_barycenter")
        plt.xlim(x[d][0], x[d][-1])
        plt.ylim(0, 2.0)
    plt.plot(x[10000], y[10000], label = "f")
    plt.legend()
    plt.show()


    # Newton's Differences Algorithm. We have stated the precise algorithm that we have used in the other file


    ####Function to calculate F
    def return_F(t_set, x, y):
        n = len(t_set)
        Fx = np.zeros((n, n))
        Fy = np.zeros((n, n))
        for i in range(0, n):
            Fx[i, 0]  = x[i]
            Fy[i, 0]  = y[i]
        for i in range(1, n):
            for j in range(1, i+1):
                Fx[i, j] = (Fx[i, j-1] - Fx[i-1, j-1])/(t_set[i] - t_set[i-j])
                Fy[i, j] = (Fy[i, j-1] - Fy[i-1, j-1])/(t_set[i] - t_set[i-j])
        return Fx, Fy

    ####Newton's differences algorithm for one point 't'
    def return_value(t, t_set, Fx, Fy):
        n = len(t_set)            
        Px = Fx[0, 0]
        Py = Fy[0, 0]
        for i in range(1, n):
            temp = 1
            for j in range(0, i):
                temp = temp*(t - t_set[j])
            Px = Px + Fx[i, i]*temp
            Py = Py + Fy[i, i]*temp
        return Px, Py

    ###newton's algorithm that returns set of points f(t) for points 't_set'
    def return_points_newton(sample, t_set, x, y):
        x_new = []
        y_new = []
        Fx, Fy = return_F(t_set, x, y)
        for t in sample:
            Px, Py = return_value(t, t_set, Fx, Fy)
            x_new.append(Px)
            y_new.append(Py)
        return x_new, y_new

    ####ndx, ndy is barycenter's output with keys d, sample is 10001 points between [-1, 1], nd_time is barycenter's running time through all cases.
    ndx = dict()
    ndy = dict()

    nd_start = time.time()
    for d in dict_cases:
        ndx[d], ndy[d] = return_points_newton(sample, t[d], x[d], y[d])
    nd_end = time.time()
    nd_time = nd_end - nd_start


    ####plotting barycenter's curves P10, P20, P40, and actual polynomial f
    for d in dict_cases:
        plt.plot(ndx[d], ndy[d], label = "P"+str(d)+"_newton")
        plt.xlim(x[d][0], x[d][-1])
        plt.ylim(0, 2.0)
    plt.plot(x[10000], y[10000], label = "f")
    plt.legend()
    plt.show()

    print("Neville's algorithm time in seconds is {}".format(n_time))
    print("Barycenter's algorithm time in seconds is {}".format(b_time))
    print("Newton's algorithm time in seconds is {}".format(nd_time))
    print("Barycenter is the fastest")

if __name__ == '__main__':
    main()

