import unittest
import numpy as np
import bayesnet as bn


class TestNegative(unittest.TestCase):

    def test_negative(self):
        x = bn.Parameter(2.)
        y = -x
        self.assertEqual(y.value, -2)
        y.backward()
        self.assertEqual(x.grad, -1)

        x = np.random.rand(2, 3)
        xp = bn.Parameter(x)
        y = -xp
        self.assertTrue((y.value == -x).all())
        y.backward(np.ones((2, 3)))
        self.assertTrue((xp.grad == -np.ones((2, 3))).all())


if __name__ == '__main__':
    unittest.main()
