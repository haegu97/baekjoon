#n = int(input())
#n_list = list(map(int, input().split()))
#print(min(n_list),max(n_list))

n = int(input())

n_list = list(map(int, input().split()))
n_list.sort()
print(n_list[0],n_list[-1])