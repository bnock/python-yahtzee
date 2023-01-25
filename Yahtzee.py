from components.Die import Die
from PyQt6.QtWidgets import QApplication

from components.MainWindow import MainWindow


class Yahtzee:
    def __init__(self):
        """Constructor.
        """
        self._window = None
        self._app = None
        self._dice = []

        self._initialize_gui()

    def run(self) -> None:
        """Run the game.
        :return: None
        """
        self._initialize_dice()
        self._window.show()
        self._app.exec()

    def _initialize_dice(self) -> None:
        """Initialize the dice.
        :return: None
        """
        for i in range(5):
            self._dice.append(Die())

    def _initialize_gui(self) -> None:
        """Initialize the GUI.
        :return: None
        """
        self._app = QApplication([])
        self._window = MainWindow('Yahtzee')

    def _roll(self) -> None:
        """Roll the dice.
        :return: None
        """
        for die in self._dice:
            die.roll()
