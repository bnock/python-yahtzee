from models.Die import Die


def sort_dice(dice: list[Die], reverse: bool = False) -> list[Die]:
    """Sort a list of dice.  Returns a new list and does not modify the original.
    :param dice: list[Die]
    :param reverse: bool
    :return: list[Die]
    """
    sorted_dice = dice.copy()
    sorted_dice.sort(key=lambda die: die.value, reverse=reverse)

    return sorted_dice


def occurrences(dice: list[Die]) -> dict[int, int]:
    """Count the occurrences of each value (1-6) in the dice.
    :param dice: list[Die]
    :return: dict[int, int]
    """
    result = {}
    for i in range(1, 7):
        result[i] = 0

    for die in dice:
        result[die.value] += 1
    return result


def total(dice: list[Die]) -> int:
    """Get the total of the dice.
    :param dice: list[Die]
    :return: int
    """
    result = 0
    for die in dice:
        result += die.value
    return result


def is_straight(dice: list[Die], min_required: int) -> bool:
    """Is this set of dice a straight?  Minimum dice count must be a part of the straight.
    :param dice: list[Die]
    :param min_required: int
    :return: bool
    """
    sorted_dice = sort_dice(dice)
    last_die = None
    longest = 1
    straight = 1

    for idx, die in enumerate(sorted_dice):
        if idx == 0:
            last_die = die.value
            continue

        if die.value == last_die + 1:
            straight += 1
            if straight > longest:
                longest = straight
        else:
            straight = 1

        last_die = die.value

    return longest >= min_required
