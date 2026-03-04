def two_sum():
    nums=[2,7,15,6]
    target=17
    n=len(nums)
    nums_map={}
    for i in range(n):
        compliment=target-nums[i]
        nums_map[compliment]=i
        #{number : index}
        #num_map[key] = value
        if nums[i] in nums_map:
            return [nums_map[nums[i]],i]
    return [-1,-1]
print(two_sum())
