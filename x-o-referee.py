__author__ = 'tpuctah'

import itertools
import copy
import functools
import operator

def checkio(table):

    #
    # table3 = copy.deepcopy(table)
    #
    # print table
    #
    # print "=" * 80
    #
    # print table2[0], table2[1], table2[2]
    #
    # table2[0][1], table2[1][0] = table2[1][0], table2[0][1]
    #
    # print table2[0], table2[1], table2[2]
    #
    # print "=" * 80
    #
    # print table2[0], table2[1], table2[2]
    #
    # table2[0][2], table2[2][0] = table2[2][0], table2[0][2]
    #
    # print table2[0], table2[1], table2[2]
    #
    # print "=" * 80
    #
    # print table2[0], table2[1], table2[2]
    #
    # table2[1][2], table2[2][1] = table2[2][1], table2[1][2]
    #
    # print table2[0], table2[1], table2[2]
    #
    # print "=" * 80

    "['X', 'X', 'X'] ['.', 'X', 'O'] ['O', '.', 'O']"

    table = [list(x) for x in table]

    t = copy.deepcopy(table)

    # 0AC => 0BD
    # B0E => A0F
    # DFO => CE0

    t[0][1], t[1][0], t[0][2], t[2][0],  t[1][2], t[2][1] = t[1][0], t[0][1], t[2][0], t[0][2], t[2][1], t[1][2]

    # ABC => AEF
    # DEF => CEF
    # GHI

    #list2 = [[row[i] for row in mat] for i in [0, 1, 2]]

    t2 = [[t[0][0], t[1][1], t[2][2]], [t[2][0], t[1][1], t[0][2]]]

    merged = list(itertools.chain(*[table, t, t2]))

    is_x = functools.partial(operator.eq, "X")
    is_o = functools.partial(operator.eq, "O")

    result = [x for x in merged if all(map(is_x, x)) or all(map(is_o, x))]

    if result:
        return result[0][0]

    return "D"

# checkio([
#     "X.O",
#     "XX.",
#     "XOO"])
#
# checkio([
#     "X.O",
#     "XX.",
#     "OOO"])


assert checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X", "Xs wins"
assert checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"

assert checkio([
    "OX.",
    "XOX",
    "XOO"]) == "O"

assert checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"
