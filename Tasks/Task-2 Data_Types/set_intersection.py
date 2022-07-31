a = int(input())
a_set = set(list(map(int,input().split()))[:a])

b= int(input())
b_set = set(list(map(int,input().split()))[:b])

intersection_set = a_set.intersection(b_set)
print(len(intersection_set))
