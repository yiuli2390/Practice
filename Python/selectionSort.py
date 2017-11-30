# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 13:27:51 2017

@author: Zero
"""

def selectionSort(A, N):
    sw = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
            '''
            temp = A[i]
            A[i] = A[minj]
            A[minj] = temp
            '''
            sw += 1
            print A
    return sw

A = [int(x) for x in raw_input().split()]
N =len(A)

sw = selectionSort(A, N)

print sw
print A