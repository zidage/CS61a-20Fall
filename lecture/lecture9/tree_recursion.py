from ucb import trace

@trace
def max_subseq(n, t):
    if n == 0 or t == 0:
        return 0
    with_ones = max_subseq(n // 10, t-1) * 10 + n%10
    not_with = max_subseq(n//10, t)
    if with_ones > not_with:
        return with_ones
    else:
        return not_with
        
max_subseq(1234,3)