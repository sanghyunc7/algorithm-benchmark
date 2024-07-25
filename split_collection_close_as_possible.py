def split_collection(collection):
    n = len(collection)
    total_sum = sum(collection)
    target = total_sum // 2

    # Create a DP table where dp[i][j] is True if a subset of sum j can be formed from the first i numbers
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True  # Zero sum is possible with zero elements

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(target + 1):
            dp[i][j] = dp[i - 1][j] or (j >= collection[i - 1] and dp[i - 1][j - collection[i - 1]])

    # Find the closest sum to target that is achievable
    closest_sum = 0
    for j in range(target, -1, -1):
        if dp[n][j]:
            closest_sum = j
            break

    # Backtrack to find the elements of the first subcollection
    subset1 = [] # will contain elements adding up to closest_sum (to the 'target')
    subset2 = collection[:]
    i, j = n, closest_sum
    while i > 0 and j > 0:
        # if dp needs i-th element (1-based indexing) to make up to sum j
        # move that element to subset1
        if not dp[i - 1][j]:
            print('asdf', collection[i - 1], subset2)
            subset1.append(collection[i - 1])
            subset2.remove(collection[i - 1])
            j -= collection[i - 1]
        i -= 1
    print(closest_sum)
    return subset1, subset2

# Example usage
collection = [3,3,3,3,3,3]
subset1, subset2 = split_collection(collection)
print("Subset 1:", subset1)
print("Subset 2:", subset2)
print("Sum of Subset 1:", sum(subset1))
print("Sum of Subset 2:", sum(subset2))
