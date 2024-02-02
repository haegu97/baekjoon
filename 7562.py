import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
q = deque()

def bfs(a, b):
  q.append((a, b))
  visited[a][b] = True
  while q:
    x, y = q.popleft()
    if x == goal_x and y == goal_y:
      return 0
    
    dx, dy = [-2,-1,1,2,-2,-1,1,2], [1,2,2,1,-1,-2,-2,-1]
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
        q.append((nx, ny))
        visited[nx][ny] = True
        graph[nx][ny] = graph[x][y] + 1
      if nx == goal_x and ny == goal_y:
        visited[nx][ny] = True
        return graph[x][y] + 1

T = int(input())
for _ in range(T):
  n = int(input())
  cur_x, cur_y = map(int, input().split())
  goal_x, goal_y = map(int, input().split())
  graph = [[0]*n for _ in range(n)]
  visited = [[False]*n for _ in range(n)]
  answer = bfs(cur_x,cur_y)
  print(answer)