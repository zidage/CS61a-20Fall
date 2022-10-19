

"""
def keep_ints(cond,n):

    def f(cond):
        i=1
        while(i<=n):
            if(cond(i)):
                print(i)
            i+=1

    return f(cond)

def is_even(x):
    return x % 2 == 0

keep_ints(is_even,5)

def make_keeper(n):
    def f(cond):
        i=1
        while(i<=n):
            if(cond(i)):
                print(i)
            i+=1
    return f

make_keeper(5)(is_even)

def curry2(h):
    def f(x):
        def g(y):
            return h(x,y)
        return g
    return f

test=lambda h:lambda x:lambda y:h(x,y)

make_adder=test(lambda x,y:x+y)
add_three=make_adder(3)
add_four=make_adder(4)
five = add_three(2)
print("For problem on page 7")
print(five)

n=7

def f(x):
    n=8
    return x+1

def g(x):
    n=9
    def h():
        return x+1
    return h

def f(f,x):
    return f(x+n)

f = f(g,n)

g= (lambda y: y())(f)

print("For problem on page 7 Tutorial")
print(f)
print(g)
"""
y="a"
h = y
def y(y):
    h="h"
    if y==h:
        return y+"i"
    y = lambda y: y(h)
    return lambda h: y(h)
y = y(y)(y)
print(y)

