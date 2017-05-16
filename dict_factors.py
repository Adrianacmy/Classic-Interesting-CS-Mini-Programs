#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Sun May  15 

@author: Adrianacmy

Create a function factors that takes in an integer n and generates a dictionary 
that contains the factors of all values from 1 to n. A factor is any number that
evenly divides another number. For example, the factors of 6 are 1, 2, 3, and 
6. Factors of 15 are 1, 3, 5, and 15. The keys of your dictionary should be an
integer between 1 and n and the values should be a list of factors for that 
particular key.
'''


def factors(n):
    '''create a list of factors for n
        n: integer 
        return: a factor list 
    '''
    factor_lst = []

    for i in range(1, n + 1):
        if n % i == 0:
            factor_lst.append(i)

    return factor_lst


def factor_dict(n):
    '''create a dict with keys of all numbers less than n and values of their factors'''

    dict = {}
    for i in range(1, n + 1):
        dict[i] = factors(i)
        
    return dict

        
def main():
    n = 9
    print(factor_dict(n))


if __name__ == '__main__':
    main()
