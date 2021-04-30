def binary_search(array, target):
    '''Binary Search Algorithm
        - input : list of numbers
        - return :
            if exist return list(target) index
            if doesn't exist return Not Found'''
    array.sort()
    head = 0
    tail = len(array) - 1
    
    while tail - head >= 0:
        center = int((head + tail) / 2)
        if array[center] == target:
            return center
        elif array[center] < target:
            head = center + 1
        elif array[center] > target:
            tail = center - 1
    return 'Not Found'

array = [13, 11, 19, 17, 29, 31, 23]
idx = binary_search(array, 17)
print(idx)
print('{} 번째의 index와 일치'.format(idx))


# 출처: https://excelsior-cjh.tistory.com/124 [EXCELSIOR]