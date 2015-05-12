import math

def is_triangular(n):
    """To tell whether n is a triangular number"""
    return (math.sqrt(n * 8 + 1) - 1) % 2 == 0
#the summation formula of arithmetic sequence is sum = (m + 1) * m / 2

def is_tetrahedral(n):
    """To tell whether n is a tetrahedral number"""
    m = 0
    f_m = 0
    while n - f_m > 0:
        m += 1
        f_m = (m ** 3 + 3 * m * m + 2 * m) / 6
        if f_m - n == 0
        return True
    return False
#the general formula of tetrahedral sequence is n = f(m) = (m^3 + 3 * m^2 + 2 * m) / 6

def is_pointy(n):
"""To tell whether n is a pointy number"""
    i = 1
    while i <= n / 2:
        if is_tetrahedral(i) and is_tetrahedral(n - i):
            return True
        i += 1
    return False
#From i = 1 to n / 2, test whether i and n - i are both tetrahedrals.

    
   
def is_square_piramidal(n):
    """To tell whether n is a tetrahedral number"""
    remainder = n
    subtractor_root = 0
    while remainder > 0:
        subtractor_root += 1
        remainder -= subtractor_root ** 2
    return remainder == 0
#n is subtracted by 1^2, 2^2, ... subtractor_root^2 until it is equal to or smaller than 0 (remainder <=0).
#If remainder == 0, then n is ansquare piramidal number.

def is_pentagonal(n):
    """To tell whether n is a pentagonal number"""
    return (math.sqrt(n * 24 + 1) + 1) % 6 == 0
#the general ofrmula of pentagonal sequence is n = (3 * m - 1) * m / 2

