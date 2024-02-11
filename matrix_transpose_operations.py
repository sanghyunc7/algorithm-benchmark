def reset(m1, m2):
    m1[:] = [[1, 2], [3, 4]]
    m2[:] = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]



# in-place
def topleft_bottomright_transpose(grid):
    n = len(grid)
    for i in range(n):
        for j in range(i + 1, n):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    print("topleft_bottomright_transpose")
    print(grid)

m1, m2 = [], []
reset(m1, m2)
topleft_bottomright_transpose(m1)
topleft_bottomright_transpose(m2)

# in-place
def bottomleft_topright_transpose(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n - i - 1):
            grid[i][j], grid[n - 1 - j][n -1 - i] = grid[n - 1 - j][n - 1 - i], grid[i][j] 
    print("bottomleft_topright_transpose")
    print(grid)


reset(m1, m2)
bottomleft_topright_transpose(m1)
bottomleft_topright_transpose(m2)

def flip_vertical(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n // 2):
            grid[i][j], grid[i][n - 1 - j] = grid[i][n - 1 - j], grid[i][j]
    print("flip_vertical")
    print(grid)

reset(m1, m2)
flip_vertical(m1)
flip_vertical(m2)


def flip_horizontal(grid):
    n = len(grid)
    for i in range(n // 2):
        for j in range(n):
            grid[i][j], grid[n - 1 - i][j] = grid[n - 1 - i][j], grid[i][j]
    print("flip_horizontal")
    print(grid)

reset(m1, m2)
flip_horizontal(m1)
flip_horizontal(m2)



# 1 2
# 3 4

# 1 2 3
# 4 5 6
# 7 8 9

# 7 4 1
# 8 5 2
# 9 6 3