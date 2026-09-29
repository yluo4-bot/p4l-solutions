from random import random # this should be helpful!

# Write your simulate_one_birthday_trial() function here along with any subroutines that you need
def simulate_one_birthday_trial(num_people: int) -> bool:
    """
    Simulate one trial of the birthday game with num_people people.

    Parameters:
    - num_people (int): the number of people in the group

    Returns:
    bool: True if there is a collision, False otherwise
    """

    lstBD = []

    for i in range(num_people):
        lstBD.append(int(random() * 365 + 1))

    return has_repeat(lstBD)

def has_repeat(a: list[int]) -> bool:
    dictNum = {}

    for i in a:

        if i in dictNum:
            dictNum[i] += 1

        else:
            dictNum[i] = 1

    for i in dictNum:
        
        if dictNum[i] > 1:
            return True

    return False
