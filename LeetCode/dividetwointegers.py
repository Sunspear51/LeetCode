#!/usr/bin/env python3

class Solution:
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
    
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
    
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
    
        positive_result = (dividend > 0) == (divisor > 0)
    
        dividend, divisor = abs(dividend), abs(divisor)
    
        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
    
        return quotient if positive_result else -quotient
