import numpy as np

# There are 36 results from 2d6
results = np.array([max([x,y]) for x in range(1,7) for y in range(1,7)])

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
print(f"\nThe odds of 7 or more on 1 roll with no bonus are roughly {odds_maker(results, 7):.2%}")

# ...10
print(f"\nThe odds of 10 or more on 1 roll with no bonus are roughly {odds_maker(results, 10):.2%}")

# After that, you'll need a bonus to get somewhere.

# Let's calculate the odds of a an inescapable tie
# That's a roll where both rolled dice equal the Course
# Each die has a 1 in 6 chance of doing that so...
inesc_tie = (1/6)**2
print(f"\nThe odds of an inescapable tie are {inesc_tie:.2%}")

# Now an available tie. That is, the odds that at least one of the rolled
# dice match the Course. Here it's easier to determine the odds neither
# rolled die matches the course and subtract that from 1. So...
avail_tie = 1-(5/6)**2
print(f"\nThe odds of an available tie are {avail_tie:.2%}")

# If we assume the Course is showing a value greater than your skill
# then the odds of an available tie are the odds of a useful tie.
# So if your fellow players are feeding you good Course dice, you're
# all set.

# If the Course die is random, then things change.
print("\nOdds of a useful tie if the Course is random and...")
for n in range(6):
    print(f"...your skill is +{n} are {(6-n)*avail_tie/6:.2%}")

print()
