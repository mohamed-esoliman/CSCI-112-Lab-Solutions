"""
Author: Mohamed Soliman
Project 1
File: numberguess.py

"""

import random


class NumberGuess:
    """Guesses a user's number."""

    def __init__(self, low, high):
        """The constructor function of the guesser."""
        self.low = low
        self.high = high
        self.counter = 0
        self.guess()

    def guess(self):
        """guesses a number in the low..high range."""
        self.value = random.randint(self.low, self.high)
        self.counter += 1

    def changeHigh(self):
        """adjusts the range to low..guess-1."""
        self.high = self.value - 1

    def changeLow(self):
        """adjusts the range to guess+1..high."""
        self.low = self.value + 1

    def getValue(self):
        """Returns the current guess."""
        return self.value

    def __str__(self):
        """Returns the string representation of the class."""
        return f"My guess is {self.value} for {self.counter} guess(es)."


def main():
    """A short tester function to exercise the number guesser methods."""
    guesser = NumberGuess(1, 100)
    print("first guess:", guesser)

    guesser.changeHigh()
    guesser.guess()
    print("guess if tooHigh:", guesser)

    guesser.changeLow()
    guesser.guess()
    print("guess if tooLow:", guesser)

    guesser.changeLow()
    guesser.guess()
    print("guess if tooLow:", guesser)

    guesser.changeHigh()
    guesser.guess()
    print("guess if tooHigh:", guesser)


# Entry point of the application.
if __name__ == "__main__":
    main()
