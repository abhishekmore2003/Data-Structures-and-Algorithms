# nums = [0, 1, 0, 3, 12]

# target = 0
# got_zero = False

# for j in range(len(nums)):
#     if nums[j] == 0 and got_zero == False :
#         target = j
#         got_zero = True

#     if nums[j] != 0 and got_zero:
#         temp = nums[j]
#         nums[j] = nums[target]
#         nums[target] = temp
#         target += 1

# print(nums)

nums = [2, 1, 0, 3, 12]

target = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[target] = nums[target], nums[i]
        target += 1

print(nums)
