nums = [1,0,0,2,3,0,5]
i = 0
for j in range(len(nums)):
    if nums[j] != 0:
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
print(nums)