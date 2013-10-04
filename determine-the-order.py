__author__ = 'nmarchenko'

"""

http://www.checkio.org/mission/task/info/determine-the-order/python-27/

The Robots have found an encrypted message. We cannot decrypt it right now, but we can take the first steps.
Given a set of "words," (for simplicity we will use lowercase latin letters as symbols) each word contains symbols at
the "alphabetical" order (It is not in the latin alphabetical order, but a different order). We need to determine the
order of all the symbols from each word and create one word with all the symbols at once from given words in the
"alphabetical" order. For some cases, if we can not determine the order for several symbols -- use latin alphabetical
order. For example: Given words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a" and "d" after "b".
So the result is "zwacbd".

Precondition: In each test, there will be only one solution.

Input: A list of strings.

Output: A string.

Example:

checkio(["acb", "bd", "zwa"]) == "zwacbd"
checkio(["klm", "kadl", "lsm"]) == "kadlsm"
checkio(["a", "b", "c"]) == "abc"
checkio(["aazzss"]) == "azs"
checkio(["dfg", "frt", "tyg"]) == "dfrtyg"

"""


def checkio(data):

    result = list(set("".join(data)))

    done = False
    while not done:
        done = True
        for i in result:
            chunks = [list(x) for x in data if i in x]

            if len(chunks) == 1 and len(chunks[0]) == 1:
                import string
                chunks[0] = string.ascii_lowercase

            for chank in chunks:
                for c in chank:
                    if c in result:
                        i_c, i_i = result.index(c), result.index(i)
                        if chank.index(c) > chank.index(i) and not i_c > i_i:
                            result[i_c], result[i_i] = result[i_i], result[i_c]
                            done = False

    return "".join(result)

import unittest


class _test(unittest.TestCase):
    def test_00(self):
        self.assertTrue(checkio(["acb", "bd", "zwa"]) == "zwacbd")

    def test_01(self):
        self.assertTrue(checkio(["klm", "kadl", "lsm"]) == "kadlsm")

    def test_02(self):
        self.assertTrue(checkio(["a", "b", "c"]) == "abc")

    def test_03(self):
        self.assertTrue(checkio(["aazzss"]) == "azs")

    def test_04(self):
        self.assertTrue(checkio(["dfg", "frt", "tyg"]) == "dfrtyg")