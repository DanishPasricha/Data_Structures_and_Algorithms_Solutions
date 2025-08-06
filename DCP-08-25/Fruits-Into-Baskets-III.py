class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        class SegmentTree:
            def __init__(self, nums):
                self.n = len(nums)
                self.tree = [0] * (4 * self.n)  # Tree size ~4n
                self.nums = nums[:]  # Copy of basket capacities
                self.build(1, 0, self.n - 1)
            
            def build(self, node, start, end):
                if start == end:
                    self.tree[node] = self.nums[start]
                    return
                mid = (start + end) // 2
                self.build(2 * node, start, mid)
                self.build(2 * node + 1, mid + 1, end)
                self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
            
            def update(self, node, start, end, idx, val):
                if start == end:
                    self.tree[node] = val
                    self.nums[start] = val
                    return
                mid = (start + end) // 2
                if idx <= mid:
                    self.update(2 * node, start, mid, idx, val)
                else:
                    self.update(2 * node + 1, mid + 1, end, idx, val)
                self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
            
            def query(self, node, start, end, target):
                if self.tree[node] < target:
                    return -1  # No basket with enough capacity in this range
                if start == end:
                    if self.nums[start] >= target:
                        self.update(1, 0, self.n - 1, start, -1)  # Mark basket as used
                        return start
                    return -1
                mid = (start + end) // 2
                # Check left subtree first for leftmost basket
                if self.tree[2 * node] >= target:
                    return self.query(2 * node, start, mid, target)
                # If left subtree fails, try right subtree
                return self.query(2 * node + 1, mid + 1, end, target)
        
        tree = SegmentTree(baskets)
        unplaced = 0
        for fruit in fruits:
            if tree.query(1, 0, len(baskets) - 1, fruit) == -1:
                unplaced += 1
        return unplaced