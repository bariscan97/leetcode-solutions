class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                r -= 1
                l += 1
            return True
        def rec(i,string,arr):
            
            if i == len(s):
                
                if string and is_palindrome(i - len(string),i - 1):
                    # print(string,i - (len(string)),i)
                    res.append(arr + [string])
                return 
            # is_palindrome(i - (len(string) - 1),i)
            if string and is_palindrome(i - len(string),i - 1):
                # print(string,i - (len(string)),i)
                rec(i + 1,s[i],arr + [string])
            rec(i+1,string + s[i],arr)
        res = []
        rec(0,"",[])
        # print(res)
        return res