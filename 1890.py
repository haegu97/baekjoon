import sys
sys.stdin = open("input.txt", "r")

ans = 0
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    if graph[i][j] == 0:
      break
    if i + graph[i][j] < n:
      dp[i+graph[i][j]][j] += dp[i][j]
    if j + graph[i][j] < n:
      dp[i][j+ graph[i][j]] += dp[i][j]
print(dp[n-1][n-1])