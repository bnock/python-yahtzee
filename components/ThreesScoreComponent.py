from .ScoreComponent import ScoreComponent
from .Die import Die


class ThreesScoreComponent(ScoreComponent):
    def __init__(self):
        super().__init__()
        self._name = 'Threes'

    def get_score(self, dice: list[Die]) -> int:
        score = 0
        for die in dice:
            if die.value == 3:
                score += 3
        return score
