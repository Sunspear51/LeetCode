#!/usr/bin/env python3

class Solution:
    def is_palindrome(self, x):
        x_str = str(x)
    
        return x_str == x_str[::-1]