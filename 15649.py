n, m = map(int, input().split())
arr = []
visited = [False] * (n+1)

def recur(num):
    if num == m:
      print(" ".join(map(str, arr)))
      return
    for i in range(1, n+1):
      if visited[i] == False:
        visited[i] = True
        arr.append(i)
        recur(num+1)
        visited[i] = False
        arr.pop()

recur(0)