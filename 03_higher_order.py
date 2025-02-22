from functools import partial

def compose2(first_fn, second_fn):
    def composed(val):
        return second_fn(first_fn(val))
    return composed

def inc(x):
    return x + 1

def dbl(x):
    return 2 * x


def cat(filename):
    with open(filename) as f:
        return f.read()

def grep(text, keyword):
    return "\n".join(line for line in text.split("\n") if keyword in line)

def wc(text, count_lines=False):
    if count_lines:
        return len(text.split("\n"))
    else:
        return len(text.split())


