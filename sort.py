#!/usr/bin/env python3

"""
File name     : sort.py
Author        : Ryky Nelson
Created Date  : October 2021
Python Version: Python 3.6.9

Description:
a list of simple implementations of sorting algorithms
"""

def Bubble(A):
    if not A or len(A) == 1 : return A
    nn = len(A)
    for i in range(nn - 1):
        swap = False
        for j in range( nn - 1 - i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swap = True
        if not swap: break

    return A


def Quick(A):
    if not A or len(A) == 1 : return A
    nn = len(A)
    p = nn - 1
    s = 0
    while s < p:
        if A[s] > A[p]:
            A[s], A[p-1] = A[p-1], A[s]
            A[p-1], A[p] = A[p], A[p-1]
            p -= 1
        else: s += 1

    return Quick(A[:p]) + [A[p]] + Quick(A[p+1:])

def Merge(A):
    if not A or len(A) == 1 : return A
    nn  = len(A)
    mid = nn // 2
    L = Merge(A[0:mid])
    R = Merge(A[mid:])
    ll, lr = len(L), len(R)

    B = []
    lidx, ridx = 0, 0
    while lidx < ll and ridx < lr:
        if L[lidx] < R[ridx]:
            B.append( L[lidx] )
            lidx += 1
        else:
            B.append( R[ridx] )
            ridx += 1

    if   lidx < ll: B += L[lidx:]
    elif ridx < lr: B += R[ridx:]

    return B
    
def Selection(A):
    if not A or len(A) == 1 : return A
    nn = len(A)
    for i in range(nn):
        imin = i
        cmin = A[imin]
        for j in range(i,nn):
            if A[j] < cmin:
                cmin = A[j]
                imin = j

        if i != imin: A[i], A[imin] = A[imin], A[i]

    return A

def Insertion(A):
    if not A or len(A) == 1 : return A
    nn = len(A)
    for i in range(1,nn):
        j = i - 1
        while j >= 0 and A[i] < A[j]: j -= 1
        A = A[:j+1] + [A[i]] + A[j+1:i] + A[i+1:]
        
    return A

    
