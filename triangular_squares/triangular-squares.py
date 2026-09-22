import sys

from math import sqrt, isqrt

# Please do not remove package declarations because these are used by the autograder. 
# If you need additional packages, then you may declare them above.


# Insert your triandsq(n) function here, along with any subroutines that you need.
# The function should return a list of triangular and square numbers under n.

def isTri(num: int) -> bool:
    total = 0
    for i in range(1, num + 1):
        total += i

        if total == num:
            return True

        if total > num: 
            return False

    return False

def isSq(num: int) -> bool:
    for i in range(1, num + 1):

        if i * i == num:
            return True
        
        if i * i > num:
            return False
    
    return False


def triandsq(n: int) -> list:

    listTriAndSq = []

    for i in range(1, n + 1):

        if isSq(i) == True and isTri(i) == True:
            listTriAndSq.append(i)

    return listTriAndSq

