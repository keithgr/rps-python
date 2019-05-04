
import unittest
from ddt import ddt, data, unpack
from main.rule import evaluate



@ddt
class Test(unittest.TestCase):

    """
        A list of move counts
        evaluates to a deterministic result
        ([ROCKS, PAPERS, SCISSORS], [ROCK_WIN, PAPER_WIN, SCISSORS_WIN]),
    """
    @data(
        # When all move counts are equal,
        # then all moves win
        ([1, 1, 1], [1, 1, 1]),
        ([3, 3, 3], [1, 1, 1]),

        # When precisely two move counts are equally small,
        # then the more frequent move wins
        ([1, 0, 0], [1, 0, 0]),
        ([0, 1, 0], [0, 1, 0]),
        ([0, 0, 1], [0, 0, 1]),

        ([5, 0, 0], [1, 0, 0]),
        ([0, 5, 0], [0, 1, 0]),
        ([0, 0, 5], [0, 0, 1]),

        ([5, 4, 4], [1, 0, 0]),
        ([4, 5, 4], [0, 1, 0]),
        ([4, 4, 5], [0, 0, 1]),

        # When only one move count is strictly least,
        # then the superior move (based on 2-player RPS), among the two most frequent moves, wins
        ([1, 1, 0], [0, 1, 0]),
        ([1, 2, 0], [0, 1, 0]),
        ([2, 1, 0], [0, 1, 0]),

        ([8, 8, 3], [0, 1, 0]),
        ([5, 8, 3], [0, 1, 0]),
        ([8, 5, 3], [0, 1, 0]),

        ([1, 0, 1], [1, 0, 0]),
        ([1, 0, 2], [1, 0, 0]),
        ([2, 0, 1], [1, 0, 0]),

        ([8, 3, 8], [1, 0, 0]),
        ([5, 3, 8], [1, 0, 0]),
        ([8, 3, 5], [1, 0, 0]),

        ([0, 1, 1], [0, 0, 1]),
        ([0, 1, 2], [0, 0, 1]),
        ([0, 2, 1], [0, 0, 1]),

        ([3, 8, 8], [0, 0, 1]),
        ([3, 5, 8], [0, 0, 1]),
        ([3, 8, 5], [0, 0, 1])
    )
    @unpack
    def testRule(self, mcs, result):
        self.assertEqual(result, evaluate(mcs))
