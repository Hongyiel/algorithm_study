
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        print(lo)
        print(hi)
        print("-------")
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [3, 1, 2, 33, 9, 11, 7]
mylist.sort()
print(mylist)
print(bisect(mylist, 6))