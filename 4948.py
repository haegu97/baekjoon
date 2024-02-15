import math
import sys
sys.stdin = open('input.txt', 'r')

m = 123456

array = [True for _ in range(2 * m + 1)]
array[0], array[1] = False, False

for i in range(2, int(math.sqrt(2*m)+1)):
  if array[i]:
    j = 2
    while i * j <= 2 * m:
      array[i * j] = False
      j += 1
while True:
  n = int(input())
  if n == 0:
    break

  count = 0

  for i in range(n+1, 2 *n + 1):
    if array[i]:
      count += 1
  print(count)