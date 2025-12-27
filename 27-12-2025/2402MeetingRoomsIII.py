class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # [end,count,0]
        meeting_count=[0]*n 
        timings=[0]*100000
        meetings.sort(key=lambda x:x[0])
        for meeting in meetings:
            start,end=meeting
            status=False 
            value=10**9
            index=-1
            for j in range(n):
                if timings[j]<value:
                    value=timings[j]
                    index=j 
                if timings[j]<=start:
                    meeting_count[j]+=1
                    status=True 
                    timings[j]=end 
                    break 
            if not status:
                meeting_count[index]+=1
                timings[index]+=(end-start)
        room_number=max_meetings=0 
        for i in range(n):
            if max_meetings<meeting_count[i]:
                max_meetings=meeting_count[i]
                room_number=i 
        return room_number
class TestApp:
    def test_case_one(self):
        assert Solution().mostBooked(2,[[0,10],[1,5],[2,7],[3,4]])==0
    def test_case_two(self):
        assert Solution().mostBooked(3,[[1,20],[2,10],[3,5],[4,9],[6,8]])==1
    def test_case_three(self):
        assert Solution().mostBooked(4,[[18,19],[3,12],[17,19],[2,13],[7,10]])==0