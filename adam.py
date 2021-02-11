"""Just for practicing Sphinx"""

def sum_two(a, b):
    """Compute sum of two values, and return int"""
    return a + b

def get_biggest(x):
    """Return the biggest value

    Key arguments:
    x -- list of int
    """
    ret = x[0]
    for i in range(1, len(x)):
        if x[i] > ret:
            ret = x[i]
    return ret

print('sum_two() result = ', sum_two(1, 3))
print('get_biggest() result = ', get_biggest([5,3,4,-10,0]))
