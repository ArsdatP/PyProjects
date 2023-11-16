def binary_search(x, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(x) -1

    if high < low:
        return -1
    
    x = sorted(x)
    midpoint = (low + high) // 2

    if x[midpoint] == target:
        return midpoint
    elif target < x[midpoint]:
        return binary_search(x, target, low, midpoint-1)
    else:
        return binary_search(x, target, midpoint+1, high)
    

if __name__ == '__main__':
    x = [2, 8, 1, 15, 10, 15, 22]
    target = 22
    print(binary_search(x, target))