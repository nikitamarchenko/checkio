__author__ = 'nmarchenko'


def checkio(balance, operations):
    return balance - sum([x + 1 for x in operations if x % 5 == 0 and x > 0 and balance - x - 1 > 0])

    for o in [x for x in operations if x % 5 == 0 and x > 0]:
        if balance > o + 1:
            balance -= o + 1
    return balance

assert checkio(120, [10, 20, 30]) == 57
assert checkio(120, [200, 10]) == 109
assert checkio(120, [3, 10]) == 109
assert checkio(120, [200, 119]) == 120
assert checkio(120, [120, 10, 122, 2, 10, 10, 30, 1]) == 56
assert checkio(120, [-10]) == 120