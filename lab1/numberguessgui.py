"""
Author: Mohamed Soliman
Project 1
File: numberguessgui.py

"""


from breezypythongui import EasyFrame


class NumberGuessGUI(EasyFrame):
    """view of the guessing program"""

    def __init__(self, guesser):
        """The construcor method of the view"""

        EasyFrame.__init__(self, title="Number Guessing Game")

        self.guesser = guesser

        self.main_label = self.addLabel(
            text=str(self.guesser),
            row=0,
            column=0,
            sticky="NSEW",
            columnspan=3,
        )

        self.addButton(text="Too Low", row=1, column=0, command=self.toolow)
        self.addButton(text="Too High", row=1, column=1, command=self.toohigh)
        self.addButton(text="Correct", row=1, column=2, command=self.correct)

    def toolow(self):
        self.guesser.changeLow()
        self.guesser.guess()
        self.main_label["text"] = str(self.guesser)

    def toohigh(self):
        self.guesser.changeHigh()
        self.guesser.guess()
        self.main_label["text"] = str(self.guesser)

    def correct(self):
        self.messageBox(
            title="Game Over",
            message=f"I won!\n{str(self.guesser)}",
        )
        self.quit()
