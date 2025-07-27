class Solution:
    def numOfSubsequences(self, s: str) -> int:
        size = len(s)
        a = b = 0
        prefix = [0] * size
        suffix = [0] * size

        for i in range(size):
            if s[i] == 'L':
                a += 1
            if s[size - 1 - i] == 'T':
                b += 1
            prefix[i] = a
            suffix[size - 1 - i] = b

        x = y = z = zz = 0

        for i in range(size):
            if s[i] == 'C':
                x += (prefix[i] + 1) * suffix[i]
                y += prefix[i] * (suffix[i] + 1)
                zz += prefix[i] * suffix[i]
            z = max(z, prefix[i] * suffix[i])

        return max(x, y, z + zz)