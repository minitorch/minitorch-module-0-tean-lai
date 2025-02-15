"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a: float, b: float):
    return a * b


def id(a: float):
    return a


def add(a: float, b: float):
    return a + b


def neg(a: float):
    return -a


def lt(a: float, b: float):
    return a < b


def eq(a: float, b: float):
    return a == b


def max(a: float, b: float):
    if a > b:
        return a
    return b


def is_close(a: float, b: float):
    return abs(a - b) < 1e-2


def sigmoid(x: float):
    if x >= 0.0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return (math.exp(x)) / (1.0 + math.exp(x))


def relu(x: float):
    if x < 0.0:
        return 0.0
    return x


def log(x: float):
    return math.log(x)


def exp(x: float):
    return math.exp(x)


def inv(x: float):
    return 1.0 / x


def log_back(x: float, y: float):
    return y / x


def inv_back(x: float, y: float):
    return -y / (x * x)


def relu_back(x: float, y: float):
    return y if x > 0.0 else 0.0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(f: Callable, seq: Iterable):
    for i in seq:
        yield f(i)


def zipWith(f: Callable, seq1: Iterable, seq2: Iterable):
    for x, y in zip(seq1, seq2):
        yield f(x, y)


def reduce(f: Callable[[float, float], float], seq: Iterable[float]) -> float:
    acc = None
    for i in seq:
        if acc is None:
            acc = i
        else:
            acc = f(i, acc)
    if acc is None:
        return 0.0
    return acc


def negList(l: list[float]):
    return map(neg, l)


def addLists(l1: list[float], l2: list[float]):
    return zipWith(add, l1, l2)


def sum(l: list[float]):
    return reduce(add, l)


def prod(l: list[float]) -> float:
    return reduce(mul, l)
