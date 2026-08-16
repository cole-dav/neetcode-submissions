class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(index,r,c):
            if index == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[index] or (r,c) in visited:
                return False
            visited.add((r,c))
            res = (dfs(index+1,r,c-1) or
                   dfs(index+1,r-1,c) or
                   dfs(index+1,r,c+1) or
                   dfs(index+1,r+1,c))
            visited.remove((r,c))
            return res
        for row in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0,row,c):
                    return True
        return False