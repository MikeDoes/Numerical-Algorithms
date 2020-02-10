#!/usr/bin/env python
# coding: utf-8
#Authors: P. Mayilvahanan and M. Mazourik
#Imports Necessary to use math Symbols and Derivatives
from sympy import Symbol, Derivative
def main():
    segment_dic=[
        {'d':5, 's':3 },
        {'d':2, 's':2 },
        {'d':3, 's':6 },
        {'d':3, 's':1 }
    ]
    time=10
    starting_point=-0.2
    c= Symbol('c')

    function=-time+c*0
    c_search=[starting_point]
    N=7

    for segment in segment_dic:
        c= Symbol('c')
        term=segment['d']/(segment['s']+c)
        function+=term

    def findTangent(function,value):
        c= Symbol('c')
        deriv= Derivative(function, c).doit()
        derivative_value= deriv.subs({c:value})
        return derivative_value

    for i in range(N):
        a=function.doit().subs({c:c_search[i]})
        b=findTangent(function,c_search[i])
        c_search.append(c_search[i]-(a/b))
        print(str(i)+". "+str(c_search[i]))
        
    
    print('\nFinal Value: ' + str(c_search[-1]))
    
if __name__ == "__main__":
    main()




