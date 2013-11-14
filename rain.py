__author__ = 'nmarchenko'

"""
http://habrahabr.ru/post/200190/
"""

import sys

data = [2, 5, 1, 2, 3, 4, 7, 7, 6]


def print_relief(relief):
    for i in reversed(range(1, max(relief) + 1)):
        sys.stdout.write('\n')
        sys.stdout.write(str(i))
        sys.stdout.write('|')
        for ii in relief:
            if i == ii:
                sys.stdout.write(str(ii))
            elif i < ii:
                sys.stdout.write('#')
            else:
                sys.stdout.write(' ')
    sys.stdout.write('\n')
    sys.stdout.write('-' * (len(relief) + 2))
    sys.stdout.write('\n  ')
    for i in range(0, len(relief)):
        sys.stdout.write(str(i))

print_relief(data)


# def find(data):
#     m = data[0]
#     for i in data[1:]:
#         if i >= m:
#             m = i
#         else:
#             return m

def find(data):
    m = 0
    index = 0
    for i, v in enumerate(data):
        if v >= m:
            m = v
            index = i
        else:
            return m, index

print ' '
print find(data)
print find(list(reversed(data)))

