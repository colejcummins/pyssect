x = 0
while x > 10:
  x += 1
  if x % 2 == 0:
    x *= 2
  if x == 7:
    continue
print(x)