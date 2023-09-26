#!/usr/bin/env python3

class Solution:
    def combinationSum2(self, candidates, targets):
        def backtrack(start, targets, path):
            if targets == 0:
                result.append(path)
                return
            if targets < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                backtrack(i + 1, targets - candidates[i], path + [candidates[i]])

        candidates.sort()
        result = []
        backtrack(0, targets, [])
        return result