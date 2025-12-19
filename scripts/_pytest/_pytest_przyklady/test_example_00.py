# pytest understands unittest, so everything we've discussed so far remains valid
import unittest

from example_01 import sum_, div

class TestExample01(unittest.TestCase):
    def test_sum_(self):
        self.assertEqual(sum_(1, 2), 3)
        self.assertEqual(sum_(0, 0), 0)
        self.assertEqual(sum_(1.5, 2.8), 4.3)

        # self.assertEqual(sum_(0.2, 0.1), 0.3)
        self.assertAlmostEqual(sum_(0.2, 0.1), 0.3)

        a = 1
        b = 2
        self.assertEqual(sum_(a, b), 3)

        # for t in [
        #     (1, 2, 3),
        #     (3, 2, 7),
        #     (-4, 4, 0)
        # ]:
        #     self.assertEqual(sum_(t[0], t[1]), t[2])

        for param in [
            (1, 2, 3),
            (3, 4, 7),
            (-4, 4, 0)
        ]:
            with self.subTest(params=param):
                self.assertEqual(sum_(param[0], param[1]), param[2]), f"{param[0]} + {param[1]} != {param[2]}"

    def test_div(self):
        with self.assertRaises(ValueError):
            div(4, 0)