
class Rule:

    @staticmethod
    def evaluate(mcs):
        if mcs[0] < mcs[1]:
            if mcs[0] < mcs[2]:
                return [0, 0, 1]
            else:
                return [0, 1, 0]
        elif mcs[0] > mcs[1]:
            if mcs[1] <= mcs[2]:
                return [1, 0, 0]
            else:
                [0, 1, 0]
        else:
            if mcs[0] < mcs[2]:
                return [0, 0, 1]
            elif mcs[0] > mcs[2]:
                return [0, 1, 0]
            else:
                return [1, 1, 1]
