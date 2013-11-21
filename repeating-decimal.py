__author__ = 'nmarchenko'

'''
http://www.checkio.org/mission/repeating-decimal/
'''


def checkio(data):
    n, d = data
    v = n // d
    r = str(v)
    n = 10 * (n - v * d)

    if n:
        r += '.'
        s = {}
        while n > 0:
            if n in s:
                return "{}({})".format(r[:s[n]], r[s[n]:])
            s[n] = len(r)
            v = n // d
            r += str(v)
            n = 10 * (n - v * d)

    return r


import unittest

class _test(unittest.TestCase):

    def test_00(self):
        self.assertEqual(checkio([1, 3]), '0.(3)')

    def test_01(self):
        self.assertEqual(checkio([5, 3]), '1.(6)')

    def test_02(self):
        self.assertEqual(checkio([3, 8]), '0.375')

    def test_03(self):
        self.assertEqual(checkio([7, 11]), '0.(63)')

    def test_04(self):
        self.assertEqual(checkio([29, 12]), '2.41(6)')

    def test_05(self):
        self.assertEqual(checkio([11, 7]), '1.(571428)')

    def test_06(self):
        self.assertEqual(checkio([23, 2]), '11.5')

    def test_07(self):
        self.assertEqual(checkio([2, 21]), '0.(095238)')

    def test_08(self):
        self.assertEqual(checkio([1, 17]), '0.(0588235294117647)')

    def test_09(self):
        self.assertEqual(checkio([58, 23]), '2.(5217391304347826086956)')

    def test_10(self):
        self.assertEqual(checkio([2, 3]), '0.(6)')

    def test_11(self):
        self.assertEqual(checkio([5, 2]), '2.5')

    def test_12(self):
        self.assertEqual(checkio([6, 4]), '1.5')

    def test_13(self):
        self.assertEqual(checkio([20, 6]), '3.(3)')

    def test_14(self):
        self.assertEqual(checkio([11, 13]), '0.(846153)')

    def test_15(self):
        self.assertEqual(checkio([22, 13]), '1.(692307)')

    def test_16(self):
        self.assertEqual(checkio([18, 23]), '0.(7826086956521739130434)')

    def test_17(self):
        self.assertEqual(checkio([30, 23]), '1.(3043478260869565217391)')

    def test_18(self):
        self.assertEqual(checkio([10, 12]), '0.8(3)')

    def test_19(self):
        self.assertEqual(checkio([41, 12]), '3.41(6)')


