import random
import unittest

class Die:

    def __init__(self, count):
        self.__count = count
        # assume 6-sided dice
        self.__sides = 6

    def get_count(self):
        return self.__count

    def get_sides(self):
        return self.__sides

    def roll_die(self):
        total = 0
        for x in range(0, self.__count):
            total += self.__roll_dice()
        return total

    def __roll_dice(self):
        # assume the numbers on the dice are 1 to __sides
        return random.randrange(1, 1 + self.__sides)


class TestDie(unittest.TestCase):

    # def setUp(self):
    #     die = Die(1)

    def test_roll_die(self):
        for x in range(1, 10):
            die = Die(x)
            for y in range(0, 100):
                roll = die.roll_die()
                self.assertLessEqual(roll, (x * die.get_sides()), "%s was rolled" % roll)
                self.assertGreaterEqual(roll, (x - 1), "%s was rolled" % roll)

    # def rolls(n, roll_stats):
    #     for x in range(0, n):
    #         rollx = roll()
    #         roll_stats[rollx] += 1
    #     return sorted(roll_stats.items(), key=operator.itemgetter(0))
    #
    # roll_stats = {
    #     2: 0,
    #     3: 0,
    #     4: 0,
    #     5: 0,
    #     6: 0,
    #     7: 0,
    #     8: 0,
    #     9: 0,
    #     10: 0,
    #     11: 0,
    #     12: 0,
    # }
    #
    # class Craps:
    #     __roll_stats = {
    #         2: 0,
    #         3: 0,
    #         4: 0,
    #         5: 0,
    #         6: 0,
    #         7: 0,
    #         8: 0,
    #         9: 0,
    #         10: 0,
    #         11: 0,
    #         12: 0,
    #     }
    #
    # print(roll())
    # roll_stats = rolls(10000, roll_stats)
    # for x in range(0, 11):
    #     print(roll_stats[x])
    #
    # print("hello there".capitalize())
    # print("hello there".upper())
    # print("hellO there".lower())
    #
    # test_file = open("test.txt", "wb")
    # print(test_file.mode)
    # print(test_file.name)
    # test_file.write(bytes("wrong text to a file\n", 'UTF-8'))
    #
    # test_file.close()
    #
    # test_file = open('test.txt', 'r+')
    # print(test_file.read())
    # test_file.close()