class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        n=len(complexity)
        for i in range(1,n):
            if complexity[i]<=complexity[0]:
                return 0
        return self.factorial(n-1)
    def factorial(self,number:int)->int:
        value=1
        mod=10**9+7
        while number>1:
              value=(value*number)%mod
              number-=1
        return value

class TestApp:
    def test_case_one(self):
        assert Solution().countPermutations([1,2,3])==2
    def test_case_two(self):
        assert Solution().countPermutations([3,3,3,4,4,4])==0
        