import sys
sys.stdin = open("input.txt", "r")
from collections import deque
q = deque()
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)] 


def bfs(i,j):
  q.append((i,j))
  visited[i][j] = True
  cnt = 0
  while q:
    x, y = q.popleft()
    dx, dy = [1,-1,0,0], [0,0,-1,1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
        cnt += 1
        visited[nx][ny] = True
        q.append((nx, ny))
  return cnt

answer_list = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == False:
      answer = bfs(i, j)
      answer_list.append(answer)

print(len(answer_list))
answer_list.sort()
for i in answer_list:
  print(i+1)