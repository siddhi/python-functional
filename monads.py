
class Nothing:
    def map(self, fn):
        return Nothing()

    def flatmap(self, fn):
        return Nothing()

    def __str__(self):
        return "Nothing()"

class Just:
    def __init__(self, val):
        self.val = val

    def map(self, fn):
        return Just(fn(self.val))

    def flatmap(self, fn):
        return fn(self.val)

    def __str__(self):
        return f"Just({self.val})"

def inc(x):

    return x + 1
 
def inverse(x):
    if x != 0:
        return Just(1/x)
    return Nothing()

print(inverse(1).map(inc).flatmap(inverse).map(inc)) # Just(1.5)
print(inverse(-1).map(inc).flatmap(inverse).map(inc)) # Nothing()


from itertools import chain
class MultiValue:
    def __init__(self, values):
        self.values = set(values)

    def map(self, fn):
        out = {fn(val) for val in self.values}
        return MultiValue(out)

    def flatmap(self, fn):
        out = (fn(val).values for val in self.values)
        return MultiValue(chain(*out))

    def __repr__(self):
         return f'MultiValue({self.values})'

import math

def sqrt(x):
    if x == 0:
        return MultiValue({0})
    y = math.sqrt(x)
    return MultiValue({y, -y})

from operator import add
from functools import partial

add2 = partial(add, 2)

print(sqrt(4).map(add2).flatmap(sqrt).map(add2).flatmap(sqrt))
# MultiValue({0, 1.4142135623730951, 2.0, -2.0, -1.4142135623730951})


