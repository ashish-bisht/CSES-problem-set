def increasing_array(nums):
    min_turns = 0

    last_num = nums[0]

    for num in nums:
        if last_num > num:
            min_turns += last_num - num
        last_num = num

    return min_turns


print(increasing_array([3, 2, 5, 1, 7]))
