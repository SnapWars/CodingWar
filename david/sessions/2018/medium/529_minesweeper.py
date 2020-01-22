class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.board = board
        self.w = len(board[0])
        self.h = len(board)
        self.click = click
        self.visited = set()

        self.ff(click[0], click[1])

        return self.board

    def get(self, r, c):
        if (r, c) in self.visited:
            return self.board[r][c]

        if r < 0 or r >= self.h or c < 0 or c >= self.w:
            return None
        return self.board[r][c]

    def ff(self, r, c):
        val = self.get(r, c)
        if not val or (r, c) in self.visited:
            return

        self.visited.add((r, c))

        if r == self.click[0] and c == self.click[1] and val == 'M':
            self.board[r][c] = 'X'
            return

        num_mines = 0
        for i in xrange(r-1, r+2):
            for j in xrange(c-1, c+2):
                if self.get(i, j) == 'M':
                    num_mines += 1

        if num_mines > 0:
            self.board[r][c] = str(num_mines)
            return

        for i in xrange(r-1, r+2):
            for j in xrange(c-1, c+2):
                self.ff(i, j)

        if val == 'E':
            self.board[r][c] = 'B'
