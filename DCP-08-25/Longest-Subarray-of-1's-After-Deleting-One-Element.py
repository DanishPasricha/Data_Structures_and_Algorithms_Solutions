# Intuition
# When we must delete exactly one element to get the longest subarray of 1's, we're essentially looking for the longest subarray that contains at most one non-1 element. Think of it this way:

# If we find a subarray with exactly one 0, we delete that 0 → all remaining are 1's
# If we find a subarray with all 1's, we still must delete one 1 → we get (length-1) 1's
# The clever insight here is to use a sliding window that maintains at most one 0, and when calculating length, we intentionally exclude that 0 from our count since we plan to delete it.

# Approach
# This solution uses the sliding window technique with a smart counting mechanism:

# Key Variables:
# l (left pointer): Start of our current window
# r (right pointer): End of our current window
# k: Our "zero budget" - how many zeros we can still accommodate (starts at 1)
# m: Maximum length of valid subarray found so far
# Algorithm Logic:
# The algorithm works in three distinct scenarios:

# Scenario 1: Encountering a 1
# if nums[r]==1:
#     if r-l>m:
#         m=r-l
#     continue
# We found a 1, so our window is still valid
# Update maximum length using r-l (not r-l+1) because if there's a 0 in our window, we don't count it
# Continue expanding the window
# Scenario 2: First 0 encountered
# if k==1:
#     k-=1  # Use our zero budget
#     if r-l>m:
#         m=r-l
#     continue
# We can accommodate this 0 since k=1
# Decrease our zero budget to 0
# Update maximum length (still using r-l because we'll delete this 0)
# Scenario 3: Second 0 encountered (window invalid)
# else:
#     while nums[l]==1:  # Skip all 1's from left
#         l+=1
#     l+=1  # Skip the first 0 we encountered
#     if r-l>m:
#         m=r-l
# Our window now has 2 zeros, which violates our constraint
# Shrink window: Move l past all consecutive 1's until we hit the first 0
# Skip that 0: l+=1 removes the first 0 from our window
# Now our window contains only the current 0 at position r
# Reset our "zero budget" implicitly (k becomes 1 again for next iteration)
# Why r-l instead of r-l+1?
# This is the genius of this approach:

# Traditional window length = right - left + 1
# But here, when we have a 0 in our window, r-l gives us exactly the count of 1's
# Since we'll delete the 0, r-l is precisely our final answer for that window
# When window has all 1's, we still use r-l because we must delete one element anyway

# Complexity
# Time complexity: O(n)

# Each element is processed at most twice: once by the right pointer r, and potentially once by the left pointer l during window shrinking
# The inner while loop doesn't create additional complexity because each element is moved by l at most once throughout the entire algorithm
# Single pass with amortized constant work per element
# Space complexity: O(1)

# Only using a fixed number of integer variables (l, r, k, m)
# No additional data structures like arrays, hash maps, or recursion stack


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        k=1
        m=-1
        for r in range(len(nums)):
            if nums[r]==1:
                if r-l>m:
                    m=r-l
                continue
            else:
                if k==1:
                    k-=1
                    if r-l>m:
                        m=r-l
                    continue
                else:
                    while nums[l]==1:
                        l+=1
                    l+=1
                    if r-l>m:
                        m=r-l
        return m
                