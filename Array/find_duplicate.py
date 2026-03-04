def find_duplicate(arr):
    result = []
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
               temp=arr[j]
               arr[j]=arr[i]
               arr[i]=temp

    for i in range(n-1):
        if (arr[i+1]==arr[i]):
            result.append(arr[i])
    return result

arr=[6,2,3,2,7,6]
print(find_duplicate(arr))

