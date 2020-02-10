#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/env python
#Encoding: utf-8
#Authors: P. Mayilvahanan and M. Mazourik
#Numerical Algorithms Autumn Semester


## Imports and splitting links file at '\n'

import numpy as np
with open('links.txt') as f:
    links = f.read()
    links=links.split('\n')[1:-1]


## Generating a dictionary of each page with its links

n=15
link_dic={}
for i in range(n):
    link_dic[i+1]=[]
for i in links:
    page=int(i.split(' ')[0])
    back_link=int(i.split(' ')[1])
    link_dic[page].append(back_link)


## Computing the ranking
def compute_ranking(link_dic=link_dic):
    # Computing A
    A=np.zeros([n,n])
    for i in link_dic:
        length=len(link_dic[i])
        for j in link_dic[i]:
            A[j-1][i-1]=1/length

    # mew
    mew=0.15
    
    # Generating e of 1s
    e=np.array([1/n for i in range(15)])
    x_new=np.array([1/n for i in range(15)])
    inf_norm=1999
    iterations=0
    
    # Iterating until inf norm condition is satisfied
    while inf_norm >= 1e-8:
        iterations+=1
        x_old=x_new.copy()
        x_new=(1-mew)*np.matmul(A,x_new)+mew*e
        inf_norm=np.max(np.abs(x_new-x_old))    
    
    # Ranking and printing
    ranking=np.argsort(x_new)[::-1]+1
    print('Number of Iterations', iterations)
    print('Eigen Vector', x_new)
    print('Ranking', ranking)



# Printing for first case
compute_ranking(link_dic)
link_dic[14]+=[14]

# Printing after adding link to 14
print('--------------')
compute_ranking(link_dic)

