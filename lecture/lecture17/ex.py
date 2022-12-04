"""Views of a Dictionary"""

d = {'one': 1, 'two': 2, 'three': 3}
d['zero'] = 0
k = iter(d.keys())  # or iter(d)
"""
>>> next(k)
'one'
>>> next(k)
'two'
>>> next(k)
'three'
>>> next(k)
'zero'
"""

v = iter(d.values())
"""
>>> next(v)
1
>>> next(v)
2
>>> next(v)
3
>>> next(v)
0
"""

i = iter(d.items())
"""
>>> next(i)
('one', 1)
>>> next(i)
('two', 2)
>>> next(i)
('three', 3)
>>> next(i)
('zero', 0)
"""

"""For Statements"""

r = range(3, 6)
list(r)
for i in r:
    print(i)

for i in r:
    print(i)

ri = iter(r)

"""Built-in Functions for Iteration"""
# Many built-in Python sequence operations return iterators that compute results lazily

bcd = ['b', 'c', 'd']
map(lambda x: x.upper(), bcd)   #creates an iterator
m = map(lambda x: x.upper(), bcd)

def double(x):
    print('**', x, '=>', 2*x, '**')
    return 2*x

"""
>>> m = map(double, [3, 5, 7])
>>> next(m)
** 3 => 6 **
6
>>> next(m)
** 5 => 10 **
10
>>> next(m)
** 7 => 14 **
14
>>> m = map(double, range(3, 7))
>>> f = lambda y: y >= 10
>>> t = filter(f, m) 
>>> next(t)
** 3 => 6 **
** 4 => 8 **
** 5 => 10 **
10
>>> list(filter(f, map(double, range(3, 7))))
** 3 => 6 **
** 4 => 8 **
** 5 => 10 **
** 6 => 12 **
[10, 12]
>>>
"""

t = [1, 2, 3, 2, 1]
"""
>>> t = [1, 2, 3, 2, 1]
>>> t
[1, 2, 3, 2, 1]
>>> reversed(t) 
<list_reverseiterator object at 0x0000019F9DE8F8B0>
>>> reversed(t) == t 
False
>>> list(reversed(t)) 
[1, 2, 3, 2, 1]
>>> list(reversed(t)) == t
True
"""

"""Generators and Generator Functions"""

def plus_minus(x):
    yield x
    yield -x

t = plus_minus(3)
"""
>>> next(t)
3
>>> next(t)
-3
>>> t
<generator object plus_minus at 0x0000028780959E00>
"""

def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

"""
>>> t = evens(2, 10)
>>> t
<generator object evens at 0x0000010C01249A10>
>>> next(t)
2
>>> next(t)
4
>>> next(t)
6
>>> next(t)
8
>>> list(evens(1, 10))
[2, 4, 6, 8]
"""

"""Generators can Yield from Iterators"""
# A yield from statement yields all values from an iterator or iterable

def a_then_b(a, b):
    """
    for x in a:
        yield x
    for x in b:
        yield x
    """
    yield from a
    yield from b

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
    else:
        yield 'Blast off'

"""
>>> for k in countdown(3):
...     print(k)
... 
3
2
1
Blast off
"""

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

"""
>>> prefixes('both')
<generator object prefixes at 0x000001F68BDD9A10>
>>> list(prefixes('both'))
['b', 'bo', 'bot', 'both']
"""

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
        