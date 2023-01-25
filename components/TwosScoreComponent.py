from .ScoreComponent import ScoreComponent
from .Die import Die


class TwosScoreComponent(ScoreComponent):
    def __init__(self):
        super().__init__()
        self._name = 'Twos'

    def get_score(self, dice: list[Die]) -> int:
        score = 0
        for die in dice:
            if die.value == 2:
                score += 2
        return score
