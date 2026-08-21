class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0]*len(temperatures)
        stack = []
        for idx in range(len(temperatures)):
            while len(stack)>0 and stack[-1][1]< temperatures[idx]:
                element = stack.pop()
                days[element[0]] = idx - element[0]
            stack.append((idx,temperatures[idx]))
        return days
