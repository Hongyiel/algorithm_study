arr = [int(x) for x in input().strip().split()]
a = arr[0]
b = arr[1]
c = arr[2]
d = arr[3]
e = arr[4]
f = arr[5]
invaild_case = a * e - d * b
if invaild_case == 0:
    exit(0)
else:
    x_result = (e*c-b*f)/(a*e-b*d)
    y_result = (a*f-d*c)/(a*e-b*d)
if x_result <= 999 and x_result >= -999 and y_result <= 999 and y_result >= -999:
    print(int(x_result), int(y_result))
else:
    exit(0)
