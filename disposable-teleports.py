__author__ = 'tpuctah'

'http://www.checkio.org/mission/task/info/disposable-teleports/python-27/'


assert get_path_from("1", "12,23,34,45,56,67,78,81") == [2, 8]
assert get_path_from("2", "12,23,34,45,56,67,78,81") == [1, 3]
assert get_path_from("3", "12,23,34,45,56,67,78,81") == [2, 4]
assert get_path_from("4", "12,23,34,45,56,67,78,81") == [3, 5]


def checkio_(data):

    def find(cell, path):
        if cell == 1 and len(path) == 8:
            print 'yyaaa'
            return path

        path.append(cell)
        for next_cell in get_path_from(cell, data):
            print path
            if next_cell not in path and find(next_cell, path):
                return path
        path.pop()

    f = find(1, [])

    print f
    #assert f

#    return "".join([str(x) for x in f])





def checkio(data):

    from_start_point = get_path_from(1, data)

    route = [1]
    route_dir = []

    def f(points, route, data):
        for point in points:
            if point == 1 and len(set(route)) == 8:
                return route
            elif sorted([route[-1], point]) not in route_dir:
                route_dir.append(sorted([route[-1], point]))
                route.append(point)
                if f(get_path_from(point, data), route, data):
                    return route
                route.pop()
                route_dir.pop()

    print "".join([str(x) for x in f(from_start_point, route, data) + [1]])


































checkio("12,23,34,45,56,67,78,81") == "123456781"
checkio("12,28,87,71,13,14,34,35,45,46,63,65") == "1365417821"
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") == "12382478561"
checkio("13,14,23,25,34,35,47,56,58,76,68") == "132586741"


