from .ScoreComponent import ScoreComponent
from .Die import Die


class FoursScoreComponent(ScoreComponent):
    def __init__(self):
        super().__init__()
        self._name = 'Fours'

    def get_score(self, dice: list[Die]) -> int:
        score = 0
        for die in dice:
            if die.value == 4:
                score += 4
        return score
