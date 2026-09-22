from random import random # this should be helpful!

def simulate_state_once(poll: float, margin_of_error: float) -> bool:
    """
    Decide the winner of one state by adding random noise to the polling result.

    Parameters:
        poll (float): Candidate 1’s polling share in the state, between 0 and 1.
        margin_of_error (float): Non-negative margin of error.

    Returns:
        bool: True if candidate 1 wins the state (adjusted poll ≥ 0.5),
              otherwise False.
    """

    randFloat = random() * margin_of_error * 2 - margin_of_error

    return ((poll + randFloat) >= 0.5)
