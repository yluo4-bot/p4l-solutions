from random import gauss # this should be helpful!

# Write your add_noise() function here along with any subroutines that you need.
def add_noise(polling_value: float, margin_of_error: float) -> float:
    """
    Add noise to a polling value.

    Simulates polling data by introducing random noise to the provided polling value.
    The noise is generated from a normal distribution with a mean of 0 and a standard
    deviation equal to half the specified margin of error.

    Parameters:
    - polling_value (float): The original polling value.
    - margin_of_error (float): The margin of error for the polling value.

    Returns:
    float: The polling value with added noise.
    """

    if margin_of_error < 0 or not 0 <= polling_value <=1:
        raise ValueError("Invalid polling value or margin of error.")

    length = 0.5 * margin_of_error

    x = gauss(0, length)

    return (polling_value + x)

# Write your simulate_one_election() function here along with any subroutines that you need.
def simulate_one_election(polls: dict[str, float],
    electoral_votes: dict[str, int],
    margin_of_error: float
) -> tuple[int, int]:    
    """
    Simulate one election.

    Parameters:
    - polls (dict): A dictionary mapping states to polling percentages.
    - electoral_votes (dict): A dictionary mapping states to electoral votes.
    - margin_of_error (float): The margin of error for the polling data.

    Returns:
    tuple: A tuple of two ints representing the number of electoral votes won by candidate 1 and candidate 2.
    """

    votes1 = 0
    votes2 = 0

    for states in polls:
        adjustedPoll = add_noise(polls[states], margin_of_error)

        if adjustedPoll >= 0.5:
            votes1 += electoral_votes[states]

        else: 
            votes2 += electoral_votes[states]

    return votes1, votes2

# Write your simulate_multiple_elections() function here along with any subroutines that you need.
def simulate_multiple_elections(
    polls: dict[str, float],
    electoral_votes: dict[str, int],
    num_trials: int,
    margin_of_error: float
) -> tuple[float, float, float]:   
    """
    Simulate multiple elections.

    Parameters:
    - polls (dict): A dictionary mapping states to polling percentages.
    - electoral_votes (dict): A dictionary mapping states to electoral votes.
    - num_trials (int): The number of simulated elections to run.
    - margin_of_error (float): The margin of error for the polling data.

    Returns:
    tuple: A tuple of three floats representing the probabilities that candidate 1 wins, candidate 2 wins, and that
           the election is a tie.
    """

    winCount1 = 0
    winCount2 = 0
    tieCount = 0

    for trial in range(num_trials):
        vote1, vote2 = simulate_one_election(polls, electoral_votes, margin_of_error)

        if vote1 > vote2:
            winCount1 += 1

        elif vote1 < vote2:
            winCount2 += 1

        else:
            tieCount += 1

    return (float(winCount1) / num_trials, float(winCount2) / num_trials, float(tieCount) / num_trials)
