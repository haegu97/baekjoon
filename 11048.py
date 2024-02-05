import sys
sys.stdin = open('input.txt', 'r')
column, row = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(column)]
dp = [[0]*row for _ in range(column)]
dp[0][0] = graph[0][0]

for i in range(1, row):
  dp[0][i] = dp[0][i-1] + graph[0][i]

for j in range(1, column):
  dp[j][0] = dp[j-1][0] + graph[j][0]

for i in range(1,column):
  for j in range(1,row):
    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + graph[i][j]
print(dp[column-1][row-1])