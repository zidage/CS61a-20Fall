from ucb import trace

@trace
def fibbo(n):
    #print("current n is ",n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbo(n-2) + fibbo(n-1)
