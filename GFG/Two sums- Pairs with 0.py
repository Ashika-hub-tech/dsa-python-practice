def get_pairs(arr):
    n = len(arr)

    # sorting
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

    left = 0
    right = n - 1
    result = []

    while left < right:

        s = arr[left] + arr[right]

        if s == 0:
            result.append([arr[left], arr[right]])

            left_val = arr[left]
            right_val = arr[right]

            while left < right and arr[left] == left_val:
                left += 1

            while left < right and arr[right] == right_val:
                right -= 1

        elif s < 0:
            left += 1
        else:
            right -= 1

    return result


arr = [4, 2, 7, -4]
print(get_pairs(arr))