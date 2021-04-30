answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
# 0인지 아닌지 구분 한것
    print(idx, value)

    if(idx== N and target == value):
        print(idx, value)
        answer += 1
        return
    if(idx == N):
        print(value)
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    print("End of first dFS: idx is : ", idx, value)
    DFS(idx+1,numbers,target,value-numbers[idx])
    print("End of second dFS: idx is : ", idx)
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer


numbers = [1,1,1,1,1]
print(solution(numbers, 3))