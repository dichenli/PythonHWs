import unittest
from figurate_numbers import *

class TestNumberPersonalities(unittest.TestCase):

    def tell_about(self, fun, n, should_be):
        if fun(n) == should_be:
            return
        if should_be:
            print str(n) + " should be " + fun.__name__[3:]
        else:
            print str(n) + " should not be " + fun.__name__[3:]
        
    def test_is_prime(self):
        self.assertEquals(2 + 2, 4)
        self.tell_about(is_prime, 1, False)
        self.tell_about(is_prime, 2, True)
        self.tell_about(is_prime, 3, True)
        self.tell_about(is_prime, 4, False)
        self.tell_about(is_prime, 5, True)
        self.tell_about(is_prime, 6, False)
        self.tell_about(is_prime, 99, False)
        self.tell_about(is_prime, 97, True)
        self.tell_about(is_prime, 169, False)
        self.tell_about(is_prime, 991, True)
        self.tell_about(is_prime, 1000, False)

    def test_is_triangular(self):
        self.tell_about(is_triangular, 1, True)
        self.tell_about(is_triangular, 2, False)
        self.tell_about(is_triangular, 3, True)
        self.tell_about(is_triangular, 5, False)
        self.tell_about(is_triangular, 6, True)
        self.tell_about(is_triangular, 21, True)
        self.tell_about(is_triangular, 30, False)
        self.tell_about(is_triangular, 55, True)
        self.tell_about(is_triangular, 990, True)
        self.tell_about(is_triangular, 1000, False)

    def test_is_square(self):
        self.tell_about(is_square, 1, True)
        self.tell_about(is_square, 2, False)
        self.tell_about(is_square, 4, True)
        self.tell_about(is_square, 8, False)
        self.tell_about(is_square, 49, True)
        self.tell_about(is_square, 99, False)
        self.tell_about(is_square, 100, True)
        self.tell_about(is_square, 121, True)
        self.tell_about(is_square, 10000, True)
        self.tell_about(is_square, 10001, False)

    def test_is_tetrahedral(self):
        self.tell_about(is_tetrahedral, 1, True)
        self.tell_about(is_tetrahedral, 2, False)
        self.tell_about(is_tetrahedral, 3, False)
        self.tell_about(is_tetrahedral, 4, True)
        self.tell_about(is_tetrahedral, 5, False)
        self.tell_about(is_tetrahedral, 10, True)
        self.tell_about(is_tetrahedral, 20, True)
        self.tell_about(is_tetrahedral, 35, True)
        self.tell_about(is_tetrahedral, 52, False)
        self.tell_about(is_tetrahedral, 56, True)
        self.tell_about(is_tetrahedral, 80, False)
        self.tell_about(is_tetrahedral, 84, True)
        self.tell_about(is_tetrahedral, 365, False)

    def test_is_square_pyramidal(self):
        self.tell_about(is_square_pyramidal, 1, True)
        self.tell_about(is_square_pyramidal, 3, False)
        self.tell_about(is_square_pyramidal, 5, True)
        self.tell_about(is_square_pyramidal, 14, True)
        self.tell_about(is_square_pyramidal, 30, True)
        self.tell_about(is_square_pyramidal, 55, True)
        self.tell_about(is_square_pyramidal, 90, False)
        self.tell_about(is_square_pyramidal, 91, True)
        self.tell_about(is_square_pyramidal, 1024, False)
        self.tell_about(is_square_pyramidal, 1028, False)

    def test_is_pentagonal(self):
        self.tell_about(is_pentagonal, 1, True)
        self.tell_about(is_pentagonal, 3, False)
        self.tell_about(is_pentagonal, 5, True)
        self.tell_about(is_pentagonal, 12, True)
        self.tell_about(is_pentagonal, 14, False)
        self.tell_about(is_pentagonal, 22, True)
        self.tell_about(is_pentagonal, 30, False)
        self.tell_about(is_pentagonal, 35, True)
        self.tell_about(is_pentagonal, 51, True)
        self.tell_about(is_pentagonal, 55, False)
        self.tell_about(is_pentagonal, 70, True)
        self.tell_about(is_pentagonal, 91, False)
        self.tell_about(is_pentagonal, 1024, False)
        self.tell_about(is_pentagonal, 1028, False)  

    def test_is_prime_oblong(self):
        self.tell_about(is_prime_oblong, 1, False)
        self.tell_about(is_prime_oblong, 3, False)
        self.tell_about(is_prime_oblong, 5, False)
        self.tell_about(is_prime_oblong, 6, True)
        self.tell_about(is_prime_oblong, 14, True)
        self.tell_about(is_prime_oblong, 22, True)
        self.tell_about(is_prime_oblong, 30, False)
        self.tell_about(is_prime_oblong, 35, True)
        self.tell_about(is_prime_oblong, 51, True)
        self.tell_about(is_prime_oblong, 55, True)
        self.tell_about(is_prime_oblong, 70, False)
        self.tell_about(is_prime_oblong, 91, True)
        self.tell_about(is_prime_oblong, 1024, False)
        self.tell_about(is_prime_oblong, 1028, False)       

    def test_is_pointy(self):
        self.tell_about(is_pointy, 1, False)
        self.tell_about(is_pointy, 2, False)
        self.tell_about(is_pointy, 4, False)
        self.tell_about(is_pointy, 5, True)
        self.tell_about(is_pointy, 8, False)
        self.tell_about(is_pointy, 11, True)
        self.tell_about(is_pointy, 14, True)
        self.tell_about(is_pointy, 25, False)
        self.tell_about(is_pointy, 30, True)
        self.tell_about(is_pointy, 91, True)
        self.tell_about(is_pointy, 100, False)
        self.tell_about(is_pointy, 350, False)
unittest.main()

