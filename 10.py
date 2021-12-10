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

def parse_line(line):
  if not line:
    return True
  loc = 0
  done = False
  stack = []
  openers = "([{<"
  closers = ")]}>"
  points = [3, 57, 1197, 25137]
  print(line)
  while not done:
    # print(loc, line[loc])
    if line[loc] in openers:
      stack.append(line[loc])
    elif line[loc] in closers:
      brace_id = openers.find(stack[-1])
      if closers[brace_id] != line[loc]:
        err = "Expected {}, but found {} instead.".format(closers[brace_id], line[loc])
        e = SyntaxError(err)
        e.points = points[ closers.find(line[loc]) ]
        raise e
      stack = stack[:-1]
    else:
      raise ValueError("Invalid Character")
    loc += 1
    if loc >= len(line):
      done = True
  return True

score = 0
for line in lines.split('\n'):
  try:
    # print(parse_line(line))
    parse_line(line)
  except SyntaxError as e:
    print(e)
    print(e.points)
    score += e.points

print(score)


