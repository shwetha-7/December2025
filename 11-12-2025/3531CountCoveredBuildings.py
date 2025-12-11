

class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        grid=[[0 for _ in range(n)] for _ in range(n)]
        for building in buildings:
            grid[building[0]-1][building[1]-1]+=1
        count=0
        for i in range(1,n):
            for j in range(1,n):
                if grid[i][j]:
                    res=self.helper(grid,i,j,n)
                    if res:
                        count+=1
        return count
            
    def checkTop(self,row:int,col:int,grid:list[list[int]]):
        if row<0:
            return False 
        if grid[row][col]==1:
            return True 
        return self.checkTop(row-1,col,grid)
    def checkBottom(self,row:int,col:int,grid:list[list[int]],n:int):
        if row==n:
            return False 
        if grid[row][col]==1:
            return True 
        return self.checkBottom(row+1,col,grid,n)
    def checkLeft(self,row:int,col:int,grid:list[list[int]]):
        if col<0:
            return False
        if grid[row][col]==1:
            return True 
        return self.checkLeft(row,col-1,grid)
    def checkRight(self,row:int,col:int,grid:list[list[int]],n:int):
        if col==n: return False 
        if grid[row][col]:
            return True 
        return self.checkRight(row,col+1,grid,n)
    def helper(self,grid:list[list[int]],row:int,col:int,n:int):
        top=self.checkTop(row-1,col,grid)
        bottom=self.checkBottom(row+1,col,grid,n)
        left=self.checkLeft(row,col-1,grid)
        right=self.checkRight(row,col+1,grid,n)
        return top and bottom and left and right
class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        count=0
        max_row=[0]*(n+1)
        min_row=[n+1]*(n+1)
        max_col=[0]*(n+1)
        min_col=[n+1]*(n+1)
        for building in buildings:
            x,y=building[0],building[1]
            max_row[y]=max(max_row[y],x)
            min_row[y]=min(min_row[y],x)
            max_col[x]=max(max_col[x],y)
            min_col[x]=min(min_col[x],y)
        for building in buildings:
            x,y=building[0],building[1]
            if min_row[y]<x<max_row[y] and min_col[x]<y<max_col[x]:
                count+=1
        return count  
class TestApp:
    def test_case_one(self):
        assert Solution().countCoveredBuildings(3,[[1,2],[2,2],[3,2],[2,1],[2,3]])==1
    def test_case_two(self):
        assert Solution().countCoveredBuildings(3,[[1,1],[1,2],[2,1],[2,2]])==0
    def test_case_three(self):
        assert Solution().countCoveredBuildings(5,[[1,3],[3,2],[3,3],[3,5],[5,3]])==1
         
        