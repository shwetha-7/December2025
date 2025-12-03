class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        pairs=[]
        n=len(points)
        for i in range(n):
            for j in range(i+1,n):
                pairs.append([points[i],points[j]])
        res=[]
        for i in range(len(pairs)):
            for j in range(i+1,len(pairs)):
                res.append([pairs[i],pairs[j]])
        count=0
        for pair in res:
            temp=self.checkParallel(pair[0],pair[1])
            if temp:
                print("Line are parallel : ",pair)
                count+=1 
        print("Count : ",count)
        return count 
        
    def checkParallel(self,line1:list[list[int]],line2:list[list[int]]):
        # check initial conditions 
        x1,x2,x3,x4=line1[0][0],line1[1][0],line2[0][0],line2[1][0]
        y1,y2,y3,y4=line1[0][1],line1[1][1],line2[0][1],line2[1][1]
        if (x1==x2 and x3==x4 and (x1==x3 or x2==x4)) or (y1==y2 and y3==y4 and (y1==y3 or y4==y2)):
            return False
        if (x1==x2 and x3==x4 and x1!=x3 and x2!=x4) or (y1==y2 and y3==y4 and y1!=y3 and y4!=y2):
            return True 
        if x1==x2 and x3!=x4: return False 
        if x1!=x2 and x3==x4: return False 
        # calculate slope
        slope1=((y2-y1)/(x2-x1))  
        slope2=((y4-y3)/(x4-x3))
        return slope1==slope2 
        v1 = (x1 == x2)
        v2 = (x3 == x4)
    
        if v1 and v2:
            # overlapping → NOT parallel
            return x1 != x3
        if v1 != v2:
            return False
    
        # --- Handle horizontal lines ---
        h1 = (y1 == y2)
        h2 = (y3 == y4)
    
        if h1 and h2:
            # overlapping → NOT parallel
            return y1 != y3
        if h1 != h2:
            return False
    
        # --- General slope case ---
        slope1 = (y2 - y1) * 1.0 / (x2 - x1)
        slope2 = (y4 - y3) * 1.0 / (x4 - x3)
    
        return slope1 == slope2
    
from collections import defaultdict
class Solution:
        def countTrapezoids(self, points: list[list[int]]) -> int:
          n = len(points)
          inf = 10**9 + 7
          slope_to_intercept = defaultdict(list)
          mid_to_slope = defaultdict(list)
          ans = 0
  
          for i in range(n):
              x1, y1 = points[i]
              for j in range(i + 1, n):
                  x2, y2 = points[j]
                  dx = x1 - x2
                  dy = y1 - y2
  
                  if x2 == x1:
                      k = inf
                      b = x1
                  else:
                      k = (y2 - y1) / (x2 - x1)
                      b = (y1 * dx - x1 * dy) / dx
  
                  mid = (x1 + x2) * 10000 + (y1 + y2)
                  slope_to_intercept[k].append(b)
                  mid_to_slope[mid].append(k)
  
          for sti in slope_to_intercept.values():
              if len(sti) == 1:
                  continue
  
              cnt = defaultdict(int)
              for b_val in sti:
                  cnt[b_val] += 1
  
              total_sum = 0
              for count in cnt.values():
                  ans += total_sum * count
                  total_sum += count
  
          for mts in mid_to_slope.values():
              if len(mts) == 1:
                  continue
  
              cnt = defaultdict(int)
              for k_val in mts:
                  cnt[k_val] += 1
  
              total_sum = 0
              for count in cnt.values():
                  ans -= total_sum * count
                  total_sum += count
  
          return ans


class TestApp:
    def test_case_one(self):
        assert Solution().countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]])==2
    def test_case_two(self):
        assert Solution().countTrapezoids([[0,0],[1,0],[0,1],[2,1]])==1
    def test_case_three(self):
        assert Solution().countTrapezoids([[71,-89],[-75,-89],[-9,11],[-24,-89],[-51,-89],[-77,-89],[42,11]])==10   