def backtracking(num):
  global ans
  if num == n:
    ans += 1
    return

  for i in range(n):
    if v1[i] == v2[i+num] == v3[num-i] == 0:
      v1[i] = v2[i+num] = v3[num-i] = 1
      backtracking(num+1)
      v1[i] = v2[i+num] = v3[num-i] = 0


n = int(input())
ans = 0
v1 = [0] * n
v2 = [0] * (2*n)
v3 = [0] * (2*n)

backtracking(0)
print(ans)