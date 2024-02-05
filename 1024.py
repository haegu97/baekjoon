n, l = map(int, input().split())

for i in range(l, 101):
  x = n/i - (i+1)/2
  if x == int(x):
    x = int(x)
    if x + 1 >= 0:
      for j in range(x+1, x+i+1):
        print(j, end = " ")
else:
      print(-1)