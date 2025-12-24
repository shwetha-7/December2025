class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort(reverse=True)
        n=len(capacity)
        total_apples=sum(apple)
        current_total=0
        for i in range(n):
            current_total+=capacity[i]
            if current_total>=total_apples:
                return i+1
        return n 
class TestApp:
    def test_case_one(self):
        assert Solution().minimumBoxes([1,3,2],[4,3,1,5,2])==2
    def test_case_two(self):
        assert Solution().minimumBoxes([5,5,5],[2,4,2,7])==4       
        