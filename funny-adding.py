__author__ = 'tpuctah'


def checkio(data):

    n1 = bin(data[0])[2:]
    n2 = bin(data[1])[2:]

    max_len = max(len(n1), len(n2)) + 1

    n1 = n1.zfill(max_len)
    n2 = n2.zfill(max_len)

    result = [0] * max_len
    additional = [0] * max_len
    for step, i in enumerate(reversed(range(max_len))):
        tmp = int(n1[i]) + int(n2[i])

        if additional[i] == 1:
            tmp += 1

        if tmp == 1:
            result[i] = 1

        if tmp >= 2:
            additional[i-1] = 1
            if tmp == 2:
                result[i] = 0
            if tmp == 3:
                result[i] = 1

        print "Step {}".format(step+1)
        current_step = ([' ']*max_len)
        current_step[i] = '!'
        print "current col -> " + ''.join(current_step)
        print "               {}".format("".join(map(str, additional)).replace("0", " "))
        print "first       -> {}".format(n1)
        print "second      -> {}".format(n2)
        print "---------------" + "-" * max_len
        print "result      -> {}\n".format("".join(map(str, result)))

    return int("".join(map(str, result)), 2)


checkio([0xff, 0xff])

assert checkio([5, 5]) == 10
assert checkio([7,1]) == 8