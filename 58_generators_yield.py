"""Python generator functions are a powerful tool for creating iterators."""

"""A generator function is a special type of function that returns an iterator object. Instead of using return to send back a single value, generator functions use yield to produce a series of results over time. This allows the function to generate values and pause its execution after each yield, maintaining its state between iterations."""


def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt   # we can see how the value is returned from the function but the function is not terminated
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)


def func1():
    yield 1
    yield 2
    yield 3
    yield 4

val = func1()
print(list(val))


# or loop and return

for val1 in func1():
    print(val1)


# Python Generator Expression
## Generator expressions are a concise way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets and are more memory efficient.

sq = (x for x in range(5))
print(type(sq))
print(sq)
print(tuple(sq))


