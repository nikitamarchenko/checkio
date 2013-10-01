__author__ = 'tpuctah'


def checkio(data):
    x = range(data[0], max(data) + data[1], data[1])
    y = range(data[2], min(data) - data[3], -data[3])

    if x[0] == y[0]:
        return x[0]

    for i in range(min(len(x), len(y))):
        if x[i+1] >= y[i]:
            return max(x[i], y[i])

assert checkio([150, 50, 1000, 100]) == 450
assert checkio([500, 300, 700, 100]) == 700
assert checkio([250, 50, 900, 100]) == 500
assert checkio([100,100,300,100]) == 200
assert checkio([200,100,200,100]) == 200
assert checkio([100,50,500,400]) == 150
