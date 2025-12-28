class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count=0
        m,n=len(grid),len(grid[0])
        for i in range(m):
            # edge case 
            if grid[i][0]<0:
                count+=n 
            else:
                # left range 
                left,right=1,n-1
                while left<=right:
                      mid=left+(right-left)//2 
                      if grid[i][mid]<0:
                          right=mid-1
                      else:
                          left=mid+1
                count+=n-left 
        return count 
                
class TestApp:
    def test_case_one(self):
        assert Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])==8
    def test_case_two(self):
        assert Solution().countNegatives([[3,2],[1,0]])==0