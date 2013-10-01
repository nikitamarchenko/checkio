__author__ = 'tpuctah'


def checkio(time):

    def to_morze(arg):
        n, size = arg
        result = list('.' * 4)
        for i, v in enumerate([8, 4, 2, 1]):
            if n >= v:
                result[i] = '-'
                n -= v
        return "".join(result[-size:])

    l = [(2, 4), (3, 4), (3, 4)]
    args = [[(x/10, l[p][0]), (x%10, l[p][1])] for p, x in enumerate(map(int, time.split(":")))]

    return " : ".join(map(lambda x: " ".join(map(to_morze, x)), args))


print checkio( "10:37:49" )
print checkio( "00:1:02" )

assert checkio( "10:37:49" ) == ".- .... : .-- .--- : -.. -..-", "First Test"
assert checkio( "21:34:56" ) == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
assert checkio( "00:1:02" )  == ".. .... : ... ...- : ... ..-.", "Third Test"
assert checkio( "23:59:59" ) == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
