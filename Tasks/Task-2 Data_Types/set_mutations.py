N = int(input())
s1 = set(list(map(int,input().split()))[:N])
no_op =int(input())

for i in range(no_op):
    cmd, _ = input().split()
    s2 = set(map(int,input().split()))
    if (cmd=="intersection_update"):
        s1.intersection_update(s2)
    elif (cmd == "update"):
        s1.update(s2)
    elif (cmd == "symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif (cmd=="difference_update"):
        s1.difference_update(s2)
print(sum(s1))        
