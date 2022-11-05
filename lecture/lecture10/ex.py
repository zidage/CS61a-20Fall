def count(s, value):

    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print("Go Bears!")

def mysum(L):
    if L == []:
        return 0
    else:
        return L[0] + mysum(L[1:])

def divisors(n):
    return [1] + [x for x in range(2,n) if n % x == 0]

def reverse(n):
    if len(n) == 1:
        return n
    else:
        return reverse(n[1:]) + n[0]