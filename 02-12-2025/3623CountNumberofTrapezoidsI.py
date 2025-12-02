from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        hash_map=defaultdict(int)
        for point in points:
            y=point[1]
            hash_map[y]+=1
        res=[]
        mod=10**9+7
        for key in hash_map:
            n=hash_map[key]
            if n>1:
                res.append(n*(n-1)//2)
        count=0 
        n=len(res)
        sum_total=sum(res)%mod
        for x in res:
            sum_total=(sum_total-x)%mod
            count=(count+sum_total*x)%mod
            
        return count 
class TestApp:
    def test_case_one(self):
        assert Solution().countTrapezoids([[1,0],[2,0],[3,0],[2,2],[3,2]])==3
    def test_case_two(self):
        assert Solution().countTrapezoids([[0,0],[1,0],[0,1],[2,1]])==1