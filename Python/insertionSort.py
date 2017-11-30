# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 11:44:20 2017

@author: Zero
"""


def trace(A, N):
    print A
    '''
    for i in range(N):
        if i > 0:
            print " "
        print A[i]
    print "\n"
    '''
    return

def insertionSort(A , N):
    for i in range(1, N):
        v = A[i]
        j = i-1
        ### if a number is less than i then move the pervious number up once
        while j>=0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        ### the while loop will -1 and found the appropriate position till a 
        ### number not less than V or put in the original position
        A[j+1] = v
        print "v is: ", v
        print "j is: ", j
        trace(A,N)
    return


### N = input("input a number:")
A = [int(x) for x in raw_input().split()]
N = len(A)

'''
for i in range(N):
    A.append(input())
'''
insertionSort(A,N)