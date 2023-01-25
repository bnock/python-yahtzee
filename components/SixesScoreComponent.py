from .ScoreComponent import ScoreComponent
from .Die import Die


class SixesScoreComponent(ScoreComponent):
    def __init__(self):
        super().__init__()
        self._name = 'Sixes'

    def get_score(self, dice: list[Die]) -> int:
        score = 0
        for die in dice:
            if die.value == 6:
                score += 6
        return score
