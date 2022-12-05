def memory(n):
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f


def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)


def group_by(s, fn):

    grouped = {}
    for e in s:
        key = fn(e)
        if grouped.__contains__(key):
            grouped[key].append(e)
        else:
            grouped[key] = [e]
    return grouped

def add_this_many(x, el, s):
    times = 0
    for e in s:
        if e == x:
            times += 1
    for i in range(times):
        s.append(el)

def filter(iterable, fn):
    for x in iterable:
        if fn(x):
            yield x


def merge(a, b):
    val1 = next(a)
    val2 = next(b)
    while True:
        if val1 == val2:
            yield val1
            val1 = next(a)
            val2 = next(b)
        elif val1 < val2:
            yield val1
            val1 = next(a)
        else:
            yield val2
            val2 = next(b)

