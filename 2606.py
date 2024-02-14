import sys
sys.stdin = open('input.txt', 'r')


from collections import deque
q = deque()

n = int(input())
network = int(input())

graph = [[]for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(network):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(i):
  cnt = 0
  q.append(1)
  visited[i] = True
  while q:
    x = q.popleft()
    for nx in graph[x]:
      if visited[nx] == False:
        visited[nx] = True
        q.append(nx)
        cnt += 1
  return cnt

print(bfs(1))