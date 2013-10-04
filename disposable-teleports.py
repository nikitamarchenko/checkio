__author__ = 'tpuctah'

'http://www.checkio.org/mission/task/info/disposable-teleports/python-27/'

def checkio(data):
    route = ['1']
    route_dir = []

    def find(start_point):
        for point in [x for x in data.replace(start_point, "").split(',') if len(x) == 1]:
            if sorted([start_point, point]) not in route_dir:
                map(list.append, [route, route_dir], [point, sorted([start_point, point])])
                if (point == '1' and len(set(route)) == 8) or find(point):
                    return route
                map(list.pop, (route, route_dir))
    return "".join(find('1'))

assert checkio("12,23,34,45,56,67,78,81") == "123456781"
assert checkio("12,28,87,71,13,14,34,35,45,46,63,65") == "128713453641"
assert checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") == "12382478561"
assert checkio("13,14,23,25,34,35,47,56,58,76,68") == "132586741"
assert checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") == '12382478561'

