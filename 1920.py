import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()


for num in arr2:
  lt, rt = 0, n-1
  flag = False

  while lt <= rt:
    mid = (lt+rt) // 2
    if num == arr1[mid]:
      flag = True
      print(1)
      break
    elif num > arr1[mid]:
      lt = mid + 1
    else:
      rt = mid - 1
  if flag == False:
    print(0)