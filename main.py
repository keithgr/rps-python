
import math

""" Max player count """
N = 10

""" 
    Initialize results array 
    Row reps number of agents
    Column reps number of enemies
"""
results = N * [N * [-1]]

""" Rule """
def rule(mcs):
    if mcs[0] < mcs[1]:
        if mcs[0] < mcs[2]: return [0, 0, 1]
        else: return [0, 1, 0]
    elif mcs[0] > mcs[1]:
        if mcs[1] <= mcs[2]: return [1, 0, 0]
        else: [0, 1, 0]
    else:
        if mcs[0] < mcs[2]: return [0, 0, 1]
        elif mcs[0] > mcs[2]: return [0, 1, 0]
        else: return [1, 1, 1]



""" For each player count """
for n in range(1, N + 1):

    """ For each agent count """
    for a in range(1, n + 1):
        # Enemy count
        e = n - a

        """
            For each agent strategy 
            WLOG, rock is the least frequent move
        """
        for ra in range(0, math.floor(a / 3) + 1):
            for pa in range(ra, a - 2 * ra + 1):
                s = a - ra - pa

                """ For each enemy configuration """
                for re in range(0, e + 1):
                    for pe in range(0, e - re + 1):
                        se = e - re - pe


