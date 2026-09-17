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
