
'''
def selection_sort_naive(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

arr=[2,1,5,4,3]
print(selection_sort_naive(arr))

def selection_sort_better(arr):
    n = len(arr)
    for i in range(n):
        min_pos=i
        for j in range(i+1,n):
            if arr[j]<arr[min_pos]:
                min_pos=j
        arr[i],arr[min_pos]=arr[min_pos],arr[i]
        print(arr)
    return arr

arr=[2,1,8,6,4]
print(selection_sort_better(arr))
'''

def selection_sort_optimal(arr):
    n = len(arr)
    for i in range(n):
        min_pos=i
        for j in range(i+1,n):
            if arr[j]<arr[min_pos]:
                min_pos=j

            if min_pos!=i:
                arr[i],arr[min_pos]=arr[min_pos],arr[i]
    return arr

arr=[9,12,56,76,2]
print(selection_sort_optimal(arr))