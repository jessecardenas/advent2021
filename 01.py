#!/usr/bin/python3


with open('01_in.txt') as f:
  lines = f.read()


data = [ float(x) for x in lines.split('\n') if x]

increases = 0
for i in range(1, len(data)):
  increases += data[i] > data[i-1]
print(increases)

increases = 0
for i in range(3, len(data)):
  old = sum( data[i-3:i] )
  new = sum( data[i-2:i+1] )
  increases += new > old
print(increases)


