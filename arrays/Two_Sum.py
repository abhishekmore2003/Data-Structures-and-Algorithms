nums = [-16, 1, 7, 11, 15]
target = 9


def find_index():
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

    return "No pair found"

result = find_index()

print("result = ",result)
        