def bubble_sort(n, nums):
    for i in range(n):
        for j in range(0, n - i - 1):
            digit_1 = nums[j] + nums[j + 1]
            digit_2 = nums[j + 1] + nums[j]
            if digit_1 < digit_2:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return "".join(nums)


n = 3
nums = ["1", "5", "4"]
print(bubble_sort(n, nums))
