# def factorial(num):
#     fact=1
#     if (num<0):
#          print("Factorial does not exist for the negative number")
#     elif(num==0):
#          print("Factorial of 0 is 1")
#     else:
#         for i in range(1,num+1):
#             fact=fact*i
#         return fact
#
# num=int(input("Enter number:"))
# print("Factorial is:" , factorial(num))

#Using Recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

# Driver code
num=5
print("Factorial of ", num,"is:",factorial(num))


# Ternary Operator
# def factorial(n):
#     return 1 if(n==0 or n==1) else n * factorial(n-1)
#
# num=5
# print("Factorial of ", num,"is:",factorial(num))
