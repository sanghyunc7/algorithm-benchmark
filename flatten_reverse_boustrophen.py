# flatten reverse boustrophen style grid


def flatten(board):
    ans = []

    board.reverse()
    for i in range(len(board)):
        row = board[i]
        if i % 2 == 1:
            row.reverse()
        for j in row:
            ans.append(j)

    return ans


board = [
    [36, 35, 34, 33, 32, 31],
    [25, 26, 27, 28, 29, 30],
    [24, 23, 22, 21, 20, 19],
    [13, 14, 15, 16, 17, 18],
    [12, 11, 10, 9, 8, 7, 6],
    [1, 2, 3, 4, 5],
]

print(flatten(board))
