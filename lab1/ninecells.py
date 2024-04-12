"""
Author: Mohamed Soliman
Project 1
File: ninecells.py

"""

from breezypythongui import EasyFrame


class NineCells(EasyFrame):
    """A 9*9 grid of labels"""

    def __init__(self):
        """The constructor function of the class"""

        EasyFrame.__init__(self)
        for i in range(3):
            for j in range(3):
                self.addLabel(text=f"({i}, {j})", row=i, column=j, sticky="NSEW")


def main():
    """The starting point for launching the program."""
    NineCells().mainloop()


# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
