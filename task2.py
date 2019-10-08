sum = 0
x = prevX = 1
while x < 4000000:
  x, prevX = x + prevX, x
  if (x % 2 == 0): sum += x
print(sum)