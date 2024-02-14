import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
tree_arr = list(map(int, input().split()))

lt, rt = 1, max(tree_arr)

while lt <= rt:
  mid = (lt+rt) // 2
  cur = 0
  for tree in tree_arr:
    if tree - mid >= 0:
      cur += (tree-mid)
  if cur >= m:
    lt = mid + 1
  else:
    rt = mid - 1
print(rt)