# -*- coding: utf-8 -*-

#Encoding: utf-8
#Authors: P. Mayilvahanan and M. Mazourik
#Numerical Algorithms Autumn Semester 2019
#Assignment 7

def main():
  def f(x):
    return x**(3/2)+x

  def numerical_grad(f,h,x=0):
    return ((18*f(x+h))+(-9*f(x+2*h))+(2*f(x+3*h))-(11*f(x)))/(6*h)

  def analytical_grad(x=0):
    return (1.5*(x**0.5))+1

  anal_grad=analytical_grad(0)
  error_array = []
  h_array = []
  for k in range(1,16):
    num_grad=numerical_grad(f,10**-k)
    error_array.append(num_grad-anal_grad)
    h_array.append(10**-k)
    print(f'{k: <3}', f'{num_grad: <19}', 'Error:', num_grad-anal_grad)

if __name__=='__main__':
    main()

