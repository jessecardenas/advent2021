#!/usr/bin/python3


with open('01_in.txt') as f:
  lines = f.read()


data = [ float(x) for x in lines.split('\n') if x]

increases = 0
for i in range(1, len(data)):
  increases += data[i] > data[i-1]
print(increases)

