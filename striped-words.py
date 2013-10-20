__author__ = 'tpuctah'

"""
http://www.checkio.org/mission/task/info/striped-words/python-27/
"""

import unittest


def checkio(data):
    result = ""
    for d in data.upper():
        if d in 'AEIOUY':
            result += '0'
        elif d in 'BCDFGHJKLMNPQRSTVWXZ':
            result += '1'
        elif d.isdigit():
            result += 'X'
        else:
            result += '_'
    import re
    return len([x for x in result.split('_') if len(x) > 1 and not re.search('X|00|11', x)])



class Test(unittest.TestCase):

    def test_00(self):
        self.assertEqual(checkio("My name is ..."), 3)

    def test_01(self):
        self.assertEqual(checkio("Hello world"), 0)

    def test_02(self):
        self.assertEqual(checkio("A quantity of striped words."), 1)

    def test_03(self):
        self.assertEqual(checkio("Dog,cat,mouse,bird.Human."), 3)

    def test_04(self):
        self.assertEqual(checkio("1st 2a ab3er root rate"), 1)



