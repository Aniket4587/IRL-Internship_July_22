
N = int(input())
lst = []
for i in range(N):
    country = input()
    lst.append(country)
lst_set = (len(set(lst)))
print(lst_set)
