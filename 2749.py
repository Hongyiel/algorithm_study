function = [0,1]
i = 1
while True:
    i+=1
    function.append((function[i-1]+function[i-2])%1000000)
    if function[i] == 1:
        if function[i-1] == 0:
            break
n = int(input())
print(function[n%(i-1)])