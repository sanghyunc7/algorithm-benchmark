class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # Initialize leaves
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Initialize internal nodes
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, value):
        # Update leaf node
        index += self.n
        self.tree[index] = value
        # Update internal nodes
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def query(self, left, right):
        # Query range sum
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

# Example usage:
data = [1, 2, 3, 4, 5]
seg_tree = SegmentTree(data)

# Query the sum from index 1 to 4
print(seg_tree.query(1, 4))  # Output: 9 (2 + 3 + 4)

# Update the value at index 2 to 10
seg_tree.update(2, 10)

# Query again the sum from index 1 to 4
print(seg_tree.query(1, 4))  # Output: 16 (2 + 10 + 4)
