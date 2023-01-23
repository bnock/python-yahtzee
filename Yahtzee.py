from components.Die import Die
from PyQt6.QtWidgets import QApplication

from components.MainWindow import MainWindow


class Yahtzee:
    def __init__(self):
        """Constructor.
        """
        self.window = None
        self.app = None
        self.dice = []

        self.initialize_gui()

    def initialize_dice(self) -> None:
        """Initialize the dice.
        :return: None
        """
        self.dice = []
        for i in range(5):
            self.dice.append(Die())

    def roll(self) -> None:
        """Roll the dice.
        :return: None
        """
        for die in self.dice:
            die.roll()

    def initialize_gui(self) -> None:
        """Initialize the GUI.
        :return: None
        """
        self.app = QApplication([])
        self.window = MainWindow('Yahtzee')

    def run(self) -> None:
        """Run the game.
        :return: None
        """
        self.window.show()
        self.app.exec()
