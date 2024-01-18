import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = [0]
for _ in range(n):
  arr.append(int(input()))

dp = [0] * (n+1)

dp[1] = arr[1]
if n >= 2:
  dp[2] = arr[1]+arr[2]
for i in range(3,n+1):
    dp[i] = max((arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3]))
print(dp[n])