#!/usr/bin/python3
import os, time
import sys

"""def print_pos(row, col, txt):
  sys.stdout.write("\033[{0};{1}H{2}".format(row, col,txt))
  sys.stdout.flush()"""

def txt_pos(row, col):
  return "\033[{0};{1}H".format(row, col)

class colors:
  bold = '\033[1m'
  green = '\033[1;32m'
  norm = '\033[0m'


# for x in range(1,10):
#   print( (colors.green if x%2 else colors.norm) + txt_pos(x,x) + str(x) )

field = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

# break it out into an array
field = [ [ int(x) for x in s if x.isnumeric() ] for s in field.split('\n') if s ]

def print_field(field, path):
  # print("\033[%d;%dH" % (0, 0)) # set cursor to 0,0
  # print( "\n".join([ "".join([ str(x) for x in row ]) for row in field ]) )
  print( txt_pos(1, 1), end='' )
  for row in field:
    print( "".join([ str(x) for x in row ] ) )
  for pos in path:
    print( colors.green + txt_pos(pos[0]+1, pos[1]+1) + "*", end='' )
  print(txt_pos(len(field), 1) +colors.norm)




curpos = [0, 0] # row, col
endpos = [len(field) - 1, len(field[0]) - 1]
path = []
path.append(curpos)

os.system('clear')
print_field(field, path)

# main loop
done = False
while not done:
  # from current pos, check 3 steps ahead, and pick best path
  new_paths = []
  # UDLR, build out list of possible paths
  for i in "UDLR":
    if is_valid(i):
      for j in "UDLR":
        if is_valid(j):
          for k in "UDLR":
            if is_valid(k):
              new_paths.append(i+j+k)
  for p in new_paths:
    # score the ending
    pass







print()


