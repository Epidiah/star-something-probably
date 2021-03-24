import numpy as np

# There are 36 results from 2d6
results = np.array([max([x,y]) for x in range(1,7) for y in range(1,7)])
print(f"{len(results)=}\n\n{results}")

# There's roughly a 1 in 6 odds of the shared die being each value
# This isn't 100% true since it's not entirely random, but true enough
# for our purposes.

def odds_maker(results, threshold, bonus=0):
    total_odds = 0
    for n in range(1,7):
        current_odds = sum(results+n+bonus >= threshold)/(6**3)
        total_odds += current_odds
    return total_odds

# With no bonus, thresholds of 7 and 10 are achieveable.
# ...7
print(f"7 or more on 1 roll is roughly {odds_maker(results, 7)}")

# ...10
print(f"10 or more on 1 roll is roughly {odds_maker(results, 10)}")

# After that, you'll need a bonus to get somewhere.
