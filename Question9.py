def has_pair_with_sum(nums, target_sum):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                return True
    return False

numbers = [10, 15, 3, 7]
target = 17
result = has_pair_with_sum(numbers, target)
print(result)
