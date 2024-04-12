"""
Author: Mohamed Soliman
File: sorts.py

Defines the selection sort and the quick sort.
"""

from counter import Counter
from tools import getRandomList


def selectionSort(lyst, comps=None, swaps=None):
    """Sorts lyst with a selection sort."""

    n = len(lyst)

    # Can we just use the built-in min function?
    def getMinimumIndex(lyst, i, n, comps=None):
        """Return the index of the minimum item in lyst[i:n]."""
        minValue = lyst[i]
        minIndex = i
        for j in range(i + 1, n):
            if comps:
                comps.increment()
            if lyst[j] < minValue:
                minValue = lyst[j]
                minIndex = j
        return minIndex

    for i in range(n):
        minimumIndex = getMinimumIndex(lyst, i, n, comps)
        if comps:
            comps.increment()
        if minimumIndex != i:
            swap(lyst, i, minimumIndex, swaps)


def quickSort(lyst, comps=None, swaps=None):
    """Sorts lyst with a quick sort."""

    def recurse(left, right):
        if left < right:
            pivotPosition = partition(lyst, left, right)
            recurse(left, pivotPosition - 1)
            recurse(pivotPosition + 1, right)

    def partition(lyst, left, right):
        middle = (left + right) // 2
        pivot = lyst[middle]
        lyst[middle] = lyst[right]
        lyst[right] = pivot

        boundary = left

        for i in range(left, right):
            if comps:
                comps.increment()
            if lyst[i] < pivot:
                swap(lyst, i, boundary, swaps)
                boundary += 1

        swap(lyst, right, boundary, swaps)
        return boundary

    recurse(0, len(lyst) - 1)


def swap(lyst, i, j, counter=None):
    """Exchanges the items at i and j in lyst and increments
    the counter if it exists."""
    if counter:
        counter.increment()
    lyst[i], lyst[j] = lyst[j], lyst[i]


def test(sort, n=15):
    """Runs some tests on a sort function."""
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)


def testWithCounters(sort, n=15):
    """Runs some tests on a sort function."""
    comps = Counter()
    swaps = Counter()
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))
    comps.reset()
    swaps.reset()
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))


def main():
    """To test, pass the name of the sort function to test."""
    test(selectionSort)
    test(quickSort)
    testWithCounters(selectionSort)
    testWithCounters(quickSort)
    testWithCounters(selectionSort, n=150)
    testWithCounters(quickSort, n=150)


if __name__ == "__main__":
    main()
