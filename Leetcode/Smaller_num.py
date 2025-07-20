# How many numbers are smaller than the current number
def smaller_num():
    nums = [8,1,2,5,3]
    final_num = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if (nums[i] > nums[j]):
                count += 1
        final_num.append(count)
    return final_num

print(smaller_num())