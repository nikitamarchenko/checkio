__author__ = 'tpuctah'

"""
http://www.checkio.org/mission/task/info/cipher-map/python-27/
"""

import unittest

import pprint

def checkio(data):
    rotated = data[0]
    result = ""
    for i in range(0, 4):
        result += "".join([data[1][x][y] for x in range(0, 4) for y in range(0, 4) if rotated[x][y] == "X"])
        rotated = (zip(*rotated[::-1]))
    return result



class Test(unittest.TestCase):

    def test_00(self):
        self.assertEqual(checkio([[
        'X...',
        '..X.',
        'X..X',
        '....'],[
        'itdf',
        'gdce',
        'aton',
        'qrdi']
        ]), 'icantforgetiddqd')

    def test_01(self):
        self.assertEqual(checkio([[
        '....',
        'X..X',
        '.X..',
        '...X'],[
        'xhwc',
        'rsqx',
        'xqzz',
        'fyzr']
        ]), 'rxqrwsfzxqxzhczy')