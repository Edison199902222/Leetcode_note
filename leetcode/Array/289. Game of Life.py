'''
// mark die -> live: -1
    // mark live -> die: 2

思路就是 先遍历 把每个位置的领据活着的数量算出来
然后 如果这个位置 是活着的话 那么邻居活着的数量超过三个 或者小于两个就要死 计为2
如果这个位置是死了 那么如果活着的邻居等于3的话 那就是活了
最后再update全局
'''

class Solution:
    def __init__(self):
        self.direction = [[0,-1],[0,1],[1,0],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:return
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    live = self.count(board,i,j)
                    if live > 3 or live < 2:
                        board[i][j] = 2
                if board[i][j] == 0:
                    live = self.count(board, i, j)
                    if live == 3:
                        board[i][j] = -1
        self.update(board)
    def update(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0
    def count(self,board,i,j):
        res = 0
        for index in self.direction:
            newrow = i + index[0]
            newcol = j + index[1]
            if newrow >= 0 and newrow < len(board) and newcol>=0 and newcol<len(board[0]) and (board[newrow][newcol]==1 or board[newrow][newcol] == 2):
                res+=1
        return res
if __name__ == "__main__":
    solution = Solution()
    print(solution.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
