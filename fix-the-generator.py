__author__ = 'nmarchenko'

'''
    http://www.checkio.org/mission/fix-the-generator/
'''


def checkio(d):
    result, r = set(), range(0, len(d))

    for i in r:
        for ii in r:
            for iii in r:
                result.add(tuple(set(sorted([i, ii, iii]))))

    result = [(d[x[0]], d[x[1]], d[x[2]]) for x in result if len(x) == 3]

    return len([(a, b, c) for a, b, c in result if not (a <= b + c and b <= c + a and c <= a + b)])

import unittest

class _test(unittest.TestCase):

    def test_00(self):
        self.assertEqual(checkio([4, 2, 10]), 1)

    def test_01(self):
        self.assertEqual(checkio([1, 2, 3]), 0)

    def test_02(self):
        self.assertEqual(checkio([5, 2, 9, 6]), 2)

    def test_03(self):
        self.assertEqual(checkio([2, 79, 47, 5, 8, 57, 35, 71, 27, 2]), 101)

    def test_04(self):
        self.assertEqual(checkio([64, 24, 58, 47, 91]), 3)

    def test_05(self):
        self.assertEqual(checkio([9, 68, 31, 46, 30]), 6)

    def test_06(self):
        self.assertEqual(checkio([99, 61, 82, 35, 61, 91]), 2)

    def test_07(self):
        self.assertEqual(checkio([35, 18, 64, 37, 99, 3, 76, 99, 12]), 59)

    def test_08(self):
        self.assertEqual(checkio([47, 45, 33, 31, 50, 13]), 5)

    def test_09(self):
        self.assertEqual(checkio([32, 14, 63, 90, 79, 91, 12, 5, 67]), 51)

    def test_10(self):
        self.assertEqual(checkio([69, 84, 12, 52]), 3)

    def test_11(self):
        self.assertEqual(checkio([78, 71, 49, 45, 86, 37]), 1)

    def test_12(self):
        self.assertEqual(checkio([36, 19, 21]), 0)

    def test_13(self):
        self.assertEqual(checkio([29, 50, 51, 36, 4, 71, 13]), 23)

    def test_14(self):
        self.assertEqual(checkio([16, 35, 95, 29, 38, 36, 36]), 15)

    def test_15(self):
        self.assertEqual(checkio([83, 47, 25, 18, 50, 67]), 9)

    def test_16(self):
        self.assertEqual(checkio([99, 37, 90, 52, 94, 93, 29, 59]), 17)

    def test_17(self):
        self.assertEqual(checkio([79, 94, 86, 15, 100, 4, 77, 7, 13]), 56)

    def test_18(self):
        self.assertEqual(checkio([60, 63, 48, 35, 31, 49, 54]), 0)

    def test_19(self):
        self.assertEqual(checkio([38, 76, 20, 44, 1]), 8)

    def test_20(self):
        self.assertEqual(checkio([58, 98, 1, 97, 13]), 7)

    def test_21(self):
        self.assertEqual(checkio([93, 86, 67, 22, 4]), 7)

    def test_22(self):
        self.assertEqual(checkio([25, 29, 17, 55]), 3)

    def test_23(self):
        self.assertEqual(checkio([67, 24, 35]), 1)

    def test_24(self):
        self.assertEqual(checkio([90, 21, 69, 97, 65, 49, 28, 74, 94, 64]), 27)

    def test_25(self):
        self.assertEqual(checkio([63, 19, 35, 53, 72, 33, 82, 67, 7, 35]), 51)

    def test_26(self):
        self.assertEqual(checkio([13, 64, 94, 7, 31, 100, 77, 19]), 39)

    def test_27(self):
        self.assertEqual(checkio([5, 7, 28, 65]), 4)

    def test_28(self):
        self.assertEqual(checkio([25, 79, 25]), 1)

    def test_29(self):
        self.assertEqual(checkio([66, 83, 39, 2, 94]), 6)

    def test_30(self):
        self.assertEqual(checkio([43, 24, 3, 39, 16, 4]), 16)

    def test_31(self):
        self.assertEqual(checkio([36, 42, 23, 60, 84, 69, 26]), 14)

    def test_32(self):
        self.assertEqual(checkio([30, 38, 68, 59, 41, 6, 14]), 20)

    def test_33(self):
        self.assertEqual(checkio([40, 40, 84, 5]), 3)

    def test_34(self):
        self.assertEqual(checkio([65, 64, 10, 44, 67, 63, 26]), 9)

    def test_35(self):
        self.assertEqual(checkio([73, 19, 48, 59, 19, 65, 94, 44, 61]), 26)

    def test_36(self):
        self.assertEqual(checkio([25, 4, 66, 82, 89, 56, 97, 39]), 30)

    def test_37(self):
        self.assertEqual(checkio([80, 36, 57, 26, 14]), 6)

    def test_38(self):
        self.assertEqual(checkio([23, 77, 96, 62, 96, 59, 6, 27, 74]), 38)

    def test_39(self):
        self.assertEqual(checkio([48, 74, 31, 97, 73, 42, 39, 27, 53, 20]), 45)

    def test_40(self):
        self.assertEqual(checkio([11, 96, 8, 69, 14]), 9)

    def test_41(self):
        self.assertEqual(checkio([52, 57, 90]), 0)

    def test_42(self):
        self.assertEqual(checkio([10, 80, 38, 66, 26, 22, 41]), 23)

    def test_43(self):
        self.assertEqual(checkio([8, 78, 27, 34, 92, 21, 14]), 24)

    def test_44(self):
        self.assertEqual(checkio([92, 74, 98, 63, 85]), 0)

    def test_45(self):
        self.assertEqual(checkio([29, 17, 4, 33]), 2)

    def test_46(self):
        self.assertEqual(checkio([54, 45, 15, 48, 92, 3, 44]), 18)





