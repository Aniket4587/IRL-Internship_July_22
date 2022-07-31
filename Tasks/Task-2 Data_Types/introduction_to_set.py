from __future__ import division

def average(array):
    # your code goes here
    arr_1 = set(arr)
    arr_2 = list(arr_1)
    avg = (sum(arr_2)/len(arr_2))
    return avg

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result
