class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        n,count=len(prices),0
        if n==1:
            return 1
        left,right=0,1 
        while right<n:
              if prices[right-1]-prices[right]==1:
                  right+=1
              else:
                  length=right-left 
                  count=count+length*(length+1)//2 
                  left=right 
                  right+=1
        length=right-left
        count=count+length*(length+1)//2 
        return count 
        
class TestApp:
    def test_case_one(self):
        assert Solution().getDescentPeriods([3,2,1,4])==7
    def test_case_two(self):
        assert Solution().getDescentPeriods([8,6,7,7])==4
    def test_case_three(self):
        assert Solution().getDescentPeriods([1])==1               
        
        