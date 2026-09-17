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
        poll = polls[states]
        adjustedPoll = add_noise(poll, margin_of_error)

        if adjustedPoll >= 0.5:
            votes1 += electoral_votes[states]

        else: 
            votes2 += electoral_votes[states]

    return votes1, votes2
