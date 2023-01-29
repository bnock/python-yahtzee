from random import randint


class Die:
    def __init__(self, value: int  = None):
        self._value = value

    @property
    def value(self) -> int:
        """Get the die's value.
        :return: int
        """
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        """Set the die's value.
        :param value: int
        :return: None
        """
        if value < 1 or value > 6:
            raise ValueError('Die value must be between 1 and 6')
        self._value = value

    def roll(self) -> None:
        """Roll the die and update its image.
        :return: None
        """
        self._value = randint(1, 6)

    def __eq__(self, other):
        return self._value == other.value
