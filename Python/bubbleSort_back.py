# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 17:02:15 2017

@author: Zero
"""

def bubbleSort(A,N):
    sw = 0
    for i in range(0, N-1):
        for j in range(N-1, i, -1):
            print "ï is: ", i
            print "j is: ", j
            if A[j] < A[j - 1]:
                temp = A[j]
                A[j] = A[j - 1]
                A[j - 1] = temp
                sw += 1
                ###print A
            print A
    return sw

A = [int(x) for x in raw_input().split()]
N = len(A)
print "N is : " , N
sw = bubbleSort(A,N)

print A
print sw