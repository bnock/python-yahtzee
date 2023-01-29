from random import randint
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from models.Die import Die as DieModel


class Die(QLabel):
    def __init__(self, die: DieModel):
        """Constructor.
        """
        super().__init__()
        self._die = die

    def roll(self) -> None:
        """Roll the die and update its image.
        :return: None
        """
        self._die.roll()
        self._update_image()

    def _update_image(self) -> None:
        """Update the die image.
        :return:
        """
        match self._die.value:
            case 1:
                image = 'one.jpeg'
            case 2:
                image = 'two.jpeg'
            case 3:
                image = 'three.jpeg'
            case 4:
                image = 'four.jpeg'
            case 5:
                image = 'five.jpeg'
            case 6:
                image = 'six.jpeg'
            case _:
                raise Exception(f'Invalid die number: {self._die.value}')

        self.setPixmap(QPixmap('images/' + image).scaledToWidth(100))

