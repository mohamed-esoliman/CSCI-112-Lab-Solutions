from my_priorityQueue import PriorityQueue as PQ1
from my_priorityQueue2 import PriorityQueue as PQ2
from time import time
from random import shuffle


def testPQ(n):
    """Compare the speed of the two priority queue classes."""
    lyst = list(range(n))
    shuffle(lyst)

    start = time()
    pq1 = PQ1(lyst)
    print(
        f"PQ1 took {round(time() - start, 5)} seconds to add {len(lyst)} shuffled items."
    )

    start = time()
    pq2 = PQ2(lyst)
    print(
        f"PQ2 took {round(time() - start, 5)} seconds to add {len(lyst)} shuffled items."
    )
    print("-" * 50)


def main():
    """Tests the priority queue classes."""
    testPQ(1000)
    testPQ(3000)
    testPQ(5000)
    testPQ(10000)
    testPQ(15000)
    testPQ(20000)


if __name__ == "__main__":
    main()
