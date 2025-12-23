import bisect

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        rows,cols=len(strs),len(strs[0])
        max_sorted_length=1
        dp=[1]*cols 
        for i in range(cols):
            for j in range(i):
                valid=True 
                for k in range(rows):
                    if strs[k][j]>strs[k][i]:
                        valid=False 
                        break 
                if valid:
                    dp[i]=max(dp[i],dp[j]+1)
            max_sorted_length=max(max_sorted_length,dp[i])
        return cols-max_sorted_length
class TestApp:
    def test_case_one(self):
        assert Solution().minDeletionSize(["babca","bbazb"])==3
    def test_case_two(self):
        assert Solution().minDeletionSize(["edcba"])==4
    def test_case_three(self):
        assert Solution().minDeletionSize(["ghi","def","abc"])==0