#!/usr/bin/env python3

class Solution:
    def letterCombinations(self, digits):
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    

        def generate_combinations(current, remaining_digits):
            if not remaining_digits:
                combinations.append(current)
            else:

                next_digit = remaining_digits[0]
                letters = digit_to_letters[next_digit]
            
                for letter in letters:
                    generate_combinations(current + letter, remaining_digits[1:])
    
        combinations = []
    
        if digits:
            generate_combinations('', digits)
    
        return combinations