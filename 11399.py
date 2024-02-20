n = int(input())
arr = list(map(int, input().split()))

cur = 0
arr.sort()
num_arr = []
for num in arr:
  cur += num
  num_arr.append(cur)
print(sum(num_arr))