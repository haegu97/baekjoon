import sys
sys.stdin = open("input.txt",'r')

n = int(input())

arr = []
for _ in range(n):
  a, b = map(int, input().split())
  arr.append((a, b))

arr.sort()

for ans in arr:
  print(ans[0],ans[1])