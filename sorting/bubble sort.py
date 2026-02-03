'''
def bubble_sort_naive(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if (arr[j]<arr[i]):
               temp=arr[i]
               arr[i]=arr[j]
               arr[j]=temp
    return arr

arr=[5,1,7,3,40,38]
bubble_sort_naive(arr)
print(arr)
'''

'''def bubble_sort_better(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[5,1,7,3,40,38]
bubble_sort_better(arr)
print(arr)
'''

def bubble_sort_optimal(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

arr=[5,1,7,3,40,38]
bubble_sort_optimal(arr)
print(arr)





