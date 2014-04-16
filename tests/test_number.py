import unittest

from pkg.mod import Number

class TestNumber(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple(self):
        nr = Number()
        nr.add(2)
        nr.mul(3)
        s = str(nr)
        self.assertEqual(s, 'Number(6)')

if __name__ == '__main__':
    unittest.main()