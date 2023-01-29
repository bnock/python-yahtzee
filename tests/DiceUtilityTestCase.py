import unittest
from utilities import DiceUtility
from models.Die import Die


class DiceUtilityTestCase(unittest.TestCase):
    def test_sort_dice(self):
        dice = [
            Die(6),
            Die(1),
            Die(5),
            Die(2),
            Die(4),
        ]

        expected = [
            Die(1),
            Die(2),
            Die(4),
            Die(5),
            Die(6),
        ]

        actual = DiceUtility.sort_dice(dice)
        self.assertEqual(expected, actual)

    def test_occurrences(self):
        dice = [
            Die(1),
            Die(1),
            Die(2),
            Die(3),
            Die(5),
        ]

        expected = {
            1: 2,
            2: 1,
            3: 1,
            4: 0,
            5: 1,
            6: 0,
        }

        actual = DiceUtility.occurrences(dice)
        self.assertEqual(expected, actual)

    def test_total(self):
        dice = [
            Die(1),
            Die(6),
            Die(3),
            Die(5),
            Die(2),
        ]

        expected = 17
        actual = DiceUtility.total(dice)
        self.assertEqual(expected, actual)

    def test_is_straight(self):
        dice = [
            Die(1),
            Die(2),
            Die(3),
            Die(4),
            Die(5),
        ]

        self.assertTrue(DiceUtility.is_straight(dice, 5))

        dice = [
            Die(1),
            Die(2),
            Die(3),
            Die(5),
            Die(6),
        ]

        self.assertFalse(DiceUtility.is_straight(dice, 4))


if __name__ == 'main':
    unittest.main()
