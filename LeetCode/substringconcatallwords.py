#!/usr/bin/env python3

from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = word_length * len(words)
        word_count = Counter(words)
        result = []

        for i in range(word_length):
            left, right = i, i
            window_words = Counter()

            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length

                if word in word_count:
                    window_words[word] += 1

                    while window_words[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        left += word_length
                        window_words[left_word] -= 1

                    if right - left == total_length:
                        result.append(left)

                else:
                    left = right
                    window_words.clear()

        return result