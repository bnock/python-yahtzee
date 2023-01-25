from .ScoreComponent import ScoreComponent
from .Die import Die
from utilities import DiceUtility


class ThreeOfAKindScoreComponent(ScoreComponent):
    def __init__(self):
        super().__init__()
        self._name = '3 of a kind'

    def get_score(self, dice: list[Die]) -> int:
        for k, v in DiceUtility.occurrences(dice).items():
            if v >= 3:
                return DiceUtility.total(dice)

        return 0
