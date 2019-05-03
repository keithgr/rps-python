
import math

""" Max player count """
N = 10

""" 
    Initialize results array 
    Row reps number of agents
    Column reps number of enemies 
"""
results = N * [N * [-1]]

#print(results)

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
        for r in range(0, math.floor(a / 3) + 1):
            for p in range(r, a - 2 * r + 1):
                s = a - r - p

                #print('{}\t{}-{}-{}'.format(a, r, p, s));
