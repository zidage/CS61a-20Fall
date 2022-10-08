def fib(n)
"""Compute the nth Fibonacci number,for N>=1."""
    pred,curr = 0,1     #0th and 1st Fibonacci numbers
    k = 1   #curr is the kth Fibonacci number
    while k<n
        pred,curr = curr,pred+curr
        k=k+1
    return curr

