class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        curr = nums[0]
        for x in nums[1:]:
            # Replace non-coprime numbers w/LCM
            if gcd(curr, x) > 1:
                curr = lcm(curr, x)

                # Pop stack if no longer coprime
                while ans and gcd(curr, ans[-1]) > 1:
                    curr = lcm(curr, ans.pop())
            else:
                # Push coprime number to stack
                ans.append(curr)
                curr = x
            
        # Push coprime number to stack
        ans.append(curr)

        return ans