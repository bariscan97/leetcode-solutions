class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack
        # split by /
        word_list = path.split('/')
        stack = []
        for word in word_list:
            if not word:
                continue
            elif word == '..':
                if stack:
                    stack.pop()
            elif word == '.':
                continue
            else:
                stack.append(word)
        return "/" + "/".join(stack)