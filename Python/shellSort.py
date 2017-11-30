# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 14:20:43 2017

@author: Zero
"""

def insertionSort(A, N, g):
    global cnt
    for i in range(g, N):
        v = A[i]
        j = i-g
        while j>=0 and A[j]>v:
            A[j+g] = A[j]
            j-=g
            cnt+=1
        A[j+g] = v
        print A

def shellSort(A, N):
    g = 1
    for h in range(g, N):
        if g > N:
            break
        G.append(g)
        g = 3*g+1
        print "g is: ", g
    
    for i in range(len(G)-1, 0, -1):
        insertionSort(A, N, G[i])

G =[]
A = [int(x) for x in raw_input().split()]
N = len(A)

shellSort(A,N)

print "G is: ", G
print "counter: ", cnt
print "A is: ", A