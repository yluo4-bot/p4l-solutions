# Insert your list_mersenne_primes() function here, along with any subroutines that you need.
def power(p, m) -> int:
    
    result = 1

    for i in range(m):
        result *= p
    
    return result

def isPrime(p) -> bool:

    if p == 0 or p == 1:
        return False

    for i in range(2, int(p ** 0.5) + 1):
        
        if p % i == 0:
            return False

    return True

def list_mersenne_primes(n: int) -> list[int]:
    """
    List all Mersenne primes of the form 2^p - 1 with p ≤ n.
    Args:
        n: Upper bound on the exponent p (non-negative integer).
    Returns:
        A list of all primes of the form 2^p - 1 where p is prime and p ≤ n,
        in increasing order of p.
    """

    listMers = []

    for i in range(n + 1):
        
        primeCandidate = power (2, i) - 1

        if isPrime(primeCandidate) == True:
            listMers.append(primeCandidate)

    return listMers
