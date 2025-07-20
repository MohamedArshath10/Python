def binary_search():
    nums = [-1, 0, 3, 5, 9 ,12]
    target = 10
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start + end) // 2
        num = nums[mid]
        if num == target:
            return mid
        elif num < target:
            start = mid + 1
        elif num > target:
            end = mid - 1
    return -1

print(binary_search())