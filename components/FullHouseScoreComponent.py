from .ScoreComponent import ScoreComponent
from .Die import Die
from utilities import DiceUtility


class FullHouseScoreComponent(ScoreComponent):
    def __init__(self):
        super().__init__()
        self._name = 'Full House'

    def get_score(self, dice: list[Die]) -> int:
        occurrences = DiceUtility.occurrences(dice)
        for k, v in occurrences.items():
            if v == 3:
                for j, x in occurrences.items():
                    if k != j and x == 2:
                        return 25

        return 0
