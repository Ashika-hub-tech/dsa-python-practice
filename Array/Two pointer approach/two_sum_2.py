def two_sum():
    nums=[2,6,7,8]
    target=9
    left=0
    right=len(nums)-1
    while left<right:
        total=nums[left]+nums[right]
        if total==target:
            return[left,right]
        elif total<target:
            left+=1
        else:
            right-=1
    return None
print(two_sum())


'''
Two pointer logic assumes:
Left side → smaller values
Right side → larger values

That assumption is only true when array is sorted.
Without sorting:
You lose the guarantee
Pointer movement becomes meaningless

| Array Type | Best Approach      |
| ---------- | ------------------ |
| Sorted     | Two Pointer (O(n)) |
| Unsorted   | HashMap (O(n))     |

'''