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
    nn = 10
    random.seed()
    A = random.sample( range(0, nn*5),  nn)
    
    print("Before:", A)
    # A = sort.Bubble(A)    
    # A = sort.Quick(A)
    # A = sort.Merge(A)
    # A = sort.Selection(A)
    A = sort.Insertion(A)

    print("After:", A)

