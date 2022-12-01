this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def adder(b):
        nonlocal a
        temp = a
        a = a + 1
        return b + temp
    return adder


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    pre1 = 0
    pre2 = 1
    idx = 0

    def next_fib():
        nonlocal pre1, pre2, idx
        if idx == 0:
            idx = idx + 1
            return 0
        if idx == 1:
            idx = idx + 1
            return 1
        else:
            curr_fib = pre1 + pre2
            pre1 = pre2
            pre2 = curr_fib
            return curr_fib
    return next_fib


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    idx = 0
    ori_len = len(lst)
    ori_idx = 0
    while (True):
        if ori_idx == ori_len - 1:
            break
        elif lst[idx] == entry and entry == elem:
            lst.insert(idx + 1, elem)
            idx += 2
        elif lst[idx] == entry and entry != elem:
            lst.insert(idx + 1, elem)
            idx += 1
        else:
            ori_idx += 1
            idx += 1
    return lst

