def two_sum():
    nums=[2,4,5,9]
    n=len(nums)
    target=7
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return[i,j]
    return [-1,-1]
print(two_sum())