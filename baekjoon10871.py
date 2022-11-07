a, b = map(int, input().split())

list = list(map(int, input().split()))
for i in range(a):
    if list[i] < b:
        print(list[i], end=" ")