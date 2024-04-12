from linkedlist import LinkedList
from random import randrange
from sorts import quickSort
from time import time
import csv

dataFile = open("lab8Data.csv", "w")
writer = csv.writer(dataFile)
writer.writerow(["n", "bucketSort", "quickSort"])
dataFile.close()


def randints(n):
    """Return a list of n random integers."""
    return [randrange(n - 1) for _ in range(n)]


def bucketSort(lyst):
    """Sort lyst using the bucket sort algorithm."""
    buckets = [LinkedList() for _ in range(len(lyst) + 1)]

    for i in lyst:
        buckets[i].add(i)

    sortedLyst = []
    for bucket in buckets:
        sortedLyst.extend(bucket)

    return sortedLyst


def testSpeed(n):
    """Test the speed of the sorting using bucket sort and quick sort."""
    lyst1 = randints(n)
    lyst2 = lyst1.copy()
    print(f"Unsorted list of {n} integers.")
    print()
    print("Sorting the list using bucket sort:")
    start = time()
    lyst1 = bucketSort(lyst1)
    timeTaken1 = time() - start
    print(f"It took {round(timeTaken1, 5)} seconds to sort the list using bucket sort.")
    print("-" * 10)
    print("Sorting the list using quick sort:")
    start = time()
    quickSort(lyst2)
    timeTaken2 = time() - start
    print(f"It took {round(timeTaken2, 5)} seconds to sort the list using bucket sort.")
    print("-" * 50)
    print()
    print()
    dataLyst = [n, timeTaken1, timeTaken2]
    with open("lab8Data.csv", "a") as dataFile:
        writer = csv.writer(dataFile)
        writer.writerow(dataLyst)


def main():
    """Test with random integers."""
    print("Sorting a simple list using bucket sort:")
    simpleLyst = [3, 5, 2, 1, 4, 10, 6, 9, 8, 7]
    print("Unsorted:", simpleLyst)
    print("Sorted:", bucketSort(simpleLyst))
    print()

    print("Sorting a list of 20 random integers using bucket sort:")
    lyst = randints(20)
    print("Unsorted:", lyst)
    print("Sorted:", bucketSort(lyst))
    print()
    print()
    print()
    print("*" * 50)
    print()

    print("Comparing the speed of bucket sort and quick sort:")
    print()
    testSpeed(1000)
    testSpeed(10000)
    testSpeed(50000)
    testSpeed(100000)
    testSpeed(150000)
    testSpeed(200000)
    testSpeed(400000)
    testSpeed(600000)
    testSpeed(800000)
    testSpeed(1000000)
    testSpeed(1500000)
    testSpeed(2000000)
    testSpeed(2500000)
    testSpeed(3000000)
    print("*" * 50)
    print("Data saved to lab8Data.csv.")


if __name__ == "__main__":
    main()
