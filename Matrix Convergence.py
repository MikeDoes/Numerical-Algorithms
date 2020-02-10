# -*- coding: utf-8 -*-

#Encoding: utf-8
#Authors: P. Mayilvahanan and M. Mazourik
#Numerical Algorithms Autumn Semester 2019

def main():
    #Parameters indicated by the problem guidelines
    precision=1e-16
    N=99999
    
    #In case of no convergence please take a larger value of iterations
    iterations = 1000

    #Initialising the Variables
    prev_guess=[0 for _ in range(N)]
    x=[0 for _ in range(N)]


    #For code hygiene and so that the machine does not calculate the same things over and over 
    middle=int(N/2)

    #To avoid spamming the iterations in the console, we let the user know that it may take a couple tens of seconds
    print('The program is running. On average, for the N given in the assignment it takes 10 seconds, please wait until it is executed :)\n')

    #We created a 'for loop' instead of a 'while loop' in case the method does not converge for this specific matrix
    for j in range(iterations):
        #For loop to go through the rows of the matrix. It could be divided into 4 parts
        for i in range(N):
            #The top row will always have a 6 in first index, -2 in second and 1 in last.
            if i==0:
                x[0]=(5+2*x[1]-x[-1])/6

            #The bottom row will always have a 6 in last index, -2 in second to last and 1 in first.
            elif i==N-1:
                x[-1]=(5+2*x[-2]-x[0])/6

            #The middle row will always have 6 in the middle and -2 surrounding it
            elif i==middle:
                x[middle]=(2+2*x[middle-1]+2*x[middle+1])/6

            #All the other rows. These always have -2 surrounding the diagonal 6 and 1 coming going from before last to second position
            else:
                x[i]=(3+2*x[i-1]+2*x[i+1]-x[N-i-1])/6
        #Converting the mathematical expression for machine precision. The python zip functions enables to iterate in a clean manner enabling us to check within O(n)
        if max([abs(v1-v2) for v1,v2 in zip(prev_guess,x)])<precision:
            print('Success after '+str(j+1)+ ' iterations! In other words k = '+str(j)+'.')
            print('The first 10 elements of the answer (x) are:\n'+str(x[:10]))
            print('It is a 99999 dimensional vector composed of \'1s\' only')
            break

        #Change the previous guess to the current copy of x so that we can compare the precision
        prev_guess=x.copy()

if __name__=='__main__':
    main()

