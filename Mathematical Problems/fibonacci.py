# def fibonacci(num):
#     n1 = 0
#     n2 = 1
#     print(n1)
#     print(n2)
#     for i in range(2,num+1):
#         sum = n1 + n2
#         print(sum)
#         n1 = n2
#         n2 = sum
#
#
# num=int(input("Enter num:"))
# print(fibonacci(num))

#Optimzed ,TO PRINT THE FIRST N fibonacci Numbers
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b

n=int(input("Enter num:"))
fibonacci(n)
# Time: O(n)
# Loop runs n times.
# Space: O(1)
# Uses only constant variables (n1, n2, sum).