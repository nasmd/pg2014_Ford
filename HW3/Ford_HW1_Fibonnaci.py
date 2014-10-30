# -*- coding: utf-8 -*-

# Trent Ford
# 2014-10-20
#Fibonnaci Sequence Function


"""
Created on Tue Sep 23 07:42:55 2014

@author: Trent
"""

def fib(N):
    """Return N Fibonacci numbers
    This function takes in the N number of values and outputs N Fibonacci
    numbers"""
    
    a,b = 0,1
    fibArray = []
    
    fibArray.append(b)
    for i in range(N-1):
        c = a+b
        a = b
        b = c
        fibArray.append(c)        
    return fibArray
    
if __name__ == '__main__':
    N = 5
    sequence = fib(N)
    
