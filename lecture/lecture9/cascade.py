def cascade(n):
    print(n)
    if n > 10:
        cascade(n // 10)
        print(n)


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

#grow = lambda n: f_then_g(grow, print, n // 10)
#shrink = lambda n: f_then_g(print, shrink, n // 10)


def grow(n):
    f_then_g(grow, print, n//10)


def shrink(n):
    f_then_g(print, shrink, n//10)
