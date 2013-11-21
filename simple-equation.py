__author__ = 'nmarchenko'

'''
    http://www.checkio.org/mission/simple-equation/
'''


def checkio(data):
    result = 0
    for i in range(0, data[0]+1):
        for ii in range(0, data[1]+1):
            for iii in range(0, data[2]+1):
                if i + ii + iii <= data[3]:
                    result += 1
    return result

import unittest


class _test(unittest.TestCase):

    def test_00(self):
        self.assertEqual(checkio([3, 2, 1, 4]), 20)

    def test_01(self):
        self.assertEqual(checkio([1, 1, 1, 1]), 4)

    def test_02(self):
        self.assertEqual(checkio([4, 4, 4, 1]), 4)

    def test_03(self):
        self.assertEqual(checkio([18, 17, 15, 83]), 5472)

    def test_04(self):
        self.assertEqual(checkio([10, 38, 4, 80]), 2145)

    def test_05(self):
        self.assertEqual(checkio([3, 1, 32, 39]), 264)

    def test_06(self):
        self.assertEqual(checkio([24, 49, 38, 40]), 11521)

    def test_07(self):
        self.assertEqual(checkio([5, 46, 40, 78]), 11191)

    def test_08(self):
        self.assertEqual(checkio([15, 9, 15, 33]), 2504)

    def test_09(self):
        self.assertEqual(checkio([5, 24, 49, 46]), 4875)

    def test_10(self):
        self.assertEqual(checkio([17, 29, 50, 82]), 26980)

    def test_11(self):
        self.assertEqual(checkio([17, 3, 48, 48]), 2808)

    def test_12(self):
        self.assertEqual(checkio([29, 21, 8, 56]), 5936)

    def test_13(self):
        self.assertEqual(checkio([23, 42, 18, 96]), 19608)

    def test_14(self):
        self.assertEqual(checkio([3, 39, 49, 91]), 8000)

    def test_15(self):
        self.assertEqual(checkio([11, 2, 39, 78]), 1440)

    def test_16(self):
        self.assertEqual(checkio([50, 13, 15, 40]), 6048)

    def test_17(self):
        self.assertEqual(checkio([20, 16, 39, 64]), 13994)

    def test_18(self):
        self.assertEqual(checkio([14, 8, 23, 60]), 3240)

    def test_19(self):
        self.assertEqual(checkio([9, 44, 16, 66]), 7640)

    def test_20(self):
        self.assertEqual(checkio([18, 1, 27, 82]), 1064)

    def test_21(self):
        self.assertEqual(checkio([39, 33, 14, 81]), 20365)

    def test_22(self):
        self.assertEqual(checkio([31, 3, 18, 33]), 1782)

    def test_23(self):
        self.assertEqual(checkio([33, 35, 29, 43]), 14280)

    def test_24(self):
        self.assertEqual(checkio([2, 44, 3, 42]), 486)

    def test_25(self):
        self.assertEqual(checkio([35, 21, 50, 61]), 26642)

    def test_26(self):
        self.assertEqual(checkio([17, 23, 27, 67]), 12096)

    def test_27(self):
        self.assertEqual(checkio([47, 35, 19, 46]), 14484)

    def test_28(self):
        self.assertEqual(checkio([30, 40, 25, 61]), 26036)

    def test_29(self):
        self.assertEqual(checkio([1, 25, 7, 44]), 416)

    def test_30(self):
        self.assertEqual(checkio([50, 50, 11, 100]), 30926)

    def test_31(self):
        self.assertEqual(checkio([35, 11, 45, 37]), 6600)

    def test_32(self):
        self.assertEqual(checkio([48, 1, 41, 45]), 2100)

