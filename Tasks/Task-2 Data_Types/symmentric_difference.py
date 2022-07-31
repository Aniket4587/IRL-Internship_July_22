m = int(input())
m_ele = list(map(int,input().split()))[:m]
m_set = set(m_ele)

n = int(input())
n_ele = list(map(int,input().split()))[:n]
n_set = set(n_ele)

sy_diff = m_set.symmetric_difference(n_set)

sy_diff_set = list(sy_diff)
for i in sorted(sy_diff_set):
    print(i)
