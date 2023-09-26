#!/usr/bin/env python3

class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        else:
            previous_sequence = self.countAndSay(n - 1)
            result = ""
            count = 1

            for i in range(len(previous_sequence)):
                if i + 1 < len(previous_sequence) and previous_sequence[i] == previous_sequence[i + 1]:
                    count += 1
                else:
                    result += str(count) + previous_sequence[i]
                    count = 1

            return result
