class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = {}
        for i, w in enumerate(wordsContainer): 
            node = trie
            if '$' not in node or len(w) < node['$'][1]: 
                node['$'] = (i, len(w))
            for ch in reversed(w): 
                node = node.setdefault(ch, {})
                if '$' not in node or len(w) < node['$'][1]: 
                    node['$'] = (i, len(w))
        ans = []
        for w in wordsQuery: 
            node = trie 
            for ch in reversed(w):
                if ch not in node: break 
                node = node[ch]
            ans.append(node['$'][0])
        return ans 