from typing import Optional
from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout
from .Die import Die


class ScoreComponent(ABC, QHBoxLayout):
    def __init__(self):
        super().__init__()
        self._label: Optional[QLabel] = None
        self._input: Optional[QLineEdit] = None
        self._button: Optional[QPushButton] = None
        self._is_scored: bool = False
        self._name: Optional[str] = None

    def set_active(self, is_active: bool) -> None:
        """Set the active status of this component. Ignored if component has been scored.
        :param is_active: bool
        :return: None
        """
        if not self._is_scored:
            if self._label is not None:
                self._label.setDisabled(not is_active)
            if self._button is not None:
                self._button.setDisabled(not is_active)

    def initialize_gui(self) -> None:
        """Initialize the GUI for this component
        :return: None
        """
        self._label = QLabel((self._name + ':') if self._name else '')
        self._label.setDisabled(True)
        self._input = QLineEdit()
        self._input.setDisabled(True)
        self._button = QPushButton('Apply')

        self.addWidget(self._label)
        self.addWidget(self._input)
        self.addWidget(self._button)

    @abstractmethod
    def get_score(self, dice: list[Die]) -> int:
        """Get the score for this component from the provided dice.
        :param dice: list[Die]
        :return: int
        """
        pass
