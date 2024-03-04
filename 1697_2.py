from collections import deque
q = deque()

n, k = map(int, input().split())
max = 100000

def bfs(start):
  visited = [0] * max
  q.append(start)
  while q:
    x = q.popleft()
    if x == k:
      return visited[x]
    else:
      nx = [x+1, x-1, x*2]
      for i in nx:
          if 0 <= i <= max and visited[i] == 0:
            visited[i] = visited[x] + 1
            q.append(i)

ans = bfs(n)
print(ans)