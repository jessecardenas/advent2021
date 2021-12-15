#!/usr/bin/python3
import time, os

field = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

# lets turn this into an array of numbers
field = [ [ int(x) for x in s if x.isnumeric() ] for s in field.split('\n') if s ]

def print_field(field):
  # print("\033[%d;%dH" % (0, 0)) # set cursor to 0,0
  # print( "\n".join([ "".join([ str(x) for x in row ]) for row in field ]) )
  for row in field:
    print( "".join([ str(x) for x in row ] ) )

flashes = 0

def flash(field, x, y):
  flashes = 1
  field[y][x] = -100
  for y2 in range(y-1, y+1):
    for x2 in range(x-1, x+1):
      if x2 >= 0 and x2 < len(field[0]) and y2 >= 0 and y2 < len(field):
        if x2 == x and y2 == y:
          continue
        field[y2][x2] += 1
        if field[y2][x2] > 9:
          flashes += flash(field, x2, y2)
  return flashes

def step(field):
  flashes = 0
  for y in range(len(field)):
    for x in range(len(field[0])):
      field[y][x] += 1
  for y in range(len(field)):
    for x in range(len(field[0])):
      if field[y][x] > 9:
        flashes += flash(field, x, y)
  for y in range(len(field)):
    for x in range(len(field[0])):
      if field[y][x] < 0:
        field[y][x] = 0
  return flashes

os.system('clear')
for i in range(10):
  print_field(field)
  print(i)
  print(flashes)
  time.sleep(1)
  flashes += step(field)





