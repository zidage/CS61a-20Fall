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