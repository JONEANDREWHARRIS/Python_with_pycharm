def sort (nums):
    for i in range(5):
        min_pos =i
        for j in range(i,6):
            if nums[j]<nums[min_pos]:
                min_pos =j

        temp =nums[i]
        nums[i] =nums[min_pos]
        nums[min_pos] = temp

        print(nums)

nums = [5,3,8,6,7,2]
6
sort(nums)
print(nums)