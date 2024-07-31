from random import randint, random
# polynomial value-restricted 0/1 knapsack

# Given a set of items, each with an arbitrary positive weight and a value = 1 or 2 ,
# determine which items to include in a collection so that the total weight is less than
# or equal to a given limit and the total value is as large as possible.

# Find a polynomial algorithm.

def knapsack(limit, weights, values):
    # we know sum(values) <= 2 * len(values), a multiple of n.
    # therefore iterate on total value instead of total weight limit
    # runtime: O((2 * len(values)) * len(values)) -> O(n^2)
    
    # dp[i][j] represents minimum total weight, given total value i and using up to index j items
    dp = [[limit + 1] * (len(values)) for _ in range(2 * len(values) + 1)]
    # parent[i][j] := ('e' or 'i', parent_i, parent_j)
    # if 'i' is set, it means value[j] is used, otherwise not
    # Use parent_i, parent_j to get ancestor.
    parent = [[('e', -1, -1)] * (len(values)) for _ in range(2 * len(values) + 1)]
    # can achieve weight 0 for 0 total value, using upto any indices
    for i in range(len(values)):
        dp[0][i] = 0
    # recurrence relation uses i - 1, set up base case for i = 0
    dp[values[0]][0] = weights[0]
    parent[values[0]][0] = ('i', -1, -1)
    # start backtracking from parent_bt to get included elements
    parent_bt = (-1, -1)
    
    for i in range(1, 2 * len(values) + 1):
        for j in range(1, len(values)):
            # to consider including the current value, does the prev subresult exist?
            include = limit + 1
            if i - values[j] >= 0:
                include = dp[i - values[j]][j - 1] + weights[j]
            exclude = dp[i][j - 1]
            
            if min(include, exclude) >= limit + 1:
                # no solution to value i using upto element j
                continue
            
            if exclude <= include:
                dp[i][j] = exclude
                parent[i][j] = ('e', i, j - 1)
            else:
                dp[i][j] = include # include element j
                parent[i][j] = ('i', i - values[j], j - 1)
                parent_bt = (i, j)

    
    # retrieve included items using parent
    items_values = []
    items_weights = []
    items_indices = []
    i, j = parent_bt
    while True:
        if i < 0 or j < 0:
            break
        if parent[i][j][0] == 'i':
            items_indices.append(j)
            items_values.append(values[j])
            items_weights.append(weights[j])
        i, j = (parent[i][j][1], parent[i][j][2])
    
    items_values.reverse()
    items_weights.reverse()
    items_indices.reverse()

    j = 0
    visual = []
    for i in range(len(values)):
        if j < len(items_indices) and items_indices[j] == i:
            visual.append('+')
            j += 1
        else:
            visual.append(' ')
    


    def visualize(buffer, input):
        frame = []
        for i in range(len(input)):
            used = len(str(input[i]))
            unused = buffer - used
            left = unused // 2
            right = unused - left

            for j in range(left):
                frame.append(' ')
            frame.append(str(input[i]))
            for j in range(right):
                frame.append(' ')
            if i != len(input) - 1:
                frame.append('|')
        return "".join(frame)
    
    print()
    print(f'limit: {limit}')
    print(f'total value:  {sum(items_values)}')
    print(f'total weight: {sum(items_weights)}')

    print()
    buffer = len(str(max(weights + values)))
    print(f'values:  {visualize(buffer + 2, values)}')
    print(f'weights: {visualize(buffer + 2, weights)}')
    print(f'include: {visualize(buffer + 2, visual)}')
    print()
        
    return



# limit = 6
# values = [1, 2, 1, 2, 1, 2]
# weights = [1, 3, 20, 1, 1, 1]
# knapsack(limit, weights, values)

limit = 10
values = []
weights = []
for i in range(20):
    values.append(randint(1, 2))
    weights.append(randint(1, 10))
knapsack(limit, weights, values)


    





