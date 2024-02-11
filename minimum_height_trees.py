# https://leetcode.com/problems/minimum-height-trees/discuss/76149/Share-my-Accepted-BFS-Python-Code-with-O(n)-Time
https://leetcode.com/problems/minimum-height-trees/
# construct graph
# find leaf nodes
# perform bfs on each leaf node, at the same time ("meet in the middle")
# imagine removing the leaf nodes on each pass. the tree is getting smaller
# the last one or two surviving leaf nodes are the middle ones
# those middle ones will have the shortest tree heights since they were in the middle