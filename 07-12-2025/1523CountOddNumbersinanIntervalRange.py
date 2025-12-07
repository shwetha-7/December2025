import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2 or high%2:
            return 1+(high-low)//2
        elif not low%2 and not high%2:
             return (high-low)//2
         
class TestApp:
    def test_case_one(self):
        assert Solution().countOdds(3,7)==3
    def test_case_two(self):
        assert Solution().countOdds(8,10)==1
    def test_case_three(self):
        assert Solution().countOdds(4,8)==2