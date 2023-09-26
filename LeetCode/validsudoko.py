#!/usr/bin/env python3

class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
            
                if cell in rows[i]:
                    return False
                rows[i].add(cell)
            
                if cell in cols[j]:
                    return False
                cols[j].add(cell)
            
                box_idx = (i // 3) * 3 + j // 3
                if cell in boxes[box_idx]:
                    return False
                boxes[box_idx].add(cell)
    
        return True