"""
Author: Mohamed Soliman
File: fibs.py

Two versions of the functions to compute the nth Fibonacci number.
"""

from counter import Counter


def fib1(n, counter=None):
    """The standard recursive version."""
    if counter:
        counter.increment()
    return 1 if n <= 2 else fib1(n - 1, counter) + fib1(n - 2, counter)


def fib2(n, counter=None):
    """The recursive version with a memoizing cache."""
    return fib2_helper(n, {}, counter)


def fib2_helper(n, fib_dict, counter=None):
    if counter:
        counter.increment()

    if n <= 2:
        return 1
    elif n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fib2_helper(n - 1, fib_dict, counter) + fib2_helper(
            n - 2, fib_dict, counter
        )
        return fib_dict[n]


def test(fib):
    """Runs some tests on a fib function."""
    for n in range(20, 24):
        print("n:", n, "fib(n):", fib(n))


def testWithCounter(fib):
    """Runs some tests on a fib function."""
    counter = Counter()
    for n in range(1, 10):
        counter.reset()
        print("n:", n, "fib(n):", fib(n, counter), " Number of calls:", str(counter))


def main():
    """To test, pass the name of the fib function to test."""
    test(fib1)
    test(fib2)

    testWithCounter(fib1)
    testWithCounter(fib2)


if __name__ == "__main__":
    main()
