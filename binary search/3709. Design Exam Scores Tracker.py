class ExamTracker:

    def __init__(self):
        self.times = []
        self.scores = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.scores.append(self.scores[-1] + score) 

    def totalScore(self, startTime: int, endTime: int) -> int:
        l = bisect_left(self.times, startTime)
        r = bisect_right(self.times, endTime)
        
        return self.scores[r] - self.scores[l]
        


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)