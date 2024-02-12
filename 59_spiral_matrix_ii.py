class Solution:
    def generateMatrix(self, n):
        # same code for spiral_matrix_1 should work
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        i = 1
        matrix = [[0] * n for _ in range(n)]

        while True:
            if i > n**2:
                return matrix

            # go right
            for j in range(left, right + 1):
                matrix[top][j] = i
                i += 1
            top += 1

            # check if we are done
            # need to check every for_loop instead of
            # every while loop because row/column gaps could clash
            # for instance, left..right+1 = 1, but bottom..top + 1 = 0
            if i > n**2:
                return matrix

            # go down
            for j in range(top, bottom + 1):
                matrix[j][right] = i
                i += 1
            right -= 1

            if i > n**2:
                return matrix

            # go left
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = i
                i += 1
            bottom -= 1

            if i > n**2:
                return matrix

            # go up
            for j in range(bottom, top - 1, -1):
                matrix[j][left] = i
                i += 1
            left += 1
