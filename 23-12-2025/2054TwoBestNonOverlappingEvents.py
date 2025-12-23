import heapq

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        result=[]
        events.sort(key=lambda x:x[0])
        max_value,max_sum=0,0
        for event in events:
            while result and result[0][0]<event[0]:
                max_value=max(max_value,result[0][1])
                heapq.heappop(result)
            max_sum=max(max_sum,max_value+event[2])
            heapq.heappush(result,(event[1],event[2]))
        return max_sum 
class TestApp:
    def test_case_one(self):
        assert Solution().maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]])==4
    def test_case_two(self):
        assert Solution().maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]])==5
    def test_case_three(self):
        assert Solution().maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]])==8    
