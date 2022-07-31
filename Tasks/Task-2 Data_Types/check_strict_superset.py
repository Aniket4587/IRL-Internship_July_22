a = set(input().split())
counter , n = 0, int(input())
for i in range (n):
        b = set(input().split())
        if a.issuperset(b) :
                counter += 1
print(counter == n)
