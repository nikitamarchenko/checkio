__author__ = 'nmarchenko'

import sys
#import and init pygame
import pygame
from math import pi as PI
from math import sin, cos, sqrt

pygame.init()

#create the screen
window = pygame.display.set_mode((640, 480))

background = pygame.Surface(window.get_size())



background = background.convert()
background.fill((255, 255, 255))

#pygame.draw.line(background, (0, 0, 0), (0, 0), (100, 100))


SIZE = 15

def DrawHex(pos, text, surface):
    #pygame.draw.line(surface, (0, 0, 0), (0, 0), (100, 100))
    if pygame.font:
        font = pygame.font.Font(None, 16)
        text = font.render(text, True, (10, 10, 10))
        text_pos = text.get_rect(centerx=pos[0], centery=pos[1])
        background.blit(text, text_pos)

    point_from = (0, 0)
    point_to = (0, 0)
    for i in range(7):
        angle = 2 * PI / 6 * i
        x_i = pos[0] + SIZE * cos(angle)
        y_i = pos[1] + SIZE * sin(angle)
        point_to = (x_i, y_i)
        if i == 0:
            point_from = (x_i, y_i)
        else:
            pygame.draw.aaline(surface, (0, 0, 0), point_from, point_to)
            point_from = point_to


def CubeToPoint(cube, window):
    #DrawHex((100, 50), 12, background)

    q = cube[0]
    r = cube[2]

    x = SIZE * 3.0/2.0 * q
    y = SIZE * sqrt(3) * (r + q/2.0)

    return x + window.get_size()[0] / 2, y + window.get_size()[1] / 2


def GetNeighbor(cube, direction):

    neighbors = [
       [+1, -1,  0], [ 0, -1, +1], [-1,  0, +1],
       [-1, +1,  0], [ 0, +1, -1], [+1,  0, -1],
    ]

    d = neighbors[direction]

    return cube[0] + d[0], cube[1] + d[1], cube[2] + d[2]


def GetNeighbor2(cube, direction):

    neighbors = [[+1,  0, -1], [+1, -1,  0], [ 0, -1, +1], [-1,  0, +1], [-1, +1,  0], [ 0, +1, -1]]

    d = neighbors[direction]

    return cube[0] + d[0], cube[1] + d[1], cube[2] + d[2]

DrawHex(CubeToPoint((0, 0, 0), window), "1", background)
#DrawHex(CubeToPoint((0, 1, -1), window), 12, "2", background)

# 1: 0, 1, -1
# 2: -1, 2, -1
# 3: -2, 3, -1
# 4: -3, 4, -1

#for i in range(6):
#    DrawHex(CubeToPoint(GetNeighbor((0, 0, 0), i), window), 12, str(i+2), background)

f = 5
t = 11

result = []


def hex_distance((x1, y1, z1), (x2, y2, z2)):
    return max(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))

# counter = 1
# for radius in range(1, 7):
#     cube = (-radius + 1, -radius, -1)
#     print cube
#     for ii, len in enumerate(map(sum, zip([radius] * 6, [-1] + [0] * 4 + [1]))):
#         for iii in range(len):
#             counter += 1
#             DrawHex(CubeToPoint(cube, window), str(counter), background)
#             cube = GetNeighbor2(cube, ii)

def checkio(value):
    first_h = (0, 0, 0) if min(value[0], value[1]) == 1 else None
    counter = 2
    for radius in range(1, 100):
        h = (-radius+1, radius, -1)
        print h
        for ii, len in enumerate(map(sum, zip([radius] * 6, [-1] + [0] * 4 + [1]))):
            for iii in range(len):

                print counter, radius, len, h

                DrawHex(CubeToPoint(h, window), str(counter), background)
                if counter == min(value[0], value[1]):
                    #print counter, h
                    first_h = h
                elif counter == max(value[0], value[1]):
                    #print first_h, h, max([abs(x1 - x2) for x1, x2 in zip(first_h, h)])
                    return max([abs(x1 - x2) for x1, x2 in zip(first_h, h)])

                neighbor = ((+1, 0, -1), (+1, -1, 0), (0, -1, +1), (-1, 0, +1), (-1, +1, 0), (0, +1, -1))[ii]

                h = map(sum, zip(h, neighbor))
                counter += 1






print checkio([100, 1])
print checkio([6, 19])

# def draw_circle(start, radius):
#     counter = 2
#     cube = (start[0], start[1] + 1, start[2] - 1)
#     for i in range(6):
#         for ii in range(radius):
#             DrawHex(CubeToPoint(cube, window), 12, str(counter), background)
#             cube = GetNeighbor(cube, i)
#             counter += 1


#draw_circle((0, 0, 0), 1)
#draw_circle((-1, 1, 0), 2)

# print result

#print hex_distance(result[0], result[1])

window.blit(background, (0, 0))
#draw a line - see http://www.pygame.org/docs/ref/draw.html for more
#draw it to the screen
pygame.display.flip()

#input handling (somewhat boilerplate code):
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        else:
            pass
            # print event
