import unittest

def division(a, b):
    return a / b

class TestDivision(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(5, 0)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            division(5, '2')
        with self.assertRaises(TypeError):
            division('10', 2)

if __name__ == '__main__':
    # Dodajte verbosity=2 kao argument za detaljnije izveštaje
    unittest.main(verbosity=2)
