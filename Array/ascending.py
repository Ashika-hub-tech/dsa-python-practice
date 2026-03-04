nums=list(map(int,input("Enter the numbers separated by space:").split()))
n=len(nums)
for i in range(n):
    for j in range(0,n-i-1):
        if(nums[j]<nums[j+1]):
            num[j],nums[j+1]=nums[j+1],nums[j]

print("Numbers in Descending:", nums)