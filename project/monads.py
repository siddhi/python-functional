from itertools import chain 

class Nothing:
    def map(self, fn):
        return Nothing()

    def flatmap(self, fn):
        return Nothing()

    def __str__(self):
        return 'Nothing()'

class Just:
    def __init__(self, val):
        self.val = val

    def map(self, fn):
        return Just(fn(self.val))

    def flatmap(self, fn):
        return fn(self.val)

    def __str__(self):
        return f'Just({self.val})'

class MultiValue:
    def __init__(self, values):
        self.values = set(values)

    def map(self, fn):
        out = {fn(val) for val in self.values}
        return MultiValue(out)

    def flatmap(self, fn):
        out = (fn(val).values for val in self.values)
        return MultiValue(chain(*out))

    def __add__(self, other):
        match other:
            case MultiValue():
                return self.flatmap(lambda a: a + other)
            case _:
                return self.map(lambda a: a + other)

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return f'MultiValue({self.values})'

