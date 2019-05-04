
import unittest
from ddt import ddt, data, unpack
from main.rule import evaluate



@ddt
class Test(unittest.TestCase):

    """
        A list of move counts
        evaluates to a deterministic result
    """
    @data(
        # When all move counts are equal, then all moves win
        ([1, 1, 1], [1, 1, 1]),
        ([3, 3, 3], [1, 1, 1]),

        # When only one move count is non-zero, then that move wins
        ([1, 0, 0], [1, 0, 0]),
        ([0, 1, 0], [0, 1, 0]),
        ([0, 0, 1], [0, 0, 1]),

        ([5, 0, 0], [1, 0, 0]),
        ([0, 5, 0], [0, 1, 0]),
        ([0, 0, 5], [0, 0, 1])


    )
    @unpack
    def testRule(self, mcs, result):
        self.assertEqual(evaluate(mcs), result)
