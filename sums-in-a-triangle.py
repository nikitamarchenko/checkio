a = [
    [01],
    [11, 12],
    [21, 22, 23],
    [31, 32, 33, 34],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55, 56],
    [61, 62, 63, 64, 65, 66, 67]
]

total = [0]


def r(point=0, level=0, result=0):
    print point, level
    if level < 7:
        result += a[level][point]
        r(point, level + 1, result)
        r(point + 1, level + 1, result)
    elif total[0] < result:
        total[0] = result


r()

print total[0]


def checkio(data):
    total = [0]

    def r(point=0, level=0, result=0):
        if level < len(data):
            result += data[level][point]
            r(point, level + 1, result)
            r(point + 1, level + 1, result)
        elif total[0] < result:
            total[0] = result

    r()

    return total[0]


assert checkio([
    [1],
    [2, 3],
    [3, 3, 1],
    [3, 1, 5, 4],
    [3, 1, 3, 1, 3],
    [2, 2, 2, 2, 2, 2],
    [5, 6, 4, 5, 6, 4, 3]
]) == 23
assert checkio([
    [1],
    [2, 1],
    [1, 2, 1],
    [1, 2, 1, 1],
    [1, 2, 1, 1, 1],
    [1, 2, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 1, 9]
]) == 15
assert checkio([
    [9],
    [2, 2],
    [3, 3, 3],
    [4, 4, 4, 4]
]) == 18