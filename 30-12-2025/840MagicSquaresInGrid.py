class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        count=0
        rows,cols=len(grid),len(grid[0])
        def check_magic_matrix(row:int,col:int):
            nonlocal rows,cols
            set_1=set()
            for i in range(3):
                for j in range(3):
                    set_1.add(grid[row+i][col+j])
            if len(set_1)!=9: return False 
            row_1=grid[row][col]+grid[row][col+1]+grid[row][col+2]
            row_2=grid[row+1][col]+grid[row+1][col+1]+grid[row+1][col+2]
            row_3=grid[row+2][col]+grid[row+2][col+1]+grid[row+2][col+2]
            col_1=grid[row][col]+grid[row+1][col]+grid[row+2][col]
            col_2=grid[row][col+1]+grid[row+1][col+1]+grid[row+2][col+1]
            col_3=grid[row][col+2]+grid[row+1][col+2]+grid[row+2][col+2]
            dia_1=grid[row][col]+grid[row+1][col+1]+grid[row+2][col+2]
            dia_2=grid[row][col+2]+grid[row+1][col+1]+grid[row+2][col]
            return row_1==row_2==row_3==col_1==col_2==col_3==dia_1==dia_2
        for row in range(rows-2):
            for col in range(cols-2):
                if check_magic_matrix(row,col):
                    count+=1
        return count 
class TestApp:
    def test_case_one(self):
        assert Solution().numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]])==1
    def test_case_two(self):
        assert Solution().numMagicSquaresInside([[8]])==0