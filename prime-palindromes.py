__author__ = 'tpuctah'

"""
http://www.checkio.org/mission/task/info/prime-palindromes-/python-27/
"""

import unittest


def sieve_of_eratosthenes(n):
    l, r = range(2, n), []
    while len(l):
        r.append(l[0])
        l = [v for v in l if v % l[0]]
    return r


def sieve_of_eratosthenes_palindromes(n):
    l, r = range(2, n), []
    while len(l):
        if str(l[0]) == str(l[0])[::-1]:
            r.append(l[0])
        l = [v for v in l if v % l[0]]
    return r


def sieve_of_eratosthenes2(n, chunck=10):
    current = chunck
    l, r = range(2, current), []
    while True:
        r.append(l[0])
        l = [v for v in l if v % l[0]]
        if current > n:
            return r
        while not l:
            l = range(current, current+chunck)
            current += chunck
            l = [v for v in l if all([v % x for x in r])]
    return r



def checkio_00(n):
    l = range(2, n+1)
    while True:
        if str(l[0]) == str(l[0])[::-1] and l[0] >= n:
            return l[0]
        l = [v for v in l if v % l[0]]


def checkio(n, chunk=100):
    current = chunk
    l, r = range(2, current), []
    while True:
        if str(l[0]) == str(l[0])[::-1] and l[0] >= n:
            return l[0]
        r.append(l[0])
        l = [v for v in l if v % l[0]]
        while not l:
            l = range(current, current+chunk)
            current += chunk
            l = [v for v in l if all([v % x for x in r])]


ETALON = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271]

ETALON_PALINDROMIC = [2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929, 10301, 10501, 10601, 11311, 11411, 12421, 12721, 12821, 13331, 13831, 13931, 14341, 14741, 15451, 15551, 16061, 16361, 16561, 16661, 17471, 17971, 18181]


class Test(unittest.TestCase):

    def test_00(self):
        self.assertEqual(sieve_of_eratosthenes(ETALON[-1]+1), ETALON)

    def test_01(self):
        self.assertEqual(sieve_of_eratosthenes_palindromes(ETALON_PALINDROMIC[-1]+1), ETALON_PALINDROMIC)
        pass

    def test_02(self):
        self.assertEqual(checkio(31), 101)

    def test_03(self):
        self.assertEqual(checkio(130), 131)

    def test_04(self):
        self.assertEqual(checkio(131), 131)

    def test_05(self):
        self.assertEqual(sieve_of_eratosthenes2(ETALON[-1]+1), ETALON)
        pass

    def test_06(self):
        self.assertEqual(checkio(18181-1), 18181)


