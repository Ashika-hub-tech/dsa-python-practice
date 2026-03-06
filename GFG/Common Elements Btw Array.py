def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

def common_element(arr1,arr2,arr3):
    arr1=sort(arr1)
    arr2=sort(arr2)
    arr3=sort(arr3)
    i=j=k=0
    result=[]
    n1=len(arr1)
    n2=len(arr2)
    n3=len(arr3)
    while i<n1 and j<n2 and k<n3:
        if(arr1[i]==arr2[j]==arr3[k]):
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr3[k]:
            j+=1
        else:
            k+=1

    if not result:
            return [-1]
    return result

arr1=[1,7,2,3]
arr2=[2,7,9,10]
arr3=[7,2,8]
print(common_element(arr1,arr2,arr3))

