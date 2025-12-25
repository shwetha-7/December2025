class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        value=max_happiness=0
        for i in range(k):
            if happiness[i]-value>=0:
                max_happiness+=happiness[i]-value 
            else:
                break
            value+=1
        return max_happiness    
    
class TestApp:
    def test_case_one(self):
        assert Solution().maximumHappinessSum([1,2,3],2)==4
    def test_case_two(self):
        assert Solution().maximumHappinessSum([1,1,1,1],2)==1
    def test_case_three(self):
        assert Solution().maximumHappinessSum([2,3,4,5],1)==5