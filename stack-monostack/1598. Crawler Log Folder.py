class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == "../" :
                if stack:
                    stack.pop()
                continue
            if i == "./":
                continue
            stack.append(i)
        return len(stack)