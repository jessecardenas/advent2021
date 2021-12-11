#!/usr/bin/python3

calls = []
boards = []
with open('04_in.txt', 'r') as f:
  calls = [ int(x) for x in f.readline().split(',') if x ]
  print(calls)

  board = []
  boardline = 0
  for line in f:
    if not line:
      continue
    board.append([ int(x) for x in line.split(' ') if x.isnumeric() ] )
    boardline += 1
    if boardline == 5:
      boardline = 1
      print(board)
      boards.append(board)
      board = []



