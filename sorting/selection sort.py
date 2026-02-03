'''def selection_sort_naive(arr):
    n=len(arr)
    for i in range(n):
        temp=i
        #Here you can directly use the  i,j
        for j in range(i+1,n):
            if arr[j]<arr[temp]:
                temp=j

        arr[i],arr[temp]=arr[temp],arr[i]
    return arr

arr=[20,19,18,17]
selection_sort_naive(arr)
print(arr)
'''

'''
def selection_sort_better(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        temp=arr[i]
        arr[i]=arr[min_index]
        arr[min_index]=temp

    return arr

arr=[20,19,18,17]
selection_sort_better(arr)
print(arr)
'''
def selection_sort_optimal(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        if arr[min_index]!=arr[i]:
            arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr

arr=[20,19,18,16]
selection_sort_optimal(arr)
print(arr)