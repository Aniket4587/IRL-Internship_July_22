n=int(input())
arr = list(map(int,input().split()))[:n]
arr_sort = sorted(list(set((arr))))

print(arr_sort[-2])
