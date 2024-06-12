import random

class Solution:
    def __init__(self, n, blacklist):
        bLen = len(blacklist)
        self.blackListMap = {}
        blacklistSet = set(blacklist)

        for b in blacklist:
            if b >= (n-bLen):
                continue
            self.blackListMap[b] = None
        
        start = n-bLen
        for b in self.blackListMap.keys():
            while start < n and start in blacklistSet:
                start += 1
            self.blackListMap[b] = start
            start += 1
        self.numElements = n - bLen

    def pick(self):
        randIndex = int(random.random() * self.numElements)
        return self.blackListMap[randIndex] if randIndex in self.blackListMap else randIndex