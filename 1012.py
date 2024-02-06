from collections import deque
q = deque()
import sys
sys.stdin = open('input.txt', 'r')

t = int(input())


def bfs(x, y):
  q.append((x, y))
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < column and 0 <= ny < row and visited[nx][ny] == False and graph[nx][ny] == 1:
        q.append((nx, ny))
        visited[nx][ny] = True


for _ in range(t):
  row, column, cabbage = map(int, input().split())
  cnt = 0
  visited = [[False]*row for _ in range(column)]
  graph = [[0]*row for _ in range(column)]
  
  for _ in range(cabbage):
    x, y = map(int, input().split())
    graph[y][x] = 1
  for i in range(column):
    for j in range(row):
      if graph[i][j] == 1 and visited[i][j] == False:
        bfs(i, j)
        cnt += 1
  print(cnt)