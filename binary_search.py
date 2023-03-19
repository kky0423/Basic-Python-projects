import random
import time


def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low  == None:
        low = 0
    if high == None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2
    
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l[low:midpoint-1], target)
    else:
        return binary_search(l[midpoint+1:high], target)
    
if __name__ == '__main__':
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()

    print(f'Naive search took {(end-start)/length}s.')

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()

    print(f'Binary search took {(end-start)/length}s.')