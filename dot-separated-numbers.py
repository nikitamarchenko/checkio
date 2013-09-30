__author__ = 'nmarchenko'

# http://www.checkio.org/mission/task/info/dot-separated-numbers/python-27/


def checkio(data):

    def f(data):
        if data.isdigit():
            return "{:,}".format(int(data)).replace(',', '.')
        return data

    return ' '.join(map(f, data.split(' ')))


checkio('123456') == '123.456'
checkio('333') == '333'
checkio('9999999') == '9.999.999'
checkio('123456 567890') == '123.456 567.890'
checkio('price is 5799') == 'price is 5.799'
checkio('he was born in 1966th') == 'he was born in 1966th'
