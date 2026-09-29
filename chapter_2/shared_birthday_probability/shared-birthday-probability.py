import random # this should be helpful!

# Write your shared_birthday_probability() function here along with any subroutines that you need
def shared_birthday_probability(num_people: int, num_trials: int) -> float:
    """
    Compute the probability that two people in a group of num_people have the same birthday, after running
    num_trials trials.

    Parameters:
    - num_people (int): the number of people in the group
    - num_trials (int): the number of trials to run

    Returns:
    float: the average probability that two people in a group of num_people have the same birthday
    """

    count = 0

    for i in range(num_trials):
        if simulate_one_birthday_trial(num_people) == True:
            count += 1

    return float(count) / num_trials

def simulate_one_birthday_trial(num_people: int) -> bool:
    lstBD = []

    for i in range(num_people):
        lstBD.append(int(random.random() * 365 + 1))

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
