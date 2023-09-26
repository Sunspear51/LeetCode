#!/usr/bin/env python3

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        unique_count = 1  # Initialize with the first element (already unique)
    
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_count] = nums[i]
                unique_count += 1

        return unique_count
