def tree(lable, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [lable] + list(branches)

def lable(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(lable(left)+lable(right), [left, right])

def count_leaves(t):
    """Count the leaves of a tree"""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
    if is_leaf(tree):
        return [lable(tree)]
    else:
        return sum([leaves(s) for s in branches(tree)], [])

def increment_leaves(t):
    """Return a tree like t but with leaf lables incremented"""
    if is_leaf(t):
        return tree(lable(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(lable(t), bs)

def increment(t):
    """Return a tree like t but with all labels incremented"""
    return tree(lable(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print('  ' * indent + str(lable(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def fact_times(n, k):
    """Return k * n * (n-1) * ... * 1"""
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)


numbers = tree(3, [tree(4), tree(5, [tree(6)])])

haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])

def print_sums(t, so_far):
    so_far = so_far + lable(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)