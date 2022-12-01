def percent_difference(x, y):
    difference = abs(x-y)   #Assignment binds name to value in the first frame of the current environment
    return 100 * difference / x

diff = percent_difference(40, 50)   #Bind the names on the left to the resulting values in the current frame

"""Non-Local Assignment & Persistent Local State"""

def make_withraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance    #Declare the name "balance" nolocal at the top of the body of the function in which it is re-assigned
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount      #Re-bind balance in the first non-local frame in which it was bound previously
        return balance
    return withdraw

"""The Effect of Nonlocal Statements"""
#Effect: Future assignments to that same change its pre-existing binding in the first non-local
#frame of the current environment in which that name is bound. 

"""Mutable Values & Persistent Local State"""

# Mutable values can be changed without a nonlocal statement

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficent funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw


"""Mutible Mutable Functions"""
john = make_withraw(100)
steven = make_withraw(10000)

"""Referential Transparency, Lost"""
# Expressions are referentially transparent if substituting an expression with its value does not change
# the meaning of a program.
# Mutation operations violate the condition of referential transparency because they do more than just return a value; they change
# the environment.

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
total = b(3) + b(4)    # total is 22, b(3) is 10, and b(4) is 12
total = 10 + b(4)   # in this case, total is 23