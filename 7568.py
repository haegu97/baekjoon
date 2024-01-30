import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
arr = []
answer = []
for _ in range(n):
  x, y = map(int, input().split())
  arr.append((x, y))

for i in arr:
  rank = 1
  for j in arr:
    if i[0] < j[0] and i[1] < j[1]:
      rank += 1
  answer.append(rank)

for i in answer:
  print(i, end = ' ')