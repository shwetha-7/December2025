
# Recursion 
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n=len(corridor)
        mod=10**9+7 
        def helper(index:int,cnt:int)->int:
            if index==n:
                return 1 if cnt==2 else 0 
            if cnt==2:
                if corridor[index]=='S':
                    result=helper(index+1,1)
                else:
                    result=(helper(index+1,0)+helper(index+1,2))%mod 
            else:
                if corridor[index]=='S':
                    result=helper(index+1,cnt+1)
                else:
                    result=helper(index+1,cnt)
            return result 
        return helper(0,0)%mod 
# Using dynamic Programming 
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n=len(corridor)
        dp=[[-1]*3 for _ in range(n)]
        mod=10**9+7 
        def helper(index:int,seats:int):
            if index==n:
               return 1 if seats==2 else 0 
            if dp[index][seats]!=-1:
                return dp[index][seats]
            if seats==2:
                if corridor[index]=='S':
                    result=helper(index+1,1)
                else:
                    result=(helper(index+1,0)+helper(index+1,2))%mod 
            else:
                if corridor[index]=='S':
                    result=helper(index+1,seats+1)
                else:
                    result=helper(index+1,seats)
            dp[index][seats]=result
            return dp[index][seats]
        return helper(0,0)

class TestApp:
    def test_case_one(self):
        assert Solution().numberOfWays("SSPPSPS")==3
    def test_case_two(self):
        assert Solution().numberOfWays("PPSPSP")==1
    def test_case_three(self):
        assert Solution().numberOfWays("S")==0
    