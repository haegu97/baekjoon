import sys
sys.stdin = open('input.txt', 'r')
n, k = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))
lt, rt = 1, max(arr)
while lt <= rt:
  mid = (lt+rt) // 2
  cnt = 0
  for line in arr:
    cnt += (line // mid)
  if cnt < k:
    rt = mid - 1
  else:
    lt = mid + 1
print(rt)