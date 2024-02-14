import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, w = map(int, input().split())
  graph[a].append((b, w))
st, ed = map(int, input().split())
distance = [[int(1e9)]*(n+1)]

def dijkstra(start):
  distance[start] = 0
  q = [(0, st)]

  while q:
    w, cur = heapq.heappop(q)
    if distance[cur] < w:
      continue

    for destination, weight in graph[cur]:
      