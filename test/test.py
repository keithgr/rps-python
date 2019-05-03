
import unittest
from main import rule



class Test(unittest.TestCase):

    def testRule(self):
        # When all move counts are equal, then all moves win
        self.assertEqual(rule.evaluate([1, 1, 1]), [1, 1, 1])
        self.assertEqual(rule.evaluate([3, 3, 3]), [1, 1, 1])

        # When only one move is present, player always wins
        self.assertEqual(rule.evaluate([1, 0, 0]), [1, 0, 0])
        self.assertEqual(rule.evaluate([0, 1, 0]), [0, 1, 0])
        self.assertEqual(rule.evaluate([0, 0, 1]), [0, 0, 1])
        self.assertEqual(rule.evaluate([5, 0, 0]), [1, 0, 0])
        self.assertEqual(rule.evaluate([0, 5, 0]), [0, 1, 0])
        self.assertEqual(rule.evaluate([0, 0, 5]), [0, 0, 1])


