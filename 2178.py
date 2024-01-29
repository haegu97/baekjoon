from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
q = deque()
n, m = map(int, input().split())
graph = [list(map(int, input()))for _ in range(n)]

def bfs():
  visited = [[0]*m for _ in range(n)]
  q.append((0,0))
  visited[0][0] = 1

  while q:
    x, y = q.popleft()
    if (x, y) == (n-1, m-1):
      return visited[x][y]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
        q.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1

ans = bfs()
print(ans)