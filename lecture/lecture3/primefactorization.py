def prime_factors(n):
    """Print the prime factors of n in non-decreasing order."""

    while n>1:
        k=smallest_prime_factor(n)
        n=n//k
        print(k)

def smallest_prime_factor(n):
    """Return the smallest k>1 that evenly divides n."""
    k=2
    while n % k != 0:
        k=k+1
    return k
