import sys
sys.stdin = open('input.txt', 'r')


N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
ans = []

def dfs(start):
  global cnt
  if len(ans) > 0 and sum(ans) == 0:
    cnt += 1
  
  for i in range(start, N):
    ans.append(num[i])
    dfs(i+1)
    ans.pop()

dfs(0)
print(cnt)