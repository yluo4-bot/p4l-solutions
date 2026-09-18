import math
from random import random # this should be helpful!

# Write your sum_dice() function here along with any subroutines that you need.
def sum_two_dice() -> int:
    return (int(random() * 6 + 1) + int(random() * 6 + 1))

def countSteps() -> int:

    first = sum_two_dice()

    if first in (7, 11):
      return 1
    
    elif first in (2, 3, 12):
      return 1

    else: 
      result = 0
      count = 1
      while result >= 0:

        result = sum_two_dice()
        count += 1

        if result == 7:
          return count

        if result == first:
          return count

def average_game_length(num_trials: int) -> float:
    """
    Simulate num_trials games of craps and estimate the average number 
    of dice rolls per game.

    Parameters:
        num_trials (int): The number of games to simulate.

    Returns:
        float: The estimated average number of dice rolls per game.
    """

    total = 0

    for i in range(num_trials):
        total += countSteps()

    return float(total) / num_trials
