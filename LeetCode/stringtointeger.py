#!/usr/bin/env python3

class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        i = 0

        s = s.lstrip()

        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return sign * (2**31 - 1) if sign == 1 else sign * (2**31)
            result = result * 10 + digit
            i += 1

        return sign * result