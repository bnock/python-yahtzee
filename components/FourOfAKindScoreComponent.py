from .ScoreComponent import ScoreComponent
from .Die import Die
from utilities import DiceUtility


class FourOfAKindScoreComponent(ScoreComponent):
    def __init__(self):
        super().__init__()
        self._name = '4 of a kind'

    def get_score(self, dice: list[Die]) -> int:
        for k, v in DiceUtility.occurrences(dice).items():
            if v >= 4:
                return DiceUtility.total(dice)

        return 0
