__author__ = 'tpuctah'


def get_path_from(station, station_map):
    #return [x.replace(station, "") for x in station_map.split(',') if station in x]
    return [int(x) for x in station_map.replace(str(station), "").split(',') if len(x) == 1]



assert get_path_from("1", "12,23,34,45,56,67,78,81") == [2, 8]
assert get_path_from("2", "12,23,34,45,56,67,78,81") == [1, 3]
assert get_path_from("3", "12,23,34,45,56,67,78,81") == [2, 4]
assert get_path_from("4", "12,23,34,45,56,67,78,81") == [3, 5]


def checkio(data):

    def find(cell, path):
        path.append(cell)
        for next_cell in get_path_from(cell, data):
            if next_cell == 1 and len(path) == 8:
                path.append(1)
                return path
            if next_cell not in path and find(next_cell, path):
                return path
        path.pop()

    f = find(1, [])

    print f
    assert f

    return "".join([str(x) for x in f])





















#assert checkio("12,23,34,45,56,67,78,81") == "123456781"
checkio("12,28,87,71,13,14,34,35,45,46,63,65") == "1365417821"
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") == "12382478561"
checkio("13,14,23,25,34,35,47,56,58,76,68") == "132586741"


