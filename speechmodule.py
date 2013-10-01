__author__ = 'tpuctah'

def checkio_0(n):
    s = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    s2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    s3 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    result = []

    hundreds = n / 100

    if hundreds:
        result.append("{} hundred".format(s[hundreds]))

    d10 = n % 100

    if 10 <= d10 < 20:
        result.append(s2[n%10])
    elif d10 > 20:
        result.append(s3[d10/10])

    d1 = n % 10

    if d1 > 0 and (d10 < 10 or d10 > 20):
        result.append(s[d1])

    print " ".join(result)
    return " ".join(result)


def checkio(n):

    s = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    result = []

    hundredth = n / 100
    tenth = n % 100 / 10
    one = n % 10

    if hundredth:
        result.append("{} hundred".format(s[hundredth]))

    if tenth == 1:
        s2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        result.append(s2[one])
    else:
        if tenth >= 2:
            s3 = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
            result.append(s3[tenth])
        if one > 0:
            result.append(s[one])

    return " ".join(result)


#print checkio(123)

#print checkio(10)
#print checkio(20)

assert checkio(4)=='four'
assert checkio(143)=='one hundred forty three'
assert checkio(12)=='twelve'
assert checkio(101)=='one hundred one'
assert checkio(212)=='two hundred twelve'
assert checkio(40)=='forty'