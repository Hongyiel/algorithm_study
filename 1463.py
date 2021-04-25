# import sys
# #1463
#
# def div_three(x_num):
#     x_num = x_num/3
#     return x_num
#
# def div_two(x_num):
#     x_num = x_num/2
#     return x_num
#
# def min_one(x_num):
#     x_num = x_num-1
#     return x_num-1
#
# x = sys.stdin.readline()
# x_num = int(x)
# count = 0
# while x_num > 1:
#     num = x_num % 3
#     if num == 0:
#         x_num = div_three(x_num)
#         count = count + 1
#     elif num == 1:
#         x_num = div_two(x_num)
#         count = count + 1
#     else:
#         x_num = min_one(x_num)
#         count = count + 1
#
# print(count)

a=int(input())
dp=[0]*1000001
dp[0]=dp[1]=0
for i in range(2,a+1):
    dp[i]=dp[i-1]+1
    if(i%2==0):
        dp[i]=min(dp[i],dp[i//2]+1)
    if(i%3==0):
        dp[i]=min(dp[i],dp[i//3]+1)
print(dp[a])
