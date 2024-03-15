import sys
sys.stdin = open("input.txt",'r')

n = int(input())
arr = []
for _ in range(n):
  a, b = map(int, input().split())
  arr.append((a, b))

arr.sort(key = lambda x : (x[1], x[0]))

cnt = 0
last = 0

for start, end in arr:
  if start >= last:
    cnt += 1
    last = end

print(cnt)