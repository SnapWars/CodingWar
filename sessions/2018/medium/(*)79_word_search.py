class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.h = len(board)
        self.w = len(board[0])
        self.l = len(word)
        self.board = board
        self.word = word
        self.adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(self.h):
            for j in range(self.w):
                if self.dfs(i, j, 0):
                    return True
        return False

    def dfs(self, r, c, index=0):
        if index == self.l:
            return True

        if r < 0 or r >= self.h or c < 0 or c >= self.w or self.board[r][c] != self.word[index]:
            return False

        temp = self.board[r][c]
        self.board[r][c] = '#'

        for dx, dy in self.adj:
            if self.dfs(r + dx, c + dy, index + 1):
                return True
        self.board[r][c] = temp
        return False
