"""Object-Oriented Programming"""
# A method for organizing modular programs.
# Abstraction barriers.
# Bundling together information and related behaviour.

# A metaphor for computation using distributed state.
# Each object has its own local state.
# Each object also knows how to manage its own local state, based on method calls.
# Methods calls are messages passed between objects.
# Several objects may all be instances of a common type.
# Different types may relate to each other.

#Specialized syntax and vocabulary to support this metaphor.


"""Classes"""
# A class serves as a template for its instances.

"""The Class Statement"""
# A class statement creates a new class and binds that class to <name> in the first frame of the current environment.
# Assignment & def statements in <suite> create attributes of the class (not names in frames)
# The suite is executed when the class statement is excuted.

"""Object Construction"""
# Ideas: All bank accounts have a balance and an account holder;
# the Account class should add those attributes to each of its instances.

"""Object Identity"""
# Every object that is an instance of a user-defined class has a unique identity.
# Identity operators "is" and "is not" test if two expressions evaluate to the same object
# Binding an object to a new name using assignment does not create a new object.


"""Methods"""
# Methods are defined in the suite of a class statement
class Account:

    interest = 0.02    # interest is not part of the instance that was somehow copied from the class!

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
# These def satements create function objects as always, 
# but their names are bound as attributes of the class.

"""Invoking Methods"""
# All invoked methods have access to the object via the self parameter, and so can
# all access and manipulate the object's state.
# Dot notation automatically supplies the first argument to a method.

"""Dot Expressions"""
# Objects receive messages via dot notation.
# Dot notation accesses attributes of the instance or its class.
# <expression> . <name>
# The <expression> can be any valid Python expression.
# The <name> must be a simple name.
# Evaluates to the value of the attribute looked up by <name> in the object 
# that is the value of the <expression>.

"""Attributes"""
"""
>>> john = Account('John')
>>> john.balance
0
>>> getattr
<built-in function getattr>
>>> getattr(john, 'balance')
0
>>> john.deposit(100)
100
>>> getattr(john, 'balance')
100
>>> hasattr(john, 'balance') 
True
>>> hasattr(john, 'lance')   
False
"""
# Using getattr, we can look up an attribute using a string
# getattr and dot expressions look up a name in the same way.

# Looking up an attribute name in an object may return:
# One of its instance attributes, or
# One of the attributes of its class

"""Methods and Functions"""
# Python distinguishes between:
# Functions, which we have been creating since the beginning of the course, and
# Bound methods, which couple together a function and the object on which that
# method will be invoked.
# Object + Function = Bound Method

"""Looking Up Attributes by Name"""
# <expression> . <name>
# To evaluate a dot expression:
# 1.Evaluate the <expression> to the left of the dot, which yields the object of the dot expression.
# 2.<name> is matched against the instance attributes of that object; if an attribute with that name exists, its value is returned.
# 3.If not, <name> is looked up in the class, which yields a class attribute value.
# 4.That value is returned unless it is a function, in which case a bound method is returned instead

"""Class Attributes"""
# Class attributes are "shared" across all instances of a class because
# they are attributes of the class, not the instance.
