import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
num_arr = list(map(int, input().split()))
answer, start, end = 0, 0, 0

while end < n:
  num_sum = sum(num_arr[start : end + 1])

  if num_sum == m:
    answer += 1
    end += 1
  
  elif num_sum > m:
    start += 1
  
  else:
    end += 1

print(answer)