import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
q = deque() 

column, row = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(column)]
visited = [[False]*row for _ in range(column)]
cnt = 0
arr = []

def bfs(i, j):
  house_cnt = 1
  q.append((i,j))
  visited[i][j] = True
  while q:
    x, y = q.popleft()
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < column and 0 <= ny < row and visited[nx][ny] == False and graph[nx][ny] == 1:
        q.append((nx, ny))
        visited[nx][ny] = True
        house_cnt += 1
  return house_cnt
  


for i in range(column):
  for j in range(row):
    if visited[i][j] == False and graph[i][j] == 1:
      tmp = bfs(i, j)
      arr.append(tmp)
      cnt += 1
print(cnt)
if len(arr) == 0:
  print(0)
else:
  print(max(arr))