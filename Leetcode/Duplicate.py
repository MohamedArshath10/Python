def duplicate(nums):
    new_num = []
    right = len(nums) - 1
    while right >= 0:
        if nums[right] not in new_num:
            new_num.append(num[right])
            nums.pop()
            right -= 1
        if nums[right] in new_num:
            nums.pop()
            right -= 1
    new_num.reverse()
    
num = [1,1,2,3,3,4,5,5]
duplicate(num)