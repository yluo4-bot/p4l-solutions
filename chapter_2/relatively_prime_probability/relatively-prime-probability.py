from random import random # this should be helpful!

# Write your relatively_prime_probability() function here along with any subroutines that you need
# Hint: include your relatively_prime() function and any subroutines that it calls.
def relatively_prime_probability(
    lower_bound: int,
    upper_bound: int,
    num_pairs: int
) -> float:    
    """
    Compute the probability that two randomly chosen integers in the range [lower_bound, upper_bound] are
    relatively prime.

    Parameters:
    - lower_bound (int): the lower bound of the range
    - upper_bound (int): the upper bound of the range
    - num_pairs (int): the number of pairs to trial

    Returns:
    float: the probability that two randomly chosen integers in the range [lower_bound, upper_bound] are
    relatively prime
    """

    ran = upper_bound - lower_bound + 1
    count = 0

    for i in range(num_pairs):
        a = int(random() * ran + lower_bound)
        b = int(random() * ran + lower_bound)

        if relatively_prime(a, b) == True:
            count += 1

    return float(count) / num_pairs


def euclid_gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Write your improved relatively_prime() function here. Use euclid_gcd!
def relatively_prime(a: int, b: int) -> bool:
    if euclid_gcd(a, b) == 1:
        return True

    return False
