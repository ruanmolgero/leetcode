from typing import List

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # current = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0] == board[r][c]:
                    
                    
                    
                    print(f"sim {word[0]}")
                    
    def next(self, r, c, w):
        for 

Solution().exist(board, word)