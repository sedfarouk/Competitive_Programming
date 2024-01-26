class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        waitDays = [0] * n
        monostack = deque() 

        for i in range(n):
            while monostack and temperatures[monostack[-1]] < temperatures[i]:
                day = monostack.pop()
                waitDays[day] = i - day
            monostack.append(i)

        return waitDays
