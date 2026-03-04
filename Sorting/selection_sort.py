def selection_sort_better(arr):
    n=len(arr)
    for i in range(n):
        min_pos=i
        for j in range(i+1,n):
            if arr[j]<arr[min_pos]:
                min_pos=j
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
    return arr

arr=[4,2,6,5]
selection_sort_better(arr)
print(arr)