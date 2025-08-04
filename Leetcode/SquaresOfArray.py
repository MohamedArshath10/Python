def squares_of_array(arr):
    left = 0
    right = len(arr) - 1
    result = []
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result.append(arr[left] ** 2)
            left += 1
        else:
            result.append(arr[right] ** 2)
            right -= 1

    # result.reverse()
    return result
print(squares_of_array([-4, -1, 0, 3, 10]))