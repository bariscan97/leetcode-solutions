class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for cur_idx in range(len(temperatures)):
            
            while stack and temperatures[cur_idx] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = cur_idx - idx

            stack.append(cur_idx)

        return answer
