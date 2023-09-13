#!/usr/bin/env python3

class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h_left, h_right = height[left], height[right]
            width = right - left
            current_area = min(h_left, h_right) * width
            max_area = max(max_area, current_area)

            if h_left < h_right:
                left += 1
            else:
                right -= 1

        return max_area