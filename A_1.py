#test
def compare(arr):
    count = 0
    for i in range(6):
        if arr[i] >= -999 and arr[i] <= 999:
            count = count + 1
        else:
            count = count - 1
    return count

# start problem
arr = [int(x) for x in input().strip().split()]
count_result = 0
if len(arr) == 6:
    count_result = compare(arr) # if count_result is not 6 then ERROR
else:
    exit(0)
if count_result == 6: # this will be making equation
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]
    e = arr[4]
    f = arr[5]
    # i.e) x + 2y = 3
    #      4x+ 5y = 6
    if a != d:
        if b == 0 and e == 0:
            exit(0)
        if a == 0:
            y_result = c / b
            x_result = (f - e * y_result) / d
        elif b == 0:
            x_result = c / a
            y_result = (f - e * y_result) / d
        else:
            a_tmp = a * d
            b_tmp = b * d
            c_tmp = c * d

            d_tmp = d * a
            e_tmp = e * a
            f_tmp = f * a

            y_tmp = b_tmp - e_tmp
            y_tmp_result = c_tmp - f_tmp

            y_result = y_tmp_result/y_tmp

            x_result = (c - b * y_result)/a
    elif a == d:
        if a == 0 and d == 0:
            exit(0)
        if b == 0 and e == 0:
            exit(0)
        y_tmp = b - e
        if y_tmp != 0:
            y_tmp_result = c - f

            y_result = y_tmp_result/y_tmp

            x_result = (c - b * y_result)/a
        # ERROR CASE 1
        # i.e) x + 2y = 3
        #      x + 2y = 4
        elif y_tmp == 0:
            if c != f:
                exit(0)
            else:
                x_result = 0
                y_result = 0
if x_result <= 999 and x_result >= -999 and y_result <= 999 and y_result >= -999:
    print(int(x_result), int(y_result))
else:
    exit(0)
