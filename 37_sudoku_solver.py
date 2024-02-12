from collections import defaultdict
from test_harness.harness import harness_run

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # back tracking approach
        # keep records of columns, rows, and squares to exit early
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    row[i].add(int(board[i][j]))
                    col[j].add(int(board[i][j]))
                    square[(i // 3, j // 3)].add(int(board[i][j]))
        

        def valid(i, j, n):
            if n in row[i]:
                return False
            if n in col[j]:
                return False
            if n in square[(i // 3, j // 3)]:
                return False
            return True


        def dfs(i, j):
            nxt = i * 9 + j
            nxt += 1
            while nxt < 81:
                nxti = nxt // 9
                nxtj = nxt % 9
                if board[nxti][nxtj] == '.':
                    break
                nxt += 1

            for n in range(1, 10):
                if valid(i, j, n):
                    row[i].add(n)
                    col[j].add(n)
                    square[(i // 3, j // 3)].add(n)
                    board[i][j] = str(n)

                    if nxt >= 81:
                        return True
                    if dfs(nxti, nxtj):
                        return True
                    row[i].remove(n)
                    col[j].remove(n)
                    square[(i // 3, j // 3)].remove(n)
       

            board[i][j] = '.'
            return False
            

        # find the first empty slot
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    dfs(i, j)
                    break
        

# harness = Solution()
test = [[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]]
# harness.solveSudoku(test)
# soln = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# print(test)
# assert(test == soln)

if __name__ == "__main__":
    harness_run(Solution(), [test])

