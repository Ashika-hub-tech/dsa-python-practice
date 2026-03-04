class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        total_sum = ((n + 1)*(n+2)) // 2
        actual_sum = sum(arr)
        return total_sum - actual_sum
arr=[2,3,4]
sol=Solution()
print(sol.missingNumber(arr))


