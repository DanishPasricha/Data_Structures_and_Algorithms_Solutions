class Solution:
    def compareVersion(self,version1, version2):
        parts1 = version1.split('.')
        parts2 = version2.split('.')
        
        for i in range(max(len(parts1), len(parts2))):
            v1 = int(parts1[i]) if i < len(parts1) else 0
            v2 = int(parts2[i]) if i < len(parts2) else 0
            
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        
        return 0


# Optimized Approach:

# Split both version strings into their revision parts using the dot '.' as a separator.
# Compare the revision parts of both versions directly without converting to integers.
# Return -1 if version1 is smaller, 1 if version1 is greater, and 0 if they're equal.
# Time Complexity: O(N + M), where N is the length of version1 and M is the length of version2.
# Space Complexity: O(N + M), to store the split revision parts.