#!/usr/bin/env python3

# line = "{([(<{}[<>[]}>{[]{[(<()>"

''' lines = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""" '''

with open('10_in.txt') as f:
  lines = f.read()

# lines = "<{([{{}}[<[[[<>{}]]]>[]]"


def parse_line(line):
  if not line:
    return 0
  loc = 0
  done = False
  stack = []
  openers = "([{<"
  closers = ")]}>"
  err_point_board = [3, 57, 1197, 25137]
  inc_point_board = [ 1, 2, 3, 4 ]
  # print(line)
  while not done:
    # print(loc, line[loc])
    if line[loc] in openers:
      stack.append(line[loc])
    elif line[loc] in closers:
      brace_id = openers.find(stack[-1])
      if closers[brace_id] != line[loc]:
        err = "Expected {}, but found {} instead.".format(closers[brace_id], line[loc])
        e = SyntaxError(err)
        e.points = err_point_board[ closers.find(line[loc]) ]
        raise e
      stack = stack[:-1]
    else:
      raise ValueError("Invalid Character")
    loc += 1
    if loc >= len(line):
      done = True
  inc_points = 0
  for c in stack[::-1]:
    inc_points = inc_points * 5 + inc_point_board[openers.find(c)]
  return inc_points

err_score = 0
inc_scores = []
for line in lines.split('\n'):
  if not line:
    continue
  try:
    # print(parse_line(line))
    inc_points = parse_line(line)
    print(inc_points)
    inc_scores.append(inc_points)
  except SyntaxError as e:
    print(e)
    print(e.points)
    err_score += e.points

print("Syntax score: {}".format(err_score))
inc_scores.sort()
mid = int((len(inc_scores) - 1) / 2)
print("Completion score: {}".format(inc_scores[mid]))

