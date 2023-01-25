from .ScoreComponent import ScoreComponent
from .Die import Die


class FivesScoreComponent(ScoreComponent):
    def __init__(self):
        super().__init__()
        self._name = 'Fives'

    def get_score(self, dice: list[Die]) -> int:
        score = 0
        for die in dice:
            if die.value == 5:
                score += 5
        return score
