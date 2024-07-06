

def add(a, b):
    return a + b
 


sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b


def add1(a):
    def add2(b):
        return add(a, b)
    return add2


fn = add1(5)
print(fn(10)) # 15


def curry(fn):
    def curried_fn(a):
        def second_fn(b):
            return fn(a, b)
        return second_fn
    return curried_fn


mul1 = curry(mul)
fn = mul1(5)
print(fn(10)) # 50


from functools import partial

fn = partial(sub, a=5)
print(fn(b=3)) # 2


inc = partial(add, 1)
dbl = partial(mul, 2)

print(inc(5)) # 6
print(dbl(20)) # 40


def compose2(first_fn, second_fn):
    def composed(val):
        return second_fn(first_fn(val))
    return composed


inc_then_dbl = compose2(inc, dbl)
print(inc_then_dbl(5)) # 12

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = Point(2, 5)
b = Point(2, 5)
print(a == b)
a.x = 10

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

a = Point(2, 5)
b = Point(2, 5)
print(a == b)


