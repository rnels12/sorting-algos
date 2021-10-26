#!/usr/bin/env python3

"""
File name     : main.py
Author        : Ryky Nelson
Created Date  : October 2021
Python Version: Python 3.6.9

Main function: 
- to produce a list of random numbers
- to call a sorting algorithm 
- to display the orignal and sorted lists
"""

import random
import sort

if __name__ == "__main__":
    nn = 15
    random.seed()
    A = random.sample( range(0, nn*5),  nn)
    
    print("Unsorted:", A)
    B = sort.Bubble(A)    
    # C = sort.Quick(A)
    # D = sort.Merge(A)
    # E = sort.Selection(A)
    # F = sort.Insertion(A)

    print("Sorted:", B)
    # print("Sorted:", C)
    # print("Sorted:", D)
    # print("Sorted:", E)
    # print("Sorted:", F)

