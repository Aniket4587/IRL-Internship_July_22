a = int(input())
a_set = set(list(map(int,input().split()))[:a])

b= int(input())
b_set = set(list(map(int,input().split()))[:b])

diff_set = a_set.difference(b_set)
print(len(diff_set))
