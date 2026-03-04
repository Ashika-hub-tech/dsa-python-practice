#GFG Solution
class Solution:
    def rotate(self, arr):
        n = len(arr)
        if n == 0:
            return arr

        last = arr[n - 1]
        for i in range(n - 1, 0, -1):
            #First value is going to be changed however,So we are changing it in this way
            arr[i] = arr[i - 1]
        arr[0] = last
        return arr
arr=[1,2,3,4]
sol=Solution()
print(sol.rotate(arr))