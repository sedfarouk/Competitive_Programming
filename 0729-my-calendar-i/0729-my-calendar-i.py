class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.calendar:
            if s < endTime <= e or s <= startTime < e:
                return False
            elif (s <= startTime and endTime <= e) or (s >= startTime and endTime >= e):
                return False
        
        self.calendar.append((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)