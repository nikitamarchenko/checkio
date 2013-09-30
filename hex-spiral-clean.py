__author__ = 'nmarchenko'


def checkio(value):
    first_h = (0, 0, 0) if min(value[0], value[1]) == 1 else None
    counter = 2
    for radius in xrange(1, 100):
        h = (-radius + 1, radius, -1)
        for ii, len in enumerate(map(sum, zip([radius] * 6, [-1] + [0] * 4 + [1]))):
            for iii in range(len):

                if counter == min(value[0], value[1]):
                    first_h = h
                elif counter == max(value[0], value[1]):
                    return max([abs(x1 - x2) for x1, x2 in zip(first_h, h)])

                neighbor = ((+1, 0, -1), (+1, -1, 0), (0, -1, +1), (-1, 0, +1), (-1, +1, 0), (0, +1, -1))[ii]
                h = map(sum, zip(h, neighbor))
                counter += 1



assert checkio([1, 2]) == 1
assert checkio([2, 9]) == 1
assert checkio([9, 2]) == 1
assert checkio([6, 19]) == 2
assert checkio([5, 11]) == 3
assert checkio([42, 13]) == 5
assert checkio([92, 62]) == 1
print checkio([100, 1])
assert checkio([100, 1]) == 6

