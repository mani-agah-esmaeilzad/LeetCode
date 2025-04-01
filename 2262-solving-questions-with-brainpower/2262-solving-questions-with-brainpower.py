class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [q[0] for q in questions]

        for i in range(n-2,-1,-1):
            out_range = i + questions[i][1] + 1
            if out_range < n:
                dp[i] += dp[out_range]
            dp[i] = max(dp[i],dp[i+1])
        return dp[0]