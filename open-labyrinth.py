__author__ = 'tpuctah'


#def NextPath(map, coord):



def checkio(map):

    class Cell(object):
        def __init__(self, map, coord, dir):
            self._map = map
            self._coord = coord
            self._dir = dir

        def GetNextCell(self):
            if self._map[self.X-1][self.Y] == 0:
                yield Cell(self._map, (self.X-1, self.Y), 'N')
            if self._map[self.X+1][self.Y] == 0:
                yield Cell(self._map, (self.X+1, self.Y), 'S')
            if self._map[self.X][self.Y-1] == 0:
                yield Cell(self._map, (self.X, self.Y-1), 'W')
            if self._map[self.X][self.Y+1] == 0:
                yield Cell(self._map, (self.X, self.Y+1), 'E')

        @property
        def X(self):
            return self._coord[0]

        @property
        def Y(self):
            return self._coord[1]

        def __str__(self):
            return self._dir

        def __eq__(self, other):
            return self._coord == other._coord



    test_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    # test_1 = Cell(test_map, (2, 2))
    # for i, v in enumerate(test_1.GetNextCell()):
    #     cell = v[1]
    #     if i == 0:
    #         assert cell.X == 1 and cell.Y == 2
    #     if i == 1:
    #         assert cell.X == 3 and cell.Y == 2
    #     if i == 2:
    #         assert cell.X == 2 and cell.Y == 1
    #     if i == 3:
    #         assert cell.X == 2 and cell.Y == 3
    #
    # test_2 = Cell(test_map, (5, 2))
    # for i, cell in enumerate(test_2.GetNextCell()):
    #     assert False

    def find(cell, path):
        path.append(cell)
        if cell.X == 10 and cell.Y == 10:
            return path
        for next_cell in cell.GetNextCell():
            if next_cell not in path and find(next_cell, path):
                return path
        path.pop()

    print find(Cell(map, (1, 1), ""), [])

    print "".join()


checkio([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])