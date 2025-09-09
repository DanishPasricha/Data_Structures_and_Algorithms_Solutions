class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        MOD = 10**9 + 7
        share = 0
        dp = [0]*n
        dp[0] = 1
        for i in range(1, n):
            if i - delay >= 0:
                share =  (share + dp[i - delay]) % MOD
            if i - forget >= 0:
                share = ( share - dp[i - forget] ) % MOD
            dp[i] = share
        res = 0
        for i in range(n - forget, n):
            if i >= 0:
              res = (res + dp[i]) % MOD
        return res