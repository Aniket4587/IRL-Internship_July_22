a = int(input())
a_set = set(list(map(int,input().split()))[:a])

b= int(input())
b_set = set(list(map(int,input().split()))[:b])

sym_diff_set = a_set.symmetric_difference(b_set)
print(len(sym_diff_set))
