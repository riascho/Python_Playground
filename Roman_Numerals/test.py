import unittest
import main

class TestRoman(unittest.TestCase):

    def test_num_to_roman(self):
        self.assertIsNotNone(main.num_to_roman(1990))
        self.assertEqual(main.num_to_roman(1990),"MCMXC")
        self.assertEqual(main.num_to_roman(-1990),None)


if __name__ == "__main__":
    unittest.main()