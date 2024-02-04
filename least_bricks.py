from collections import defaultdict


class Solution:
    def leastBricks(self, wall):
        # create dictionary, collect number of times
        # that we reach a certain total width from left
        # find largest number in dict.values()

        widths = defaultdict(int)
        for row in wall:
            width = 0
            for i in row:
                width += i
                widths[width] += 1

        # remove key of the rightermost edge
        widths.pop(sum(wall[0]))
        v = list(widths.values())
        # in case no middle lines
        v.append(0)
        # number of times we achieve this width
        mx = max(v)
        # number of times we have to go through bricks for that width
        return len(wall) - mx
