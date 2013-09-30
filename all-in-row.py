__author__ = 'nmarchenko'

# http://www.checkio.org/mission/task/info/all-in-row/python-27/

import itertools


def checkio(data):
    #print str(data).replace('[', '').replace(']', '').split(',')

    print map(int, (''.join([x for x in str(data) if x.isdigit() or x == ','])).split(','))

    return data


checkio([1, 2, 3]) == [1, 2, 3]
checkio([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]

checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]