__author__ = 'nmarchenko'

from itertools import izip_longest

def checkio2(data):

    print bin(data[0])[2:]
    print "00"+bin(data[1])[2:]

    v1 = map(int, list(reversed(bin(data[0])[2:])))
    v2 = map(int, list(reversed(bin(data[1])[2:])))

    return map(sum, izip_longest(v1, v2, fillvalue=0)).count(1)


def checkio(data):
    v = [map(int, list(reversed(bin(x)[2:]))) for x in data]
    return map(sum, izip_longest(*v, fillvalue=0)).count(1)

assert checkio([117, 17]) == 3
assert checkio([1, 2]) == 2
assert checkio([16, 15]) == 5
