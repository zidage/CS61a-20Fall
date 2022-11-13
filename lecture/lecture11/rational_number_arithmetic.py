from math import gcd


def rational(n, d):
    """Construct a rational number that represents N/D."""
    def select(name):
        g = gcd(n, d)
        if name == 'n':
            return n // g
        elif name == 'd':
            return d // g
    return select


def numer(x):
    """Return the numerator of rational number X."""
    return x('n')


def denom(x):
    """Return the denominator of rational number X."""
    return x('d')


def add_rational(rx, ry):
    nx = numer(rx)
    dx = denom(rx)
    ny = numer(ry)
    dy = denom(ry) 
    return rational((nx*dy+dx*ny), (dx*dy))


def print_rational(x):
    print(numer(x))
    print("——")
    print(denom(x))