class Solution:
    def spiralOrder(self, matrix):
        # use for loops in a while loop
        # make the bounds smaller once a row/column is complete
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        ans = []
        while True:
            if len(ans) >= len(matrix) * len(matrix[0]):
                # need to return first x elements
                # no way around it, unless we add X, Y below
                return ans[: len(matrix) * len(matrix[0])]

            # go right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
                print(ans[-1], top, i)
            top += 1

            # go down
            # X: if bottom <= top:
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
                print(ans[-1], i, right)
            right -= 1

            # go left
            # Y: if left <= right:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
                print(ans[-1], bottom, i)
            bottom -= 1

            # go up
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
                print(ans[-1], i, left)
            left += 1


harness = Solution()

test = [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40, 41, 42],
    [43, 44, 45, 46, 47, 48, 49],
    [50, 51, 52, 53, 54, 55, 56],
    [57, 58, 59, 60, 61, 62, 63],
    [64, 65, 66, 67, 68, 69, 70],
]

sol = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    14,
    21,
    28,
    35,
    42,
    49,
    56,
    63,
    70,
    69,
    68,
    67,
    66,
    65,
    64,
    57,
    50,
    43,
    36,
    29,
    22,
    15,
    8,
    9,
    10,
    11,
    12,
    13,
    20,
    27,
    34,
    41,
    48,
    55,
    62,
    61,
    60,
    59,
    58,
    51,
    44,
    37,
    30,
    23,
    16,
    17,
    18,
    19,
    26,
    33,
    40,
    47,
    54,
    53,
    52,
    45,
    38,
    31,
    24,
    25,
    32,
    39,
    46,
]

print()
out = harness.spiralOrder(test)
print(out)
assert out == sol
