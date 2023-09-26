#!/usr/bin/env python3

class Solution:
    def removeElement(self, nums, val):
        current = 0
        last_valid = 0
    
        while current < len(nums):
            if nums[current] != val:
                nums[last_valid] = nums[current]
                last_valid += 1
            current += 1
    
        return last_valid