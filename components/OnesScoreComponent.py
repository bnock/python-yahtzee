from .ScoreComponent import ScoreComponent
from .Die import Die


class OnesScoreComponent(ScoreComponent):
    def __init__(self):
        super().__init__()
        self._name = 'Ones'

    def get_score(self, dice: list[Die]) -> int:
        score = 0
        for die in dice:
            if die.value == 1:
                score += 1
        return score
