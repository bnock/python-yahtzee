from random import randint
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap


class Die(QLabel):
    def __init__(self):
        """Constructor.
        """
        super().__init__()
        self._value = None

    def roll(self) -> None:
        """Roll the die and update its image.
        :return: None
        """
        self._value = randint(1, 6)

        match self._value:
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
                raise Exception(f'Invalid die number: {self.value}')

        self.setPixmap(QPixmap('images/' + image).scaledToWidth(100))

    @property
    def value(self) -> int:
        """Get the die's value.
        :return: int
        """
        return self._value
