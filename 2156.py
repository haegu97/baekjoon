import sys
input = sys.stdin.readline
sys.stdin = open("input.txt", "r")

n = int(input())
arr = [0]
dp = [0] * (n+1)

for _ in range(n):
  arr.append(int(input()))

dp[1] = arr[1]

if n >= 2:
  dp[2] = arr[1] + arr[2]

  for i in range(3, n+1):
    case_1 = dp[i-1]
    case_2 = arr[i] + dp[i-2]
    case_3 = arr[i] + arr[i-1] + dp[i-3]

    dp[i] = max(case_1, case_2, case_3)
print(dp[n])