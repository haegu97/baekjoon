from collections import deque

def bfs():
  q = deque()
  q.append(n)
  while q:
    x = q.popleft()
    if x == k:
      print(dist[x])
    for j in (x-1,x+1,2*x):
      if 0 <= j <= max and not dist[j]:
        dist[j] = dist[x] + 1
        q.append(j)


max = 100000
n, k =map(int, input().split())
dist = [0] * (max+1)

bfs()