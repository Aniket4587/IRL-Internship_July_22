a = int(input())
a_set = set(list(map(int,input().split()))[:a])

b=int(input())
b_set = set(list(map(int,input().split()))[:b])

res_set = a_set.union(b_set)
print(len(res_set))
