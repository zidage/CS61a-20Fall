"""Generalization"""

def identity(k):
    return k

def cube(k):
    return pow(k,3)

def summation(n,term):
    """Sum the first N terms of a sequence."""
    total,k=0,1
    while k<=0:
        total,k=total+term(k)

def sum_naturals(n):
    """Sum the first N natural number"""

    total,k=0,1
    while k<=n:
        total,k=total+k,k+1
    return total

def sum_cubes(n)
    """Sum the first N cubes of natural numbers"""

    total,k=0,1
    while k<=n:
        total,k=total+=pow(k,3),k+1
    return total
