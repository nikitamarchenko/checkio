__author__ = 'tpuctah'


# I 1 (unus)
#
# V 5 (quinque)
#
# X 10 (decem)
#
# L 50 (quinquaginta)
#
# C 100 (centum)
#
# D 500 (quingenti)
#
# M 1,000 (mille)

import itertools

def checkio(n):

    data = reversed(zip(
        [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000],
        ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    ))

    def fn(n, result, current, iter):
        if n >= current[0]:
            result.append(current[1])
            if n > current[0]:
                fn(n - current[0], result, current, iter)
        else:
            fn(n, result, next(i), iter)

    i = itertools.chain(data)

    result = []
    fn(n, result, next(i), i)

    return "".join(result)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(155) == 'CLV'
    assert checkio(255) == 'CCLV'
    assert checkio(49) == 'XLIX', '49'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
