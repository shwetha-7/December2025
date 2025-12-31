class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        end_day=-1
        mat=[[0 for _ in range(col)] for _ in range(row)]
        visited=[[False for _ in range(col)] for _ in range(row)]
        for  r,c in cells:
             if self.checkToReachBottom(mat,visited,row,col):
                 end_day+=1
             mat[r-1][c-1]=1
        return end_day
    def checkToReachBottom(self,mat:list[list[int]],visited:list[list[int]],rows:int,cols:int)->bool:
        
        def helper(row:int,col:int)->bool:
            if row==rows-1: return True 
            status=False 
            # check bottom
            if row+1<rows and not status and not visited[row+1][col] and not mat[row+1][col]:
                visited[row+1][col]=True 
                status = status or helper(row+1,col)
                visited[row+1][col]=False 
            # check top 
            if row-1>=0 and not status and not visited[row-1][col] and not mat[row-1][col]:
                visited[row-1][col]=True 
                status = status or helper(row-1,col)
                visited[row-1][col]=False 
            # check left 
            if col-1>=0 and not status and not visited[row][col-1] and not mat[row][col-1]:
                visited[row][col-1]=True 
                status = status or helper(row,col-1)
                visited[row][col-1]=False 
            if col+1<cols and not status and not visited[row][col+1] and not mat[row][col+1]:
                visited[row][col+1]=True 
                status = status or helper(row,col+1)
                visited[row][col+1]=False 
            return status
        
        for j in range(cols):
            if mat[0][j]==0 and helper(0,j):
                return True 
        return False
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        dsu=DSU(row*col+2)
        mat=[[0 for _ in range(col)] for _ in range(row)]
        dirs=[[1,0],[0,1],[-1,0],[0,-1]]
        n=len(cells)
        for i in range(n-1,-1,-1):
            r,c=cells[i][0]-1,cells[i][1]-1
            id1=r*col+c+1
            mat[r][c]=1
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc 
                if 0<=nr<row and 0<=nc<col and mat[nr][nc]==1:
                    id2=nr*col+nc+1
                    dsu.union(id1,id2)
                if r==0:
                    dsu.union(0,id1)
                if r==row-1:
                    dsu.union(row*col+1,id1)
                if dsu.find(0)==dsu.find(row*col+1):
                    return i 
        return -1 
    
class DSU:
    def __init__(self,n:int):
        self.root=list(range(n))
    def find(self,x:int):
        if self.root[x]!=x:
            return self.find(self.root[x])
        return self.root[x]
    def union(self,x:int,y:int):
        rx=self.find(x)
        ry=self.find(y)
        if rx==ry: return 
        self.root[rx]=ry 
        
            
    

class TestApp:
    def test_case_one(self):
        assert Solution().latestDayToCross(2,2,[[1,1],[2,1],[1,2],[2,2]])==2
    def test_case_two(self):
        assert Solution().latestDayToCross(2,2,[[1,1],[1,2],[2,1],[2,2]])==1
    def test_case_three(self):
        assert Solution().latestDayToCross(3,3,[[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]])==3
        